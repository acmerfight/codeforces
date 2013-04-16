vowel_set = set(['a', 'e', 'i', 'o', 'u', 'y'])

word = list(raw_input().lower())
copy_word = word[:]

for letter in copy_word:
    if letter in vowel_set:
        word.remove(letter)

word = '.'.join(word)

print '.' + word
