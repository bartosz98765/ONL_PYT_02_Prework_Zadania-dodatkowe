list_of_list = []
string_list_1 = ["Piłka", "noga", "opona"]
string_list_2 = ["nnn", "ppp", "ccc", "zzz"]
string_list_3 = ["123p", "p321", "987z", "345c", "150n"]
nr_p = 0

list_of_list.append(string_list_1)
list_of_list.append(string_list_2)
list_of_list.append(string_list_3)

for element_list in list_of_list:
    for element in element_list:
        letters = list(element)
        for element_letter in letters:
            if element_letter == "p" or element_letter == "P":
                nr_p += 1
print(nr_p)
