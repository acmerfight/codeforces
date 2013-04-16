from math import ceil

total = input()

data_list = raw_input().split()

one_count = data_list.count("1")
two_count = data_list.count("2")
three_count = data_list.count("3")

taxi_count = data_list.count("4") 

three_combine_one = min(one_count, three_count)
taxi_count += three_combine_one
one_count -= three_combine_one
three_count -= three_combine_one

two_combine_two = two_count / 2
taxi_count += two_combine_two
two_count = two_count % 2

if three_count:
    taxi_count += three_count

if two_count:
    taxi_count += 1
    one_count -= 2

if one_count > 0:
    if one_count % 4 == 0:
        taxi_count += one_count / 4
    else:
        taxi_count += (one_count / 4 + 1) 

print taxi_count
