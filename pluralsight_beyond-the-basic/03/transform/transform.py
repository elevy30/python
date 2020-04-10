from pprint import pprint as pp

sunday = [12, 14, 15, 17, 20, 22, 22, 23, 22, 20, 18]
monday = [13, 14, 13, 14, 20, 22, 23, 19, 18, 18, 17]
tuesday = [2, 3, 4, 7, 9, 10, 14, 10, 8, 7, 6]

print()
print("simple print")
for item in zip(sunday, monday, tuesday):
    print(item)

print()
print("pp daily print")
daily = [sunday, monday, tuesday]
pp(daily)

print()
type(daily)
print("taken from list print")
for item in zip(daily[0], daily[1], daily[2]):
    pp(item)
print()
print()
for item in zip(*daily):
    pp(item)

print()
pp(daily)
print()
print("list of zip which convert the column to row")
transposed = list(zip(*daily))
pp(transposed)

print("list of zip which convert the column to row")
transposed_transposed = list(zip(*transposed))
pp(transposed_transposed)