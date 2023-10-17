principal = 1000 # initial amount
rate = 5 / 100 # APR (5%)
years = 10 # number of years

for number in range(years):
    principal += principal * rate
    print("years", number+1, round(principal, 2))