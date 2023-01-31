BASE = 7

def itov(x):
    digits = []
    if x == 0:
        digits.append(0)
    while x > 0:
        digits.append(x % BASE)
        x //= BASE
    digits.reverse()
    return digits

def gen(pos = 0, minute = False, smaller = False):
    max_val = max_minute if minute else max_hour
    if pos >= len(max_val):
        if minute:
            return 1
        else:
            return gen(0, True)
    else:
        ans = 0
        for digit in range(BASE):
            if not used[digit] and (smaller or digit <= max_val[pos]):
                used[digit] = True
                ans += gen(pos + 1, minute, smaller or digit < max_val[pos])
                used[digit] = False
        return ans

n, m = map(int, input().split())
n -= 1
m -= 1
used = [False] * BASE
max_hour = itov(n)
max_minute = itov(m)
print(gen())