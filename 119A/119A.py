def gcd(a, b):
    return a if not b else gcd(b, a % b)

Simon_number, Antisimon_number, total = map(int, raw_input().split())
flag = True

while total >= 0:
    if flag:
        total -= gcd(Simon_number, total)
    else:
        total -= gcd(Antisimon_number, total)

    flag = not flag

    if total < 0:
        print 0 if flag == 1 else 1
