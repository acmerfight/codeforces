import sys, re

n = raw_input()
regular_one = re.compile(r"R(\d+)C(\d+)")
regular_two = re.compile(r"([A-Z]+)(\d+)") 

def base26(n):
    r = ""
    while(n):
        r = chr(ord('A')+(n-1)%26) + r
        n = (n-1) / 26
    return r

def decimal(s):
    r = 0
    for c in s:
        r *= 26
        r += ord(c) - ord('A') + 1
    return r

for line in sys.stdin:
    m = regular_one.match(line)
    if m:
        print base26(int(m.group(2))) + m.group(1)
    else:
        m = regular_two.match(line)
        print "R" + m.group(2) + "C" + str(decimal(m.group(1)))
        
