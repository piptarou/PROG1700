import pygame, os, datetime, sqlite3
from sqlite3 import Error

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Py Py Revolution!")

BACKGROUND = pygame.image.load(os.path.join('assets', 'background.png'))
END_BACKGROUND = pygame.image.load(os.path.join('assets', 'end_background.png'))

BLACK = (0, 0, 0)
FPS = 60
ARROW_SPEED = 4
ARROW_WIDTH, ARROW_HEIGHT = 79, 79

PRESS_AREA_START_Y = 500
'''Area for arrows to collide with.
   Adjust the fourth number to change the difficulty, I've set it at what I consider a medium difficulty.
   Bigger = easier, but may cause scoring for the next arrow'''
PRESS_AREA_RECT = pygame.Rect(280, 0, 350, 30)

# This is the control area
ARROW_OUTLINE_IMAGE = pygame.image.load(os.path.join('assets', '0base.png'))
ARROW_OUTLINE = pygame.transform.scale(ARROW_OUTLINE_IMAGE, (350, 90))

ARROW_PRESS_IMAGE = pygame.image.load(os.path.join('assets', '00base.png'))
ARROW_PRESS = pygame.transform.scale(ARROW_PRESS_IMAGE, (350, 90))

ARROW_LEFT_IMAGE = pygame.image.load(os.path.join('assets', '1left_arrow.png'))
ARROW_LEFT = pygame.transform.scale(ARROW_LEFT_IMAGE, (ARROW_WIDTH, ARROW_HEIGHT))

ARROW_DOWN_IMAGE = pygame.image.load(os.path.join('assets', '2down_arrow.png'))
ARROW_DOWN = pygame.transform.scale(ARROW_DOWN_IMAGE, (ARROW_WIDTH, ARROW_HEIGHT))

ARROW_UP_IMAGE = pygame.image.load(os.path.join('assets', '3up_arrow.png'))
ARROW_UP = pygame.transform.scale(ARROW_UP_IMAGE, (ARROW_WIDTH, ARROW_HEIGHT))

ARROW_RIGHT_IMAGE = pygame.image.load(os.path.join('assets', '4right_arrow.png'))
ARROW_RIGHT = pygame.transform.scale(ARROW_RIGHT_IMAGE, (ARROW_WIDTH, ARROW_HEIGHT))

database = r".\pyscore.db"\

def draw_window(arrows, score):
    WIN.fill(BLACK)
    WIN.blit(BACKGROUND, (0, 0))

    #   This shows the player when they're pressing a control button and is easier to judge if the arrows are being hit.
    key_press = pygame.key.get_pressed()
    if key_press[pygame.K_a]:
        WIN.blit(ARROW_PRESS, (280, 0))
        check_arrow_hit(arrows, 0, score)
    if key_press[pygame.K_s]:
        WIN.blit(ARROW_PRESS, (280, 0))
        check_arrow_hit(arrows, 1, score)
    if key_press[pygame.K_w]:
        WIN.blit(ARROW_PRESS, (280, 0))
        check_arrow_hit(arrows, 2, score)
    if key_press[pygame.K_d]:
        WIN.blit(ARROW_PRESS, (280, 0))
        check_arrow_hit(arrows, 3, score)

    #   Draws ARROW_OUTLINE on top of ARROW_PRESS
    WIN.blit(ARROW_OUTLINE, (280, 0))

    '''
    Draws arrows on top of the control arrows. The order for drawing is important, it goes from bottom up.
    We want the song arrows over the control arrows or they get covered and the player can't see them.
    '''
    for x, y, arrow_type in arrows:
        if arrow_type == 0:
            WIN.blit(ARROW_LEFT, (x, y))
        elif arrow_type == 1:
            WIN.blit(ARROW_DOWN, (x, y))
        elif arrow_type == 2:
            WIN.blit(ARROW_UP, (x, y))
        elif arrow_type == 3:
            WIN.blit(ARROW_RIGHT, (x, y))

#   Display score
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    WIN.blit(score_text, (10, 10))

#   Display controls
    font = pygame.font.Font(None, 25)
    controls_text = font.render(f"Controls:", True, (255, 255, 255))
    left_text = font.render(f"Left: A", True, (255, 255, 255))
    down_text = font.render(f"Down: S", True, (255, 255, 255))
    up_text = font.render(f"Up: W", True, (255, 255, 255))
    right_text = font.render(f"Right: D", True, (255, 255, 255))
    WIN.blit(controls_text, (10, 60))
    WIN.blit(left_text, (10, 90))
    WIN.blit(down_text, (10, 110))
    WIN.blit(up_text, (10, 130))
    WIN.blit(right_text, (10, 150))

    '''
    This adds a collider in for the arrows hitting the control area.
    It makes a copy the arrow list from the load_assets function so that when a player correctly
    hits their arrow, it disappears.
    '''
