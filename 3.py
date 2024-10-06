def count_vowels(s):
    vowels = "aeiouAEIOU"
    k = 0
    for char in s:
        if char in vowels:
            k += 1
    return k
input_string = input("Введіть рядок: ")
print(f"Кількість голосних: {count_vowels(input_string)}")
