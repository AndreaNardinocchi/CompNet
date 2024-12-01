inp = input('Enter Fahrenheit Temperature: ')
fahr = float(inp)
cel = round((fahr - 32.0) * 5.0 / 9.0, 2)
print(cel)
