def solution():
    e, s, m = map(int, input().strip().split(" "))
    e_max, s_max, m_max = 15, 28, 19

    for i in range(e_max*m_max):
        year = s_max*i+s-1
        if year % e_max == e-1 and year % m_max == m-1:
            print(year+1)
            break


def solution2():
    a, b, c = map(int, input().split())
    answer = (28*19*13*a+15*19*17*b+15*28*10*c) % (15*28*19)
    print(answer) if answer != 0 else print(7980)


solution()
