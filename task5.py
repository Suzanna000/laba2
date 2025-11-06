def is_prime(number: int) -> bool:
    if number < 2:
        return False
    
    for i in range(2, number):
        if number % i == 0:
            return False

    return True


def find_primes_up_to(n: int) -> list[int]:
    prime_numbers = []

    for i in range(1, n + 1):
        if is_prime(i):
            prime_numbers.append(i)
    
    return prime_numbers


if __name__ == "__main__":
    number_n = 100
    primes_list = find_primes_up_to(number_n)
    print(f"Список простых чисел до {number_n}:")
    print(primes_list)