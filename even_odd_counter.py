list = [12, 14, 2, 3, 9, 11, 10]
even_list = []
odd_list = []
for n in list:
    if n%2 == 0:
        even_list += [n]
    else:
        odd_list += [n]
print(len(even_list))
print(len(odd_list))
