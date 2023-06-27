n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))


def solve(nums):
    for n in nums:
        h, t, o = n//60, (n % 60) // 10, n % 10
        # when minute is more than 35, press MINT and one more ADDH
        if t >= 4 or (t == 3 and o >= 6):
            h += 1
            t = 6-t
            # when o>=5, press MINO and prss MINT one less time.
            if o >= 5:
                t -= 1
                o = 10-o
                print(h, 0, t, 0, o)
            # else, pree ADDO and pree MINT
            else:
                print(h, 0, t, o, 0)
        # when minute is le than 35, press ADDT.
        else:
            # when o>5, press MINO and one more ADDT
            if o > 5:
                t += 1
                o = 10 - o
                print(h, t, 0, 0, o)
            # else, press ADDO
            else:
                print(h, t, 0, o, 0)


solve(nums)
