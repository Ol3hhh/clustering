list1 = [1, 2, 3, 4]
list2 = [1, 3, 2, 4]

# Підрахунок збігів з урахуванням порядку
matches = sum(1 for x, y in zip(list1, list2) if x == y)

print("Кількість збігів:", matches)  # Виведе: Кількість збігів: 2
