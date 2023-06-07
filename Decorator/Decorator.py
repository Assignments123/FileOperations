import time
import math
import logging


def log_decorator(func):

    # open a logfile if not present then create new.
    # set logfile's level as info and format how data must be stored in it.
    logging.basicConfig(filename="logfile.log",level=logging.INFO,format =
                        '%(asctime)s , %(levelname)s , %(message)s')

    # create a wrapper function which will actually hold the information 
    # of decorated/wrapped function
    def wrapper_function(*args,**kwargs):

        # perform the actions which you want to perform before the 
        # decorated/wrapped function is executed
        print("inside handler function")

        # calling the wrapped / decorated function inside decorator
        result = func(*args,**kwargs)

        # perform actions which you decorator is supposed to do on 
        # result of wrapped function
        # store name of wrapped function in a variable
        FunctionName = func.__name__
        # returns tuple of values
        # Arguments = args
        # to access first element from tuple of arguments
        Arguments = args[0]
        # store result into a variable
        Return_value = result
        # storing the response to logfile
        logging.info('Function name : %s, Passed Arguments : %s,\
                     Returned values : %s',FunctionName,
                     Arguments,Return_value)

        print(FunctionName,Arguments,Return_value)
    # return the actual output or return value of function 
    # which was passed to decorator as an argument
    return wrapper_function


# decorator to measure execution time
def timing_decorator(func):
     
    # given pointer to arguments which will be passed during function call
    def wrapper_function(*args,**kwargs):
 
        time.sleep(2)
        # Start time of function
        starttime = time.time()
        print(starttime)
        time.sleep(2)
        
        # calling the wrapped function / decorated function inside decorator
        result = func(*args,**kwargs)

        # End time of function
        endtime = time.time()
        print(endtime)
        print("Total time taken is : ", func.__name__, endtime - starttime )
        wrapper_function.__name__ = func.__name__
        return result

    # return wrapper_function which is nothing but decorated calculate_factorial function
    return wrapper_function


@log_decorator
@timing_decorator
# calculate_factorial function will be executed in timing_decorator first, 
# whatever this function return in timing_decorator will be decorated,
# and will be returned to log_decorator as response of calculate_factorial function
# calculate_factorial func will not be directly executed in log_decorator.

# function which is passed to a decorator as an argument is called as 
# wrapped function or decorated function
def calculate_factorial(num):
    
    try:
        factorial = math.factorial(num)
        return factorial
    except ValueError:
        print("Please provide positive integer values only")
    except TypeError:
        print("Please provide positive integer values only")

if __name__ == "__main__":

    # call function
    calculate_factorial(3)