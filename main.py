print("Длмашнее задание")


def decorator(func):
    import time

    def wrapper(*args):
        start_time = time.time()
        func(*args)
        end_time = time.time()
        print(f'Время выполнения функции составило {end_time-start_time} секунд')
    return wrapper


@decorator
def create_list(a: int, b: int) -> list:
    pl = [i for i in range(a, b+1)]
    return pl


start = int(input("Введите начальную границу диапазона:\n"))
end = int(input("Введите конечную границу диапазона:\n"))
create_list(start, end)


print("Бонус! Нахождение минимального и максимального значения\n"
      " без использования функций 'min()' и 'max()'\n"
      " с любым количеством вложенных списков")
plist = []


def find_min(nums: list) -> int:
    print("Data after sorting:\n", sorted(nums))
    nums = sorted(nums)
    num = nums[0]
    return num


def find_max(nums: list) -> int:
    print("Data after sorting:\n", sorted(nums))
    nums = sorted(nums, reverse=True)
    num = nums[0]
    return num


def list_creating(*nums):
    print("Data before sorting (You can input your own data in function calling string):\n", nums)
    for i in nums:
        if type(i) == int:
            plist.append(i)
        elif type(i) == list:
            list_unpacking(i)
    while True:
        choose = str(input("To view min value input 'min'\n"
                           "To view max value input 'max'\n"
                           "To exit input 'exit'\n"))
        if choose.upper() == "EXIT":
            print("Bye")
            break
        elif choose.upper() == "MIN":
            print(find_min(plist))
        elif choose.upper() == "MAX":
            print(find_max(plist))
        else:
            print("You've choosed a wrong option, please try again!")


def list_unpacking(args):
    for i in args:
        if type(i) == int:
            plist.append(i)
        elif type(i) == list:
            list_unpacking(i)


list_creating([2, 4, [2, 5, 7, [10, [20, [-22, 28, [34, [-3456, 345,
            [5068, [4965]]]]]], 17, [20, 19, [100, 219], -23]]], 7,
            9, [2, 6, 8]], 20, 100, [-1000, 22, [20000, 2354]])