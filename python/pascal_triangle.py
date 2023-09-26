# Напишите программу, которая запрашивает у пользователя число n,
# а затем выводит n первых строк треугольника Паскаля. Обеспечьте
# отказоустойчивость при введении пользователем не валидного значения
# n (т.е. не целого положительного числа)

def n_line(n: int) -> []:
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    else:
        parent_line = n_line(n - 1)
        result = [1]

        for i in range(0, len(parent_line) - 1):
            result.append(parent_line[i] + parent_line[i + 1])

        result.append(1)

        return result


def input_count() -> int:
    n = None

    while n is None:
        try:
            print("Введите положительное число: ")
            n = int(input())

            if n <= 0:
                n = None
                raise ValueError

        except ValueError:
            print("Неверный формат ввода.")

    return n


if __name__ == '__main__':
    for i in range(0, input_count()):
        print(n_line(i + 1))
