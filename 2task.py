import random

secret_number = random.randint(1, 100)

print("Я загадав число від 1 до 100. В тебе є 7 спроб вгадати його!")

for attempt in range(1, 8):
    guess = int(input(f"Спроба {attempt}: "))

    if guess == secret_number:
        print(f"Ти вгадав число з {attempt} спроби! Молодець!")
        break
    elif guess < secret_number:
        print("Моє число більше.")
    else:
        print("Моє число менше.")

else:
    print(f"Ти не вгадав. Загадане число було: {secret_number}")
