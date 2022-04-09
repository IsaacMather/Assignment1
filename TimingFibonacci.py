#write three functions in one Python module.

#first, fibonacci_direct(n). This function should use a loop to fund and return the nth Fibonacci number. If you
# code this right, you should find that it works very quickly and can calculate the 1000th Fibonacci number in the blink
#of an eye.

def fibonacci_direct(n):
    pass


# Next, fibonacci_recursive(n). This function should call tiself recursively and find the nth Fibonacci number. In other
#words, if you call fibonacci_recursive(n) it should return fibonacci_recursive(n-1) + fibonacci_recursive(n-2). If you
#code this right, you should find that you can quickly get a value for fibonacci_recursive(10) but not for
# fibonacci)_recursive(50).

def fibonacci_recursive(n):
    pass

#Finally, fibonacci_memo(n). This is identical to the fibonacci_recursive() function, but it should be wrapped in an
# @lru_cache decorator, and the calls inside should be to fibonacci_memo(). You should find that fibonacci_memo(50) runs
#very quickly.

@functools.lru_cache()
def fibonacci_memo(n):
    pass


#Analysis
#In a document, include the following analysis:

# First, what is the emperical complexity of each of your three algorithms. That is, create a timer and run each function
#several times with a value of n, then double n and do it again, etc..

#Going through this several times for each n will even out external effects. Show your average results in both a graph and
#a table.

#I suggest using a table like the one below, and focusing on the factor increase in time for each doubling on n... what does
#it tell you?


#... to be continued