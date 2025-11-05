def is_prime(number: int) -> bool:
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    for divisor in range(3, int(number**0.5) + 1, 2):
        if number % divisor == 0:
            return False

    return True


def find_primes_up_to(limit: int) -> list[int]:
    return [num for num in range(2, limit + 1) if is_prime(num)]


if __name__ == "__main__":
    limit_number = 100
    primes_list = find_primes_up_to(limit_number)
    print(f"Список простых чисел до {limit_number}:")
    print(primes_list)