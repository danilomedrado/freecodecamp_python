#learn-the-bisection-method-by-finding-the-square-root-of-a-numbe
#https://github.com/freeCodeCamp/freeCodeCamp/tree/main/curriculum/challenges/english/07-scientific-computing-with-python/learn-the-bisection-method-by-finding-the-square-root-of-a-number
#In this project, you will find the approximate square root of a given number using the bisection method.
#The bisection method is a technique for finding the roots of a real-valued function. 
#It works by narrowing down an interval where the square root lies until it converges to a value within a specified tolerance.

def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    if square_target < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    if square_target == 1:
        root = 1
        print(f'The square root of {square_target} is 1')
    elif square_target == 0:
        root = 0
        print(f'The square root of {square_target} is 0')
    else:
        low = 0
        high = max(1, square_target)
        root = None
        
        for _ in range(max_iterations):
            mid = (low + high) / 2
            square_mid = mid**2

            #print('low', low, 'high', high, 'mid', mid, 'root', root, 'square_mid', square_mid)

            if abs(square_mid - square_target) < tolerance:
                root = mid
                break
            elif square_mid < square_target:
                low = mid
            else:
                high = mid

        if root is None:
            print(f"Failed to converge within {max_iterations} iterations.")
    
        else:   
            print(f'The square root of {square_target} is approximately {root}')
    
    return root

valor = float(input('digite um numero:'))
print('raiz', square_root_bisection(valor))