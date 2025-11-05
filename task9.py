def find_minimum(data: list[float]) -> float:
    if not data:
        raise ValueError("Список не должен быть пустым.")

    minimum = data[0]

    for element in data:
        if element < minimum:
            minimum = element

    return minimum


if __name__ == "__main__":
    numbers = [5, 2, 9, 1, 5, 6, 0.5, 3]

    try:
        min_value = find_minimum(numbers)
        print(f"Исходный список: {numbers}")
        print(f"Минимальный элемент: {min_value}")

    except ValueError as e:
        print(f"Ошибка: {e}")