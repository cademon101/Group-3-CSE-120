import math
import re
import numpy as np
from matplotlib import pyplot as plt 
from fractions import Fraction
import os

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
    
    def graphFibonacci(self, n):
        fib_sequence = self.fibonacci(n)
        num_points = len(fib_sequence)

        # Calculate polar coordinates
        theta = np.linspace(0, 2 * math.pi, num_points, endpoint=False)
        radius = fib_sequence
           
        # Plot the polar chart
        fig, ax = plt.subplots(subplot_kw={'projection': 'polar'}, figsize=(8, 8))
        ax.plot(theta, radius, marker='o', linestyle='-', color='b')
        ax.set_title(f"Fibonacci Sequence in Polar Coordinates up to {n}")
        plt.show()    
        
    def plot_graph(self, x, y, title="Chart", show_grid_lines=False, x_label="x", y_label="y"):
        plt.plot(x, y)
        plt.title(f"Plot of {title}")
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.grid(show_grid_lines)
        plt.show()
          
    def is_number_prime(self, n):
        if n <= 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    
    def generate_primes(self, n):
        primes = []
        for num in range(2, n + 1):
            if self.is_number_prime(num):
                primes.append(num)
        return primes
        
    def make_prime_graph(self, num):
        y_list = self.generate_primes(num)
        x_list = [int(x) for x in range(1, len(y_list)+1)]
        self.plot_graph(x_list, y_list, f"Prime numbers up to {num}", True)
        
    def plot_equation(self, equation, x_range=(-10, 10), num_points=100, show_grid_lines=False):
        x_values = []
        y_values = []
    
        for i in range(num_points):
            x = x_range[0] + i * (x_range[1] - x_range[0]) / (num_points - 1)
            x_values.append(x)
    
            try:
                y = eval(equation.replace('^', '**').replace('x', str(x)))
                y_values.append(y)
            except Exception as e:
                print(e)
                pass
            
        self.plot_graph(x_values, y_values, f"{equation}", show_grid_lines)
        
    def fraction_to_decimal(self, numerator, denominator):
        result = numerator / denominator
        print(f"The decimal representation of {numerator}/{denominator} is: {result}")
        return float(result)
    
    def square_root(self, x):
        return math.sqrt(x)

    def decimal_to_fraction(self, decimal):
        fraction = Fraction(decimal).limit_denominator()
        print(f"The fraction representation of {decimal} is: {fraction.numerator}/{fraction.denominator}")
        return float(fraction.numerator/ fraction.denominator)
      
    def factorial(self, x):
        return math.factorial(x)
      
    def simplify_fraction(self, numerator, denominator):
        gcd = math.gcd(numerator, denominator)
        return numerator // gcd, denominator // gcd

    def log(self, x, y):
      if y == 0:
        return math.log(x)
      return math.log(x, y)

    def print_menu(self):
            print("\nOptions:")
            print("To add'+', subtract'-', multiply'*', divide'/': type your two numbers with an operator split by spaces EX: (38 / 2)")
            print("To continue calculation with past result(non graphing function) use an operator followed by number EX:+ 4")
            print("Enter 'derivative' for derivative")
            print("Enter 'fib' for Fibonacci sequence")
            print("Enter 'graphFib' for Fibonacci sequence")
            print("Enter 'graph' for graphing")
            print("Enter 'equationGraph' to see a graph for an equation")
            print("Enter 'prime' for prime factors")
            print("Enter 'primeGraph' for a graph of prime numbers")
            print("Enter 'f to d' to convert a fraction into a decimal")
            print("Enter 'd to f' to convert a decimal into a fraction")
            print("Enter 'square' for square root")
            print("Enter 'fact' for factorial")
            print("Enter 'simplify' to simplify a fraction")
            print("Enter 'log' for logarithmic functions")
            print("Enter 'complex' for complex basic arithmatic EX: (5+5)5c")
            print("Enter 'c' to clear past result")
            print("Enter 'cc' to clear whole terminal")
            print("Enter 'quit' to end the program")
    
    def calculate_complex_expression(self, user_input):
        #user_input = input("Please enter the expression to calculate: ")
        user_input = user_input.replace('^', '**')  
        user_input = re.sub(r'(\d)\s*\(', r'\1*(', user_input)
        try:
            result = eval(user_input)
            return result
        except Exception as e:
            print(":", e)
            return None

    def quick_calc(self, input_parts, result):

        #calculations with past result
        if (len(input_parts) == 2):
            num1 = float(result)
            operator = input_parts[0]
            num2 = float(input_parts[1])
            if operator == '+':
                return Calculator().add(num1, num2)
            elif operator == '-':
                return Calculator().subtract(num1, num2)
            elif operator == '*':
                return Calculator().multiply(num1, num2)
            elif operator == '/':
                return Calculator().divide(num1, num2)
            else:
                print("Invalid operator. Please use '+', '-', '*', or '/'.")

        #basic calculations
        if (len(input_parts) == 3):
            num1 = float(input_parts[0])
            operator = input_parts[1]
            num2 = float(input_parts[2])
            if operator == '+':
                return Calculator().add(num1, num2)
            elif operator == '-':
                return Calculator().subtract(num1, num2)
            elif operator == '*':
                return Calculator().multiply(num1, num2)
            elif operator == '/':
                return Calculator().divide(num1, num2)
            else:
                print("Invalid operator. Please use '+', '-', '*', or '/'.")
                ##place cal code here 

