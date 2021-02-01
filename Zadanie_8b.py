result = {}
d = {}

def add_to_dict( mydictionary, mytuple ):
    if not (mytuple[0] in mydictionary):
        mydictionary[mytuple[0]] = mytuple[1]
    else:
        if type(result[mytuple[0]]) == type(42):
            mydictionary_value_list = []
            mydictionary_value_list.append(result[mytuple[0]])
            mydictionary_value_list.append(mytuple[1])
            mydictionary[mytuple[0]] = mydictionary_value_list
        else:
            mydictionary_value_list = []
            mydictionary_value_list.extend(result[mytuple[0]])
            mydictionary_value_list.append(mytuple[1])
            mydictionary[mytuple[0]] = mydictionary_value_list
    print(mydictionary)
    return( mydictionary )


t = ("pierwszy", 11, "drugi", 22, "trzeci", 33)
result = add_to_dict( d, t )
print(result)

t = ("pierwszy", 111, "drugi", 22, "trzeci", 33)
result = add_to_dict( d, t )
print(result)

t = ("drugi", 22)
result = add_to_dict( d, t )
print(result)

t = ("trzeci", 33)
result = add_to_dict( d, t )
print(result)

t = ("drugi", 222)
result = add_to_dict( d, t )
print(result)

t = ("drugi", 2222)
result = add_to_dict( d, t )
print(result)

t = ("drugi", 22222)
result = add_to_dict( d, t )
print(result)