def check_arrow_hit(arrows, expected_arrow_type, score):
    for arrow in arrows[:]:  # This uses a copy of the arrows list to allow removal during iteration
        x, y, arrow_type = arrow
        arrow_rect = pygame.Rect(x, y, ARROW_WIDTH, ARROW_HEIGHT)

        if arrow_type == expected_arrow_type and arrow_rect.colliderect(PRESS_AREA_RECT):
            arrows.remove(arrow)  # This removes an arrow only when it's within the press area
            score += 1

    return score

def create_connection(db_file):
    """
    create a database connection to the SQLite database
    specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):
    """
    create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def make_table():
    sql_create_highscore_table = """ CREATE TABLE IF NOT EXISTS highscore (
                                        id INTEGER PRIMARY KEY,
                                        finalscore INTEGER NOT NULL,
                                        timestamp TEXT NOT NULL
                                    ); """
    conn = create_connection(database)
    if conn is not None:
        create_table(conn, sql_create_highscore_table)
    else:
        print("Error! cannot create the database connection.")

def create_score(conn, finalscore,timestamp):
#   Puts a score into the highscore table

    sql = ''' INSERT INTO highscore(finalscore,timestamp)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, (finalscore,timestamp))
    conn.commit()
    return cur.lastrowid

#   This reads the binary file and puts them in a list, it reads line by line to check where the arrow is designated.
def load_assets():
    arrow_positions = []
    with open('assets/middleschool.txt', 'r') as file:
        song = file.readlines()

    for y, line in enumerate(song):
        for x, number in enumerate(line.strip()):
        #   This reads the txt file line by line to determine where the '1's are in the list, after enumerating the list.
        #   It then determines the position on the x axis before appending and returning it to the list where a copy is made and used later.
            if number == '1':
                x_position = (WIDTH - ARROW_WIDTH * len(line.strip())) / 2 + x * ARROW_WIDTH
                arrow_positions.append((x_position, y * ARROW_HEIGHT, int(x)))

    return arrow_positions

#   The UTF error I was getting is because Pygame doesn't play nice with mp3 files.
#   I converted the song to a wav and made it shorter.
def play_music():
    pygame.mixer.music.load(os.path.join('assets', 'middleschool.wav'))
    pygame.mixer.music.play()

#   This is the function to create an end screen.
def end_level(score):
    WIN.fill(BLACK)
    WIN.blit(END_BACKGROUND, (0, 0))
    font = pygame.font.Font(None, 60)
    end_score = font.render(f"Final Score: {score}", True, (255, 255, 255))
    WIN.blit(end_score, (300, 140))

    #   It's always important to credit the creators of any assets, I also ensured that they were license-free for personal use
    font = pygame.font.Font(None, 40)
    credits = font.render(f"Credits", True, (255, 255, 255))
    WIN.blit(credits, (300, 200))

    font = pygame.font.Font(None, 20)
    credit_idea = font.render(f"Miranda Johnson -- Design including arrows and their layout", True, (255, 255, 255))
    WIN.blit(credit_idea, (300, 240))

    font = pygame.font.Font(None, 20)
    credit_music = font.render(f"Floor Model -- Middle School Mayhem (song)", True, (255, 255, 255))
    #   https://uppbeat.io/track/floor-model/middle-school-mayhem
    WIN.blit(credit_music, (300, 260))
    #   https://deep-fold.itch.io/space-background-generator
    font = pygame.font.Font(None, 20)
    credit_bg = font.render(f"Deep-Fold on itch.io -- Space Background Generator", True, (255, 255, 255))

    WIN.blit(credit_bg, (300, 280))

def main():
    play_music()

    arrows = load_assets()
    clock = pygame.time.Clock()
    make_table()  #   Create the table outside the game loop

    conn = create_connection(database)
    if conn is None:
        print("Error! cannot create the database connection.")
        return

    arrow_score = 0

    running = True

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #   This saves the score and timestamp and inserts into a db file
                finalscore = arrow_score
                timestamp = datetime.datetime.now()
                create_score(conn, finalscore, timestamp)
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            arrow_score = check_arrow_hit(arrows, 0, arrow_score)
        if keys[pygame.K_s]:
            arrow_score = check_arrow_hit(arrows, 1, arrow_score)
        if keys[pygame.K_w]:
            arrow_score = check_arrow_hit(arrows, 2, arrow_score)
        if keys[pygame.K_d]:
            arrow_score = check_arrow_hit(arrows, 3, arrow_score)

        for i in range(len(arrows)):
            x, y, arrow_type = arrows[i]
            arrows[i] = (x, y - ARROW_SPEED, arrow_type)

        #   This checks if mixer.music is busy (playing music) and if so, it shows the game screen.
        if pygame.mixer.music.get_busy() > 0:
            draw_window(arrows, arrow_score)

        #   If mixer.music is not busy, it shows to the end screen.
        if pygame.mixer.music.get_busy() == 0:
            end_level(arrow_score)

        pygame.display.flip()
    pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()