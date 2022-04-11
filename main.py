from TimingFibonacci import fibonacci_direct, fibonacci_recursive, fibonacci_memo
import timeit
from GraphMaker import graph_maker

def my_range(start, stop):
    i = start
    while i <= stop:
        yield i
        i += i

def super_timer(size: int, function_to_call):
    #need to get this set up so it doubles the size of the fibonacci number
    # we're searching for each time

    size_list = []
    average_time_list = []

    sizes = [5, 10, 20, 40, 80]
    # sizes = [5, 10, 20]

    runs = 5
    print({function_to_call})
    print("Size     Average Time")
    print("---------------------")
    for size in sizes:
        total_time = timeit.timeit(
                                   f"{function_to_call}({size})",
                                   setup=f"from __main__ import {function_to_call}",
                                   number=runs)
        average_time = total_time / runs
        print(f"{size:<2}        {average_time:<20.10f}")

        size_list.append(size)
        average_time_list.append(average_time)

    return size_list, average_time_list
    # graph_maker(size_list, average_time_list, function_to_call)



    ##from here, once it's finished running i want to graph out the growth
    # in time spend




if __name__ == '__main__':
    # print(fibonacci_direct(10))
    # print(fibonacci_recursive(40))
    # print(fibonacci_memo(10))
    dir_size_list, dir_time_list = super_timer(100, 'fibonacci_direct')
    recur_size_list, recur_time_list = super_timer(100, 'fibonacci_recursive')
    memo_size_list, memo_time_list = super_timer(100, 'fibonacci_memo')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
