while True:
    user_input = input("Введи ціле невід'ємне число: ")

    if user_input.isdigit():
        number = int(user_input)
        break
    else:
        print("Помилка! Потрібно ввести ціле число, не менше 0.")

factorial = 1
steps = ""

counter = 1
while counter <= number:
    factorial *= counter
    steps += str(counter)
    if counter != number:
        steps += "*"
    counter += 1

print(f"{number}! = {steps} = {factorial}")