def calculatorSimulator():
    
    
    calculator = Calculator()
    calculator.print_menu()
    result = 0
    while True:

        user_input = input(": ")
        input_split = user_input.split() 
        
        if user_input == "quit":
            break

        #Keeping this in for de-bugging :)
        elif user_input in ("add", "subtract", "multiply", "divide"):
            num1 = float(input("\nEnter first number: "))
            num2 = float(input("Enter second number: "))
            result = getattr(calculator, user_input)(num1, num2)
            print("Result: ", result)
        
        elif user_input == "derivative":
            expression = input("\nEnter your expression. Example: 2x^2: ")
            result = calculator.calculate_derivative(expression)
            print("Result: ", result)
        
        elif user_input == "fib":
            n = int(input("\nEnter the number of Fibonacci numbers: "))
            result = calculator.fibonacci(n)
            print("Fibonacci sequence:", result)
            
        elif user_input == "graphFib":
            n = int(input("\nEnter the number n. Drawing the fibonnaci sequence from range (1, n). n: "))
            calculator.graphFibonacci(n)

        elif user_input == "c":
            result = 0

        elif user_input == "cc":
            result = 0
            if os.name == 'nt':
                _ = os.system('cls')
                calculator.print_menu()
            else:
                _ = os.system('clear')
                calculator.print_menu()
        
        elif user_input in ("graph"):
            #Comment: love the code here, but lets make a method in our calculator class that genereates the x and y value lists, 
            #we can have the user inputs here but lets not have calculations here, we can put that in the class object
            #see elif statements for primeGraph and equationGraph, you should know what i mean
            user_x = input("\nEnter x values. Seperate by spaces(1 23 4 33 2): ")
            x_list_string = user_x.split()
            x_list = [int(x) for x in x_list_string]
            user_y = input("\nEnter y values. Seperate by spaces(1 23 4 33 2): ")
            y_list_string = user_y.split()
            y_list = [int(x) for x in y_list_string]
            calculator.plot_graph(x_list, y_list)
            
        elif user_input == "primeGraph":
            num = int(input("Enter the number n. Drawing prime graph from range (1, n). n: "))
            calculator.make_prime_graph(num)
            
        elif user_input == "equationGraph":
            equation = input("Enter an equation (ex: x^2): ")
            startRange = int(input("Enter the starting number of the range: "))
            endRange = int(input("Enter the ending number of the range: "))
            smoothness = int(input("Enter the number of the points (0 to any number, more points = smoother graph): "))
            showGridLines = False if input("Show Grid lines 0 for No, 1 for yes: ") == "0" else True
            calculator.plot_equation(equation, (startRange, endRange), smoothness, showGridLines)
            
        #prime user input
        elif user_input in ("prime"):
        #Comment: my attempt to fix an error I noticed, when user input is anything but a number we get an error "invalid literal for int() with base 10:"
        #Comment: removed 'try' and 'except' 
                n = int(input("Enter a number: "))
                if calculator.is_number_prime(n):
                    print(f"{n} is a prime number.")
                else:
                    print(f"{n} is not a prime number.")
          
        elif user_input == "d to f":
            decimal = float(input("Enter the decimal number: "))
            result = calculator.decimal_to_fraction(decimal)
        
        elif user_input == "f to d":
            numerator = int(input("Enter the numerator: "))
            denominator = int(input("Enter the denominator: "))
            result = calculator.fraction_to_decimal(numerator, denominator)
        
        elif user_input in ("square", "square root"):
            num = float(input("\nEnter number: "))
            print("Result: ", calculator.square_root(num))
        
        elif user_input in ("fact"):
            num = float(input("\nEnter number: "))
            print("Result: ", calculator.factorial(num))
        
        elif user_input in ("log"):
          num = float(input("\nEnter number: "))
          base = float(input("Enter base (for natural use 0):"))
          result = calculator.log(num, base)
          print("Result: ", result)

        elif (user_input in ("complex")):
            num = input("\nEnter expression EX 4(4*5) : ")
            result = calculator.calculate_complex_expression(num)
            print("Result: ", result)


        elif user_input in ("simplify"):
            numerator = float(input("\nEnter numerator: "))
            denominator = float(input("Enter denominator: "))
            result = calculator.simplify_fraction(numerator, denominator)
            print("Result: ", result)
        
        #catch all for quick calculate
        elif ( len(input_split) >= 2 ):
            result = calculator.quick_calc(input_split, result)
            print("Result: ", result)



    
def main():
    try:
        calculatorSimulator()
    #error handler to handle, got some inspiration from natalie 
    except ValueError as E:
        print(E)
    #Comment: 'with' was misspelled, wuth -> with 
        print("Be careful with varible typings")
        main()

main()
