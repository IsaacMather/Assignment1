from TimingFibonacci import fibonacci_direct, fibonacci_recursive, fibonacci_memo
import timeit
import sys
import matplotlib.pyplot as plt
import functools
sys.setrecursionlimit(100000)

def fibonacci_direct(n):
    count = 0
    lower_number = 0
    higher_number = 1
    temp = 0

    if n == 0:
        return 0
    elif n == 1:
        return 1


    else:
        while count < n:
            # print(lower_number)
            temp = lower_number + higher_number
            lower_number = higher_number
            higher_number = temp
            count += 1

    return lower_number


def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


def fib_memo_caller(n):
    fibonacci_memo.cache_clear()
    fibonacci_memo(n)

@functools.lru_cache()
def fibonacci_memo(n):
    if n <= 1:
        return n
    else:
        return fibonacci_memo(n-1) + fibonacci_memo(n-2)


def graph_maker(x_axis, y_axis, title):
    fix, ax = plt.subplots()
    ax.plot(x_axis, y_axis)
    ax.set_xlabel("Size")
    ax.set_ylabel("Average Time")
    ax.set_title(f"Complexity of {title}")
    ax.legend()
    plt.show()

def my_range(start, stop):
    i = start
    while i <= stop:
        yield i
        i += i

def super_timer(sizes: int, function_to_call):
    size_list = []
    average_time_list = []

    runs = 5
    print({function_to_call})
    print("Size     Average Time")
    print("---------------------")
    for size in my_range(5, sizes):
        #should i reset the cache here?

        total_time = timeit.timeit(
                                   f"{function_to_call}({size})",
                                   setup=f"from __main__ import {function_to_call}",
                                   number=runs)
        average_time = total_time / runs
        print(f"{size:<2}        {average_time:<20.10f}")

        size_list.append(size)
        average_time_list.append(average_time)

    return size_list, average_time_list


if __name__ == '__main__':
    dir_size_list, dir_time_list = super_timer(1000000, 'fibonacci_direct')
    recur_size_list, recur_time_list = super_timer(40, 'fibonacci_recursive')
    memo_size_list, memo_time_list = super_timer(11000, 'fib_memo_caller')

    graph_maker(dir_size_list, dir_time_list, 'fibonacci_direct')
    graph_maker(recur_size_list, recur_time_list, 'fibonacci_recursive')
    graph_maker(memo_size_list, memo_time_list, 'fibonacci_memo')

#
# #/Users/isaacmather/PycharmProjects/Assignment1/venv/bin/python /Users/isaacmather/PycharmProjects/Assignment1/main.py
# {'fibonacci_direct'}
# Size     Average Time
# ---------------------
# 5         0.0000009486
# 10        0.0000010340
# 20        0.0000018714
# 40        0.0000035356
# 80        0.0000115860
# 160        0.0000333414
# 320        0.0000475246
# 640        0.0001124588
# 1280        0.0002483400
# 2560        0.0003581610
# 5120        0.0008619278
# 10240        0.0034258786
# 20480        0.0092464182
# 40960        0.0257886840
# 81920        0.0992320660
# 163840        0.3351890942
# 327680        1.2552827814
# 655360        5.0992263736
# {'fibonacci_recursive'}
# Size     Average Time
# ---------------------
# 5         0.0000025678
# 10        0.0000237118
# 20        0.0026972596
# 40        40.5266326946
# {'fib_memo_caller'}
# Size     Average Time
# ---------------------
# 5         0.0000032634
# 10        0.0000050674
# 20        0.0000097970
# 40        0.0000193886
# 80        0.0000371864
# 160        0.0000780456
# 320        0.0001637926
# 640        0.0003546272
# 1280        0.0007634582
# 2560        0.0016263462
# 5120        0.0039538970
# 10240        0.0097502078
# No artists with labels found to put in legend.  Note that artists whose label start with an underscore are ignored when legend() is called with no argument.
# No artists with labels found to put in legend.  Note that artists whose label start with an underscore are ignored when legend() is called with no argument.
# No artists with labels found to put in legend.  Note that artists whose label start with an underscore are ignored when legend() is called with no argument.
#
# Process finished with exit code 0