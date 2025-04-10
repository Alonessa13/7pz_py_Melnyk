# Введення діапазону
low = int(input("Введи нижню межу: "))
high = int(input("Введи верхню межу: "))

found_any = False

print("Прості числа в цьому діапазоні:")

for num in range(low, high + 1):
    if num > 1:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end=' ')
            found_any = True

if not found_any:
    print("У цьому діапазоні немає простих чисел.")
