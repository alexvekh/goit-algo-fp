def greedy_algorithm(budget, items):
    # Сортування по співвідношенню calories / cost в порядку спадання
    sorted_items = sorted(items.items(), key=lambda item: item[1]["calories"] / item[1]["cost"], reverse=True)

    choised_items = []  # Список для зберігання обраних items
    total_calories = 0  # Загальна кількість калорій

    for item in sorted_items:
        item_name = item[0]
        item_cost = item[1]['cost']
        item_calories = item[1]['calories']
        
        if item_cost <= budget:
            choised_items.append(item_name)
            total_calories += item_calories
            budget -= item_cost

    return choised_items, total_calories, budget



def dynamic_programming(budget, items):
    # Ініціалізація таблиці DP. dp[i] зберігає максимальні калорії для бюджету i
    dp = [0] * (budget + 1)
    
    # Зберігаємо вибір предметів для кожного бюджету
    item_choice = [[] for _ in range(budget + 1)]

    for item, properties in items.items():
        cost = properties['cost']
        calories = properties['calories']
        
        # Проходимо таблицю DP у зворотному порядку, щоб уникнути повторного вибору того ж предмета
        for current_budget in range(budget, cost - 1, -1):
            if dp[current_budget - cost] + calories > dp[current_budget]:
                dp[current_budget] = dp[current_budget - cost] + calories
                item_choice[current_budget] = item_choice[current_budget - cost] + [item]
    
        # Знаходимо загальну вартість обраних предметів
    total_cost = sum(items[item]['cost'] for item in item_choice[budget])
    
    # Вираховуємо залишок бюджету
    remaining_budget = budget - total_cost
    
    return item_choice[budget], dp[budget], remaining_budget

def greedy_algorithm_repeated(budget, items):
    # Жадібний алгоритм на випадок коли можна вибирати декілька однакових предметів
    # Сортування по співвідношенню calories / cost в порядку спадання
    sorted_items = sorted(items.items(), key=lambda item: item[1]["calories"] / item[1]["cost"], reverse=True)

    choised_items = {}  # Словник для зберігання обраних items
    total_calories = 0  # Загальна кількість калорій

    for item in sorted_items:
        item_name = item[0]
        item_cost = item[1]['cost']
        item_calories = item[1]['calories']
        
        if item_cost <= budget:
            # Скільки одиниць цього предмета можна придбати за залишковий бюджет
            num_items = budget // item_cost
            choised_items[item_name] = num_items
            total_calories += num_items * item_calories
            budget -= num_items * item_cost

    return choised_items, total_calories, budget



def dynamic_programming_repeated(budget, items):
    # Ініціалізація таблиці DP. dp[i] зберігає максимальні калорії для бюджету i
    dp = [0] * (budget + 1)
    
    # Зберігаємо вибір предметів для кожного бюджету
    item_choice = [{} for _ in range(budget + 1)]

    for current_budget in range(1, budget + 1):
        for item, properties in items.items():
            cost = properties['cost']
            calories = properties['calories']
            if cost <= current_budget:
                if dp[current_budget - cost] + calories > dp[current_budget]:
                    dp[current_budget] = dp[current_budget - cost] + calories
                    item_choice[current_budget] = item_choice[current_budget - cost].copy()
                    if item in item_choice[current_budget]:
                        item_choice[current_budget][item] += 1
                    else:
                        item_choice[current_budget][item] = 1

    # Знаходимо загальну вартість обраних предметів
    total_cost = sum(items[item]['cost'] * count for item, count in item_choice[budget].items())
    
    # Вираховуємо залишок бюджету
    remaining_budget = budget - total_cost
    
    return item_choice[budget], dp[budget], remaining_budget


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 101  # Прикладовий бюджет

for alg in [greedy_algorithm, dynamic_programming, greedy_algorithm_repeated, dynamic_programming_repeated]:
    choised_items, total_calories, change = alg(budget, items)
    print("\n    ", alg.__name__)
    print(f"Обрані {alg.__name__} предмети: {choised_items}")
    print("Загальна кількість калорій:", total_calories)
    if change != 0:
        print("Решта:", change, "грн.")

print()