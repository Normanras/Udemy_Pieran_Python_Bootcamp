def func_one(n):
    return(str(num) for num in range(n))

func_one(10)

def func_two(n):
    return list(map(str,range(n)))

func_two(10)

import time
# Run current time before the code
start_time = time.time()

# then run the code
result = func_one(100000)
# Then run current time after the code
end_time = time.time()
# Elapsed Time
elapsed_time = end_time - start_time

print(elapsed_time)


#Compare this to func_two

import time
# Run current time before the code
start_time = time.time()

# then run the code
result = func_two(100000)
# Then run current time after the code
end_time = time.time()
# Elapsed Time
elapsed_time = end_time - start_time

print(elapsed_time)

#This usage becomes hard to measure efficiently and super acurately. 
# better to use the timeit module

import timeit
timeit.timeit
stmt = '''
func_one(100)
'''

setup='''
def func_one(n):
    return(str(num) for num in range(n))e
'''

timeit.timeit(stmt,setup,number=100000)

stmt2 = '''
func_two(100)
'''

setup2 = '''
def func_two(n):
    return list(map(str,range(n)))

'''

timeit.timeit(stmt,setup,number=100000)
#this should show func2 running faster

%%timeit
func_one(100)

%%timeit
func_two(100)
