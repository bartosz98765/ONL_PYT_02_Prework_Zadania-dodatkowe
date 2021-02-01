def add_to_dict( mydictionary, mytuple ):
    mydictionary[mytuple[0]] = mytuple[1]
    print(mydictionary)
    return( mydictionary )


d = {}
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