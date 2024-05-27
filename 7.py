"""
Необхідно написати програму на Python, яка імітує велику кількість кидків кубиків, 
обчислює суми чисел, які випадають на кубиках, і визначає ймовірність кожної можливої суми.

Створіть симуляцію, де два кубики кидаються велику кількість разів. 
Для кожного кидка визначте суму чисел, які випали на обох кубиках. 
Підрахуйте, скільки разів кожна можлива сума (від 2 до 12) з’являється у процесі симуляції. 
Використовуючи ці дані, обчисліть імовірність кожної суми.

На основі проведених імітацій створіть таблицю або графік, 
який відображає ймовірності кожної суми, виявлені за допомогою методу Монте-Карло.

Таблиця ймовірностей сум при киданні двох кубиків виглядає наступним чином.

Сума	Імовірність
2	2.78% (1/36)
3	5.56% (2/36)
4	8.33% (3/36)
5	11.11% (4/36)
6	13.89% (5/36)
7	16.67% (6/36)
8	13.89% (5/36)
9	11.11% (4/36)
10	8.33% (3/36)
11	5.56% (2/36)
12	2.78% (1/36)
Порівняйте отримані за допомогою методу Монте-Карло результати з аналітичними розрахунками, 
наведеними в таблиці вище.
"""

import random
import matplotlib.pyplot as plt

def roll_dice(num_rolls):
    sums = [0] * 13  # Ініціалізація списку для підрахунку сум від 2 до 12

    for _ in range(num_rolls):
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        total = roll1 + roll2
        sums[total] += 1

    return sums

def calculate_probabilities(sums, num_rolls):
    probabilities = [0] * 13

    for i in range(2, 13):
        probabilities[i] = (sums[i] / num_rolls) * 100

    return probabilities

def print_probabilities(probabilities):
    print("  {:5}    {:7}".format("Сума", "Імовірність"))
    print("-"*23)
    for i in range(2, 13):
        c = probabilities[i]

        p = probabilities[i]
        f = p/2.777777
        print("{:5} | {:7.2f}% ({}/36)".format(i, p, round(f)))

def plot_probabilities(probabilities):
    sums = list(range(2, 13))
    plt.bar(sums, probabilities[2:13], tick_label=sums, color='skyblue')
    plt.xlabel('Сума')
    plt.ylabel('Імовірність (%)')
    plt.title('Ймовірність сум при киданні двох кубиків')
    plt.show()

def main():
    num_rolls = 1000000  # Кількість кидків
    sums = roll_dice(num_rolls)
    probabilities = calculate_probabilities(sums, num_rolls)
    print_probabilities(probabilities)
    plot_probabilities(probabilities)

if __name__ == "__main__":
    main()
