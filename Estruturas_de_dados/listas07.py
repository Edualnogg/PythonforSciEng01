
j = '*'
for i in range(20):
    print(j)
    j += '*'
    n = 2
    if i >= 19:
        for k in range(20):
            print(j[n:])
            n += 1
