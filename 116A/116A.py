total = input()
result = 0
result_list = []
for index in range(total):
    out_number, in_number = map(int, raw_input().split())
    result += in_number - out_number 
    result_list.append(result)
    
print sorted(result_list)[-1] 
