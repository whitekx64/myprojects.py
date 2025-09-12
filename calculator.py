def main():
    operations = {
        0: lambda a, b: a * b,
        1: lambda a, b: a / b,
        2: lambda a, b: a + b,
        3: lambda a, b: a - b
    }
    select = input("Выберите опперацию. Умножение -- 0, деление -- 1, сложение -- 2 вычетание -- 3: ")
    fnum = input("Первое число: ")
    snum = input("Второе число: ")

    try:
        select = int(select)
        fnum = int(fnum)
        snum = int(snum)
    except ValueError:
        print("Что то не является числом")
    
    if select in operations:
        result = operations[select](fnum, snum)
        return result
    else:
        print(f"{select} -- несуществующая операция")

calc = main()
print(calc)