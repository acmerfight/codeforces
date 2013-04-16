total = input()

for index in xrange(total):
    words = raw_input().strip()
    if len(words) > 10:
        print words[0] + str(len(words) - 2) + words[-1]
    else:
        print words
