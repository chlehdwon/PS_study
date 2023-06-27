def solve():
    a = dict()
    h_sum = 0

    for _ in range(9):
        h = int(input())
        a[h] = 1
        h_sum += h

    target = h_sum - 100
    for x in a:
        if x != target-x and target-x in a:
            del a[x]
            del a[target-x]
            break
    dwarf = sorted(list(a))
    for num in dwarf:
        print(num)


solve()
