shedule = {'monday': ['clean house', 'drive car', 'meet with freands'], 'thuesday': None, 'wednesday': ['manicure', 'hammam', 'beer']}

print(list(shedule.values()))


list_values = list(shedule.values())
list_values.remove(None)

empty_list = []

for i in range(0,len(list_values) ):
    empty_list.extend(list_values[i])

print(len(empty_list))




# link to Python.org dictionary
https://docs.python.org/3/tutorial/datastructures.html#dictionaries