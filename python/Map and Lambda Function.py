# https://www.hackerrank.com/challenges/map-and-lambda-expression/problem
# Apparently, I do not know the Fibonacci sequence as well as I thought.

cube = lambda x: x**3 

def fibonacci(n):
    fib_list = [0, 1]

    for i in range(2, n):
        a = fib_list[i-1]
        b = fib_list[i-2]

        fib_list.append(a+b)
   
    return(fib_list[0:n])


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))