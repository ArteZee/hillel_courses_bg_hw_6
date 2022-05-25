first = {1: 10, 2: 20}

second = {3: 30, 4: 40}

third = {5: 50, 6: 60}

fourth = {7: 70, 8: 80}

fifth = {9: 90, 10: 100}

# general_dict = first | second | third | fourth | fifth
new_dict = {}

# unite first dict in general
for k, v in first.items():
    new_dict[k] = v

# unite second dict in general
for k, v in second.items():
    new_dict[k] = v

# unite third dict in general
for k, v in third.items():
    new_dict[k] = v

# unite fourth dict in general
for k, v in fourth.items():
    new_dict[k] = v

# unite fifth dict in general
for k, v in fifth.items():
    new_dict[k] = v

print(new_dict)
