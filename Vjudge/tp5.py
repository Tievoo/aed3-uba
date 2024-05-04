tests = []

n = int(input())

while n != 0:
    a = input().split()
    a_int = list(map(int, a))

    tests.append(a_int)
    n = int(input())

for test in tests:
    work_units = 0
    wine_sum = 0

    #req = request for selling/buying wine
    for req in test:
        # we sum to work units the absolute value of the sum of demands for wine
        # if we need 10 units of wine and we have 5, we need to buy 5 units, so we add 5 to work_units
        # and viceversa
        work_units += abs(wine_sum)
        wine_sum += req
    
    print(work_units)