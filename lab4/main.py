import math

WORDS = [
    "ЯК", "ПОДІЛИШ", "РАДІСТЬ", "СТАНЕ",
    "ПОДВІЙНОЮ", "А", "ГОРЕ", "ВПОЛОВИНУ", "МЕНШИМ"
]

LETTER_POSITIONS = {
    'А': 1,  'Б': 2,  'В': 3,  'Г': 4,  'Ґ': 5,  'Д': 6,
    'Е': 7,  'Є': 8,  'Ж': 9,  'З': 10, 'И': 11, 'І': 12,
    'Ї': 13, 'Й': 14, 'К': 15, 'Л': 16, 'М': 17, 'Н': 18,
    'О': 19, 'П': 20, 'Р': 21, 'С': 22, 'Т': 23, 'У': 24,
    'Ф': 25, 'Х': 26, 'Ц': 27, 'Ч': 28, 'Ш': 29, 'Щ': 30,
    'Ь': 31, 'Ю': 32, 'Я': 33
}

def get_word_sum(word: str) -> int:
    return sum(LETTER_POSITIONS.get(char.upper(), 0) for char in word)

def hash_division(key: str, m: int = 13) -> int:
    return get_word_sum(key) % m

A_CONST = (math.sqrt(5) - 1) / 2

def hash_multiplication(key: str, m: int = 16) -> int:
    k = get_word_sum(key)
    fraction = (k * A_CONST) % 1
    return math.floor(m * fraction)

def build_open_hash_table(words: list, m: int, hash_func) -> list:
    table = [[] for _ in range(m)]
    for word in words:
        address = hash_func(word, m)
        table[address].append(word)
    return table

def build_closed_hash_table(words: list, m: int, hash_func) -> list:
    table = [None] * m
    for word in words:
        start_address = hash_func(word, m)
        for i in range(m):
            address = (start_address + i) % m
            if table[address] is None:
                table[address] = word
                break
    return table

def analyze_search_stats(words: list, m: int, hash_func, mode="open"):
    comparisons = {}
    if mode == "open":
        table = build_open_hash_table(words, m, hash_func)
        for word in words:
            address = hash_func(word, m)
            chain = table[address]
            comparisons[word] = chain.index(word) + 1
    else:
        table = build_closed_hash_table(words, m, hash_func)
        for word in words:
            start_address = hash_func(word, m)
            count = 0
            for i in range(m):
                count += 1
                address = (start_address + i) % m
                if table[address] == word:
                    comparisons[word] = count
                    break
    max_word = max(comparisons, key=comparisons.get)
    avg_cmp = sum(comparisons.values()) / len(comparisons)
    return comparisons, max_word, comparisons[max_word], avg_cmp

if __name__ == "__main__":
    print("1. РОЗРАХУНОК ХЕШ-АДРЕС ДЛЯ СЛІВ")
    for w in WORDS:
        k = get_word_sum(w)
        print(f"{w:10} | K={k:3d} | h_div(m=13)={hash_division(w, 13):02d} | h_mul(m=16)={hash_multiplication(w, 16):02d}")

    print("\n 2. ВІДКРИТА ХЕШ-ТАБЛИЦЯ (МЕТОД ЛАНЦЮЖКІВ, M=13) ")
    open_div = build_open_hash_table(WORDS, 13, hash_division)
    for i, chain in enumerate(open_div):
        print(f"Індекс [{i:02d}]: {chain}")

    print("\n3. ЗАКРИТА ХЕШ-ТАБЛИЦЯ (ВІДКРИТА АДРЕСАЦІЯ, M=13) ")
    closed_div = build_closed_hash_table(WORDS, 13, hash_division)
    for i, val in enumerate(closed_div):
        print(f"Індекс [{i:02d}]: {val if val is not None else '(NULL)'}")

    print("\n 4. СТАТИСТИКА ПОРІВНЯНЬ ПРИ ПОШУКУ ")
    _, max_w_op, max_c_op, avg_op = analyze_search_stats(WORDS, 13, hash_division, "open")
    print(f"Відкрита таблиця: Макс. порівнянь = {max_c_op} ('{max_w_op}'), Середня кількість = {avg_op:.2f}")

    _, max_w_cl, max_c_cl, avg_cl = analyze_search_stats(WORDS, 13, hash_division, "closed")
    print(f"Закрита таблиця:  Макс. порівнянь = {max_c_cl} ('{max_w_cl}'), Середня кількість = {avg_cl:.2f}")
