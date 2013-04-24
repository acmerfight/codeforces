input_data = map(int, raw_input().split())
path_input = raw_input()
total_time = input_data[0]
startX, startY = input_data[1], input_data[2]
endX, endY = input_data[3], input_data[4]

distanceX = endX - startX
distanceY = endY - startY

path_record = {} 
path_record["N"], path_record["S"] = (distanceY, 0) if distanceY > 0 else (0, -distanceY)
path_record["E"], path_record["W"] = (distanceX, 0) if distanceX > 0 else (0, -distanceX)

for now_time in xrange(0, total_time):
    now_wind = path_input[now_time]
    path_record[now_wind] -= 1
    if path_record["E"] < 1 and path_record["W"] < 1 and path_record["S"] < 1 and path_record["N"] < 1:
        print now_time + 1
        break
else:
    print -1
