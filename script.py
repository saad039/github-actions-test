# Learning and experimenting with decorators


import pandas
import numpy
import sys
import regex
import functools


def plus_one(function):
    # print('decorator invoked')
    def add_one():
        return function() + 1

    return add_one


@plus_one
def foo():
    # print('foo invoked')
    return 9


# Create a function producing a string. It's result get consumed by two
# decorators that first Title case
# it and later split it

def to_title_case(func):
    def convert():
        return func().title()
    return convert


def perform_split(func):
    def split():
        return func().split(' ')
    return split


@perform_split
@to_title_case
def producer():
    return 'hello world from saad who wants to become a top hacker'


# Receving arguments inside decorators

def decorator_logger(func):
    def logger(arg1: str, arg2: str):
        print(f'Args received: {arg1} and {arg2}')
        return func(arg1, arg2)
    return logger


def power_logger(func):
    def logger(*args, **kwargs):
        print(f'the positional arguments received are: {args}')
        print(f'the keywork arguments received are: {kwargs}')
        return func(*args, **kwargs)
    return logger


@power_logger
def concat(arg1: str, arg2: str):
    return arg1 + arg2


print(foo())
print(producer())


result = concat('saad is', ' good boy')


@power_logger
def foo(name, age):
    return 'nothing'


print(f'result: {result}')
print(foo(name='saad', age=20))


# Creating a decorator which accepts arguments

def decorator_with_args(name: str, age: str):
    def decorator(func):
        @functools.wraps(func)
        def logger_l(farg1, farg2):
            """Hello from logger_l"""
            print(f'Decorator args received: {name} and {age}')
            print(
                f'Function arguments received Function arguments received Function arguments received Function arguments received Function arguments received: {farg1} and {farg2}')
            return func(farg1, farg2)
        return logger_l
    return decorator


@decorator_with_args('saad', '21')
def foo(name, age):
    """foo does something"""
    return 'nothing'


print(foo('valentine', 'Saint Denis'))


print(f'The name of function is: {foo.__name__}')
print(f'The doc of function is: {foo.__doc__}')


# Debugging decorators


def closure():
    count = 0

    def aux():
        nonlocal count
        count += 1
        # print(count)
        return count

    return aux


cc = closure()


for i in range(10):
    print(cc())

import numpy, pandas, bs4, requests 
import numpy, pandas, bs4, requests 
import numpy, pandas, bs4, requests 
import numpy, pandas, bs4, requests 