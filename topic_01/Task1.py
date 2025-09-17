text = input("Введіть текст з 10 знаками: ")

if len(text) > 10:
    print("Знаків більше ніж 10")
elif len(text) < 10:
   print("Знаків менше ніж 10")
else:
    reserved = text[::-1]
    print(reserved)
