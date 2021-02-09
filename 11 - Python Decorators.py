
# Decorators allow you to add functionality to exisitng 
# functions. You can turn it on and off. 

@some_decorator
def simple_func():
    # Do simple stuff
    # Return something 

# Building out a decorator while reviewing some information

def func():
    return 1

def hello():
    return "Hello!"

greet = hello

del hello

hello() <- it is now not defined
but if we call "greet" it will still return hello

def hello(name='Norm'):
    print('The hello() function has been executed')
    
    def greet():
        return'\t This is the greet() function inside hello!'
    
    def welcome():
        return '\t This is the welcome() function inside hello'

    print(greet())
    print(welcome())
    print('This is the end of the hello function!')



def hello(name='Norm'):
    print('The hello() function has been executed')
    
    def greet():
        return'\t This is the greet() function inside hello!'
    
    def welcome():
        return '\t This is the welcome() function inside hello'

    print("I am going to return a function!")

    if name == 'Norm':
        return greet
    else:
        return welcome

my_new_func = hello('Jose')

print(my_new_func() )

def cool():

    def super_cool():
        return 'I am very cool!'

    return super_cool

some_func = cool()

some_func

some_func()


def hello():
    return 'Hi Jose!'

def other(some_def_func):
    print('Other Code runs here!')
    print(some_def_func())

other(hello)


def new_decorator(original_func):

    def wrap_func():

        print('Some extra code, before the original function')

        original_func()

        print('Some extra code, after the original function')

    return wrap_func

def func_needs_decorator():
    print("I want to be decorated!")

decorated_func = new_decorator(func_needs_decorator)


@new_decorator
def func_needs_decorator():
    print("I want to be decorated!")

func_needs_decorator()