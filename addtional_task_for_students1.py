# TODO Написать свою реализацию функции для подсчёта числа вхождение элементов в список
def my_count(l: list, item) -> int:
    count = 0
    for element in l:
        if element == item:
            count += 1
    return count


# Ввод данных
if __name__ == "__main__":
    try:
        # Ввод списка
        input_list = input("Введите элементы списка через пробел: ").split()
        # Преобразование в числа
        input_list = [int(x) if x.isdigit() else x for x in input_list]

        # Ввод элемента
        search_item = input("Введите нужный элемент для подсчета: ")
        # Преобразование в число
        if search_item.isdigit():
            search_item = int(search_item)

        # Подсчет вхождений
        result = my_count(input_list, search_item)

        # Вывод результата
        print(f"Количество вхождений в элементов в список {search_item}: {result}")
    except ValueError:
        print("Ошибка. Введите другие данные")