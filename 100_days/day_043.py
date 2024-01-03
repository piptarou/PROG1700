import random as r

bingo_card = []

def bingo_gen():
    number = r.randint(1, 90)
    return number

def card():
    for row in bingo_card:
        print(row)

numbers = []
for i in range(8):
    numbers.append(bingo_gen())

numbers.sort()

bingo_card = [[numbers[0], numbers[1], numbers[2]],
              [numbers[3], "bingo", numbers[4]],
              [numbers[5], numbers[6], numbers[7]]
              ]

card()