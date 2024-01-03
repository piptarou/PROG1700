amount = 1_000 # principal loan amount
apr = 1.05 # 5% interest
term = 10 # years
#I used (term) for the range so that it could be changed later.
for i in range(term):
    amount = amount * apr
    print(f"year {i}: {amount}")