#Day 32

import random as r
langs = ["こんにちは", "안녕하세요", "สวัสดี", "Привіт"]
rand_lang = r.randint(0,len(langs)-1)
# print(f"Here's a greeting in a random language! {rand_lang}")
print(f"{langs[rand_lang]}")