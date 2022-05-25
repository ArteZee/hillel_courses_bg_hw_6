# create new dict
numbers = {}

for i in range(11, 21):
    numbers[i] = i ** 2
# summarize values of dict
summ_of_dic_values = sum(numbers.values())


print(numbers)
print(summ_of_dic_values)