data_list = []

i = int(input("Podaj ile liczb chcesz umieścić na liście: "))

while i > 0:
    data_list.append(int(input("Podaj liczbę: ")))
    i -= 1

print(f"Wprowadzone lista: {data_list}")
print(f"Posortowana lista: {sorted(data_list)}")
