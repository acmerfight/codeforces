total = input()
score_list = []
data = [] 
name_score = {}
for index in range(total):
    name, score = raw_input().split() 
    data.append((name, int(score)))
    name_score[name] = name_score.get(name, 0) + int(score)
for name, score in name_score.iteritems():
    score_list.append(score)

max_score = max(score_list)
temp = {}
for NameScore in data:
    name, score = NameScore
    temp[name] = temp.get(name, 0) + score
    if temp[name] >= max_score and name_score[name] == max_score:
        print name
        break

