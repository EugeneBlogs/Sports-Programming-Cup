# Последовательность Фибоначчи
fib = [1, 2]
while True:
    next = fib[-1] + fib[-2]
    if next > 2 ** 61:
        break
    fib.append(next)

fib_digit_sums = [sum(int(n) for n in str(el)) for el in fib]  # Суммы цифр в последовательности

first_sum = int(input())
candidates = [i for i in range(len(fib)) if fib_digit_sums[i] == first_sum]  # Индексы с такой суммой цифр
last_idx = len(fib) - 1

# Выбор кнопки
if all(i < last_idx for i in candidates):
    # Есть все кандидаты не последние, то можем нажимать "+"
    print("+")
    next_sum = int(input())
    for i in candidates:
        if i + 1 < len(fib) and fib_digit_sums[i + 1] == next_sum:
            x = i
            break
else:
    print("-")
    prev_sum = int(input())
    for i in candidates:
        if i - 1 >= 0 and fib_digit_sums[i - 1] == prev_sum:
            x = i
            break

print(fib[x])