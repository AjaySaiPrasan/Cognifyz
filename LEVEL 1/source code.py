class Level1:
    @staticmethod
    def reverse_string():
        """
        Task 1: String Reversal
        Takes a string as input and returns the reverse of that string.
        """
        s=input("Enter a string to reverse: ")
        print(s[::-1])

    @staticmethod
    def convert_temperature():
        """
        Task 2: Temperature Conversion
        Converts temperatures between Celsius and Fahrenheit.
        Prompts the user to enter a temperature value and the unit of measurement, and then displays the converted temperature.
        """
        temp=float(input("Enter temperature: "))
        unit=input("Enter unit (C/F): ").upper()
        if unit=="C":
            x=(temp*9/5)+32
            print(f"{temp}°C is {x}°F")
        elif unit=="F":
            x=(temp-32)*5/9
            print(f"{temp}°F is {x}°C")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    @staticmethod
    def validate_email():
        """
        Task 3: Email Validator
        Validates whether a given string is a valid email address.
        Checks for the format, including the presence of an "@" symbol and a domain name.
        """
        import re
        pattern=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        email=input("Enter email: ")
        print("Valid email" if re.match(pattern, email) else "Invalid email")

    @staticmethod
    def calculator():
        """
        Task 4: Calculator Program
        Acts as a basic calculator.
        Prompts the user to enter two numbers and an operator (+, -, *, /, %),
        and then displays the result of the operation.
        """
        num1=float(input("Enter first number: "))
        num2=float(input("Enter second number: "))
        op=input("Enter operator (+, -, *, /, %): ")
        if op=="+":
            result=num1+num2
        elif op=="-":
            result=num1-num2
        elif op=="*":
            result=num1*num2
        elif op=="/":
            if num2!=0:
                result=num1/num2
            else:
                result="Error! Division by zero."
        elif op=="%":
            result=num1%num2
        else:
            result="Invalid operator"
        print(f"Result: {result}")

    @staticmethod
    def is_palindrome():
        """
        Task 5: Palindrome Checker
        Checks whether a given string is a palindrome.
        A palindrome is a word, phrase, or sequence that reads the same backward as forward.
        """
        s=input("Enter a string to check if it's a palindrome: ")
        print("Palindrome" if s==s[::-1] else "Not a palindrome")

print("TASK 1:")
Level1.reverse_string()
print()
print("TASK 2:")
Level1.convert_temperature()
print()
print("TASK 3:")
Level1.validate_email()
Level1.validate_email()
print()
print("TASK 4:")
Level1.calculator()
print()
print("TASK 5:")
Level1.is_palindrome()
Level1.is_palindrome()