total = input()
name_score = {}
for index in range(total):
    name, score = raw_input().split() 
    if name in name_score:
        name_score[name][0] += int(score)
        name_score[name][1] = index
    else:
        temp_dict = {name: [int(score), index]}
        name_score.update(temp_dict)
sorted_by_socore = sorted(name_score.items(), key=lambda d:d[1][0], reverse=True)
max_item = sorted_by_socore[0] 
for item in sorted_by_socore[1:]:
    if max_item[1][0] == item[1][0] and max_item[1][1] > item[1][1]:
        max_item = item
    else:
        break
print max_item[0]
