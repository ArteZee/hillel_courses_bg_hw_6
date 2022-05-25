data = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]

# create new data list
new_list_data = []

list_data_for_dict = []
the_final_list = []
final_dict={}

# get data length
range_data = range(0, len(data) )
new=[]
b=[]


for i in range_data:
    new_list_data.extend(data[i].values())
# Создал сначала множество чтоб убрать дубликаты
sett_list_data = set(new_list_data)
# Перевел в список чтоб можно было обращаться и вызывать при необходимости
list_set_data=list(sett_list_data)

# Выполнение обычного задания БЕЗ УСЛОЖНЕНИЯ
print(sett_list_data)
# print(list_set_data)

for i in range_data:
    list_data_for_dict.extend(list(data[i].items()))
    new.extend(list(list_data_for_dict[i]))

for a in list_set_data:
    if a in the_final_list:
        pass
    else:
        the_final_list.extend(new[new.index(a)-1:new.index(a)+1])
# print(the_final_list)

k = range(0, len(the_final_list) -1, 2)

for y in k:
    final_dict[the_final_list[y]] = the_final_list[y+1]
    b.append(final_dict.copy())
    final_dict.clear()


print(b)



