def generate_fibonacci(n: int) -> list[int]:
    if n <= 0:
        raise ValueError("Последовательность Фибоначчи не может быть меньше 1")
    elif n == 1:
        return [0]

    fib_list = [0, 1]

    for i in range(2, n):
        next_fib = fib_list[i - 1] + fib_list[i - 2]
        fib_list.append(next_fib)

    return fib_list


if __name__ == "__main__":
    try:
        count_n = 10
        fib_sequence = generate_fibonacci(count_n)
        print(f"Первые {count_n} чисел Фибоначчи: {fib_sequence}")
    except ValueError as e:
        print(f"Ошибка: {e}")