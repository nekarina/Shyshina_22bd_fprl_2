a = int(input("Введіть a: "))

if a <= 0:
    print(0)
elif a == 1:
    print(1)
else:
    b, c = 0, 1
    for _ in range(2, a + 1):
        b, c = c, b + c
    print(f"Число Фібоначчі для a={a}: {c}")