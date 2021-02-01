line_length = 5
symbols = "#*$"
i = 0

symbols_list = list(symbols)
symbols_list_lenght = len(symbols_list)-1
import random

while i < line_length:
    last_element = random.randint(0,symbols_list_lenght)
    print(symbols_list[last_element], end='')
    i += 1
else:
    print("", end='\n')
