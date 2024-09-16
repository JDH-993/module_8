def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for i in range(len(numbers)):
        try:
            result = result + numbers[i]
        except TypeError:
            incorrect_data = incorrect_data + 1
            print(f"В numbers записан некорректный тип данных: {numbers[i]}")
    return [result, incorrect_data]
def calculate_average(numbers):
    try:
        r = len(numbers)
    except:
        print(f"В numbers записан некорректный тип данных: {numbers}")
        return None

    o = personal_sum(numbers)
    try:
        u = o[0]/(len(numbers) - o[1])
        return u
    except ZeroDivisionError:
        return 0


print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать