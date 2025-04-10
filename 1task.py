# дані 
start_sum = float(input("Введіть початкову суму вкладу: "))
percent = float(input("Введіть річну процентну ставку (%): "))
target_sum = float(input("Введіть бажану кінцеву суму: "))
years = 0
current_sum = start_sum
# Цикл працює, поки сума не досягне бажаної
while current_sum < target_sum:
    years += 1
    current_sum += current_sum * (percent / 100)
    print(f"Після {years} року(ів): {round(current_sum, 2)} грн")
print(f"Щоб досягти {target_sum} грн, знадобиться {years} рік(років).")
