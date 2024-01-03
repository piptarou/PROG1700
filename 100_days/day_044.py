import random as r, os, time

def bingo_gen():
    number = r.randint(1, 90)
    return number

def pretty_print(bingo_card):
  for row in bingo_card:
    for i in row:
      print(i, end = "\t|\t")
    print()

def card_gen():
    numbers = []
    for i in range(8):
        num = bingo_gen()
        while num in numbers:
           num = bingo_gen()
        numbers.append(num)
    
    numbers.sort()

    bingo_card = [[numbers[0], numbers[1], numbers[2]],
                [numbers[3], "bingo", numbers[4]],
                [numbers[5], numbers[6], numbers[7]]
                ]
    return bingo_card

def score_count(bingo_card):
    score = 0
    for row in bingo_card:
        for i in row:
            if i == "X":
                score += 1
    return score

def main():
    bingo_card = card_gen()
    while True:
        pretty_print(bingo_card)
        num = int(input("Number: "))
        for row in range(3):
            for i in range(3):
                if bingo_card[row][i] == num:
                    bingo_card[row][i] = "X"

        final_score = score_count(bingo_card)
        if final_score == 8:
            print("BINGO!")
            break

        time.sleep(1)
        os.system("cls")

if __name__ == "__main__":
    main()