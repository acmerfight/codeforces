total = input()
record = list(raw_input())

start_pos = 0
end_pos = 0
if "R" in record and "L" in record:
    flag = ""
    index = 0
    for sub_record in record:
        index += 1
        if sub_record == "R" or sub_record == "L":
            start_pos = index
            flag = sub_record
            break

    index = 0
    for sub_record in record:
        index += 1
        if sub_record != flag and sub_record != ".":
            end_pos = index
            break

    print start_pos, end_pos-1 

if "R" in record and "L" not in record:
    record = "".join(record)
    start_pos = record.find("R") + 1
    for index in range(start_pos-1, total):
        record = list(record)
        if record[index] == "R":
            end_pos = index + 1

    print start_pos, end_pos+1

if "L" in record and "R" not in record:
    record = "".join(record)
    end_pos = record.find("L")
    for index in range(end_pos, total):
        record = list(record)
        if record[index] == "L":
            start_pos = index + 1

    print start_pos, end_pos
