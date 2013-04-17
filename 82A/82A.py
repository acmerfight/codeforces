nth_can = input()

name_list = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]

n = 0
while True:
    n += 1
    total_number = 5 * pow(2, n) - 5
    if total_number >= nth_can:
        break

current_number = 5 * pow(2, n-1) - 5 
tmp_number = nth_can - current_number
for index in range(1, 6):
    if tmp_number <= (pow(2, n-1) * index):
        print name_list[index-1]
        break

