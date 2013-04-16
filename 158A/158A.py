n, k = map(int, raw_input().split())
data_list = map(int, raw_input().split())
count = 0
for data in data_list:
    if data >= data_list[k-1] and data > 0:
        count += 1
    elif data < data_list[k-1]:
        break
print count
