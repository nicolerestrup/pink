data_list = [5, 2, 7, -3, 6, 9, 0]
for existing_number in range(len(data_list)):
    for sencount_number in range(existing_number + 1, len(data_list)):
        if data_list[existing_number] > data_list[sencount_number]:
            data_list[existing_number], data_list[sencount_number] = data_list[sencount_number], data_list[existing_number]
print(data_list)
