# 1 - misol 
text = input("Kiriting: ")

for i, harf in enumerate(text, start=1):
    print(f"{i} - {harf}")

# 2 - misol
name = input("Ismni kiriting: ")

if len(name) <= 2:
    print("Chiqish:", name)
else:
    middle = "X" * (len(name) - 2)
    masked = name[0] + middle + name[-1]
    print("Chiqish:", masked)

# 3 - misol
my_tuple = ("a", "b", "c", "d")
result = tuple((i, my_tuple[i]) for i in range(len(my_tuple)))
print(result)

# 4 - misol
t = ("apple", "banana", "ok")
res = tuple(s[::-1] for s in t)
print(res)
