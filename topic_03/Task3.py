print("=== Тестування методів словників ===")
dict = {'a':1,'b':2,'c':3}
print("Початковий словник:     ",dict)
dict.update({'d':4, 'b':20})
print("update({'d':4, 'b':20}):",dict)
del dict['a']
print("del dict['a']:          ",dict)
print("keys():                 ", list(dict.keys()))
print("values():               ", list(dict.values()))
print("items():                ", list(dict.items()))
dict.clear()
print("clear():                ",dict)