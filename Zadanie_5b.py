string_list = ['ala', 'ma', 'piegi']
i = 0
for element in string_list:
    if  len(element) > 2:
        list_element = list(element)
        if  list_element[0] == list_element[len(element)-1]:
            i += 1
print(i)
