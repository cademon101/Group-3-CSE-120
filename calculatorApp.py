# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 16:50:00 2023

@author: Sishir
"""
from matplotlib import pyplot as plt

class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            return "Division by zero is not allowed."
        return x / y

    def calculate_derivative(self, expression):
        terms = expression.split('+')
        derivative_terms = []

        for term in terms:
            coefficient, exponent = term.split('x^')
            coefficient = int(coefficient)
            exponent = int(exponent)
            if exponent == 0:
                derivative_term = "0"
            else:
                derivative_coefficient = coefficient * exponent
                derivative_exponent = exponent - 1
                derivative_term = f"{derivative_coefficient}x^{derivative_exponent}"

            derivative_terms.append(derivative_term)

        derivative = "+".join(derivative_terms)

        return derivative

    def fibonacci(self, n):
        fib_sequence = []
        a, b = 0, 1

        for _ in range(n):
            fib_sequence.append(a)
            a, b = b, a + b

        return fib_sequence
    
    def plot_graph(self, x, y):
        plt.plot(x, y)
        plt.show()
    
    def print_menu(self):
        print("\nOptions:")
        print("Enter 'add' for addition")
        print("Enter 'subtract' for subtraction")
        print("Enter 'multiply' for multiplication")
        print("Enter 'divide' for division")
        print("Enter 'derivative' for derivative")
        print("Enter 'fib' for Fibonacci sequence")
        print("Enter 'graph' for graphing")
        print("Enter 'quit' to end the program")




def main():
    calculator = Calculator()
    while True:
        calculator.print_menu();
        user_input = input(": ")
    
        if user_input == "quit":
            break
    
        if user_input in ("add", "subtract", "multiply", "divide"):
            num1 = float(input("\nEnter first number: "))
            num2 = float(input("Enter second number: "))
    
            if user_input == "add":
                print("Result: ", calculator.add(num1, num2))
            elif user_input == "subtract":
                print("Result: ", calculator.subtract(num1, num2))
            elif user_input == "multiply":
                print("Result: ", calculator.multiply(num1, num2))
            elif user_input == "divide":
                print("Result: ", calculator.divide(num1, num2))
                
        elif user_input in ("derivative"):
            expression = input("\nEnter your expression. Example: 2x^2: ")
            print("Result: ", calculator.calculate_derivative(expression))
            
        elif user_input in ("fibonacci"):
            n = int(input("\nEnter the number of Fibonacci numbers: "))
            print("Fibonacci sequence:", calculator.fibonacci(n))

        elif user_input in ("graph"):
            user_x = input("\nEnter x values. Seperate by spaces(1 23 4 33 2): ")
            x_list_string = user_x.split()
            x_list = [int(x) for x in x_list_string]
            user_y = input("\nEnter y values. Seperate by spaces(1 23 4 33 2): ")
            y_list_string = user_y.split()
            y_list = [int(x) for x in y_list_string]
            calculator.plot_graph(x_list, y_list)

        else:
            print("Invalid input")
            
main()