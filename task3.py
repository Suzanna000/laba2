def calculate_factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Факториал определён только для неотрицательных чисел.")
    elif n == 0:
        return 1
    else:
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        return factorial


if __name__ == "__main__":
    num = 5
    try:
        result = calculate_factorial(num)
        print(f"Факториал числа {num}: {result}")

    except ValueError as e:
        print(f"Ошибка: {e}")