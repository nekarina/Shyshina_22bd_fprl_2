array = []
for i in range(25):
    while True:
        try:
            num = float(input(f"Введіть число {i+1}: "))
            array.append(num)
            break
        except ValueError:
            print("Будь ласка, введіть правильне число.")
array.sort(reverse=True)
print([array[i] for i in range(1, 25, 2)])

