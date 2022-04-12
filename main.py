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
        fibonacci_memo.cache_clear()
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
    memo_size_list, memo_time_list = super_timer(11000, 'fibonacci_memo')

    graph_maker(dir_size_list, dir_time_list, 'fibonacci_direct')
    graph_maker(recur_size_list, recur_time_list, 'fibonacci_recursive')
    graph_maker(memo_size_list, memo_time_list, 'fibonacci_memo')



#output
# {'fibonacci_direct'}
# Size     Average Time
# ---------------------
# Size       Average Time
# 5         0.0000009652
# 10         0.0000010484
# 20         0.0000019144
# 40         0.0000036202
# 80         0.0000073354
# 160         0.0000151100
# 320         0.0000393576
# 640         0.0001155316
# 1280         0.0004850168
# 2560         0.0005233208
# 5120         0.0010921882
# 10240         0.0038937558
# 20480         0.0086921520
# 40960         0.0259926444
# 81920         0.0899243990
# 163840         0.3292538178
# 327680         1.2725213328
# 655360         5.0695950332
# {'fibonacci_recursive'}
# Size     Average Time
# ---------------------
# 5         0.0000025132
# 10         0.0000236836
# 20         0.0026550916
# 40         42.0832498160
# {'fibonacci_memo'}
# Size     Average Time
# ---------------------
# 5         0.0000010760
# 10        0.0000014248
# 20        0.0000024240
# 40        0.0000046146
# 80        0.0000090918
# 160        0.0000228566
# 320        0.0000496248
# 640        0.0001034370
# 1280        0.0002051328
# 2560        0.0004361558
# 5120        0.0009554204
# 10240        0.0022977032

