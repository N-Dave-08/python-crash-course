#1
evens = [x for x in range(10) if x % 2 == 0]
print(evens)

#2
a, b = (5, 10)
print(a, b)

#use case
name = ["Ac", "John", "Barbara"]
short_names = [n for n in name if len(n) <= 4]
print(short_names)
