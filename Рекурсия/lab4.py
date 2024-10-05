# Требуется запрограммировать рекурсивный алгоритм,
# который вычисляет
# 1) n-й член геометрической прогрессии;
# 2) сумму n членов геометрической прогрессии;
# 3) n-й член арифметической прогрессии;
# 4) двоичное представление десятичного числа;
# 5) наименьшее общее кратное двух натуральных чисел.


def input_int(text):
    while True:
        try:
            value = int(input(text))
            if value <= 0:
                raise ValueError("Число должно быть положительным.")
            return value
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите число.")


# 1) n-й член геометрической прогрессии
def gp_n(a0, r, n):
    if n == 0:
        return a0
    return gp_n(a0, r, n - 1) * r


# 2) Сумма n членов геометрической прогрессии
def gp_sum(a0, r, n):
    if n == 0:
        return a0
    return gp_sum(a0, r, n - 1) + a0 * (r ** n)


# 3) n-й член арифметической прогрессии
def ap_n(a0, d, n):
    if n == 0:
        return a0
    return ap_n(a0, d, n - 1) + d


# 4) Двоичное представление десятичного числа
def dec_bin(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return dec_bin(n // 2) + str(n % 2)


# 5) Наименьшее общее кратное (НОК) двух натуральных чисел
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def main():
    print("Геометрическая прогрессия")
    el = input_int("Введите нулевой элемент (a0): ")
    denominator = input_int("Введите знаменатель (r): ")
    num = input_int("Введите номер члена (n): ")
    print(f"\nn-й член геометрической прогрессии: {gp_n(el, denominator, num)}")
    print(f"Сумма n членов геометрической прогрессии: {gp_sum(el, denominator, num)}")
    print("\nАрифметическая прогрессия")

    el = input_int("Введите нулевой элемент (a0): ")
    diff = input_int("Введите разность (d): ")
    num = input_int("Введите номер члена (n): ")

    print(f"\nn-й член арифметической прогрессии: {ap_n(el, diff, num)}")

    print("\nДвоичное представление:")
    decimal_number = input_int("Введите десятичное число: ")
    binary_representation = dec_bin(decimal_number)

    print(f"Двоичное представление числа {decimal_number}: {binary_representation}")

    print("\nНаименьшее общее кратное:")

    num1 = input_int("Введите первое натуральное число: ")
    num2 = input_int("Введите второе натуральное число: ")

    print(f"Наименьшее общее кратное {num1} и {num2}: {lcm(num1, num2)}")
    return 0

if __name__ == '__main__':
    main()