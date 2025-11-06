import string


def count_word_frequency(filepath: str) -> dict[str, int]:
    word_counts = {}
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            text = file.read()

        text = text.lower()

        for p in string.punctuation:
            text = text.replace(p, "")

        words = text.split()

        for word in words:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1

    except FileNotFoundError:
        print(f"Ошибка: Файл не найден по пути {filepath}")
        return {}

    return word_counts


if __name__ == "__main__":
    file_path = "task17_file.txt"
    frequency = count_word_frequency(file_path)

    if frequency:
        print(f"Частота слов в файле '{file_path}':")
        for word, count in frequency.items():
            print(f"  {word}: {count}")