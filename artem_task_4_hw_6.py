# create ne dict
after = {}

before = {'id1':

{
'name': 'Ruslan',
'class': 1,
'subjects' : {'Math', 'Algorithms', 'English'}

},

'id2':

{

'name': 'Mark',
'class': 2,
'subjects' : {'Geometry', 'Java', 'Cooking'}

},

'id3':

{

'name': 'Ruslan',
'class': 1,
'subjects' : {'Math', 'Algorithms', 'English'}

}

}

# get list keys of dict before
list_of_keys = list(before.keys())
range_of_before = range(0, len(list_of_keys) - 1)

for i in range_of_before:
    if before == after:
        print("ok")
        break
    else:
        after[list_of_keys[i]] = before.get(list_of_keys[i])
print(after)
