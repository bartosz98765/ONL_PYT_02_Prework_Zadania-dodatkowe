number = int(input("Podaj liczbę: "))

def dividers_odd( number ):
    dividers_list = []
    i = 1
    while i <= number // 2:
        if number % i == 0 and odd_number(i) != 0:
                dividers_list.append(i)
        i += 1
    if len(dividers_list) == 1:
        dividers_list.append(number)
    return (dividers_list)

def odd_number( number ):
    dividers_odd_nr = number
    i = number // 2
    while i > 1:
        if (number % i) == 0:
            dividers_odd_nr = 0
            break
        else:
            i -= 1
    return (dividers_odd_nr)


print(f"Dzieliniki pierwsze liczby {number} to: {dividers_odd(number)}")
