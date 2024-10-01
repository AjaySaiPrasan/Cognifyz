import random
import string
import os

class Level2:
    @staticmethod
    def guessing_game():
        """
        Task 1: Guessing Game
        Generates a random number between 1 and 100. The user should guess the number, and the program provides hints.
        """
        n=random.randint(1,100)
        guess=None
        while guess!=n:
            guess=int(input("Guess the number between 1 and 100: "))
            if guess<n:
                print("Too low!")
            elif guess>n:
                print("Too high!")
            else:
                print("Congratulations! You guessed it right!")

    @staticmethod
    def number_guesser():
        """
        Task 2: Number Guesser
        Generates a random number within a specified range, and the user tries to guess it. Provides feedback on guesses.
        """
        l=int(input("Enter the lower bound of the range: "))
        u=int(input("Enter the upper bound of the range: "))
        n=random.randint(l,u)
        guess=None
        while guess!=n:
            guess=int(input(f"Guess the number between {l} and {u}: "))
            if guess<n:
                print("Too low!")
            elif guess>n:
                print("Too high!")
            else:
                print("Congratulations! You guessed it right!")

    @staticmethod
    def password_strength_checker():
        """
        Task 3: Password Strength Checker
        Evaluates the strength of a password based on length, uppercase, lowercase letters, digits, and special characters.
        """
        pwd=input("Enter a password to check its strength: ")
        n=len(pwd) >= 8
        u=any(c.isupper() for c in pwd)
        l=any(c.islower() for c in pwd)
        digit=any(c.isdigit() for c in pwd)
        spl=any(c in string.punctuation for c in pwd)
        if n and u and l and digit and spl:
            print("Strong password")
        else:
            print("Weak password")

    @staticmethod
    def fibonacci_sequence():
        """
        Task 4: Fibonacci Sequence
        Generates the Fibonacci sequence up to a given number of terms and displays it.
        """
        n=int(input("Enter the number of terms for the Fibonacci sequence: "))
        a,b=0,1
        sequence=[]
        for _ in range(n):
            sequence.append(a)
            a,b=b,a+b
        print("Fibonacci sequence:",sequence)

    @staticmethod
    def file_manipulation():
        """
        Task 5: File Manipulation
        Reads a text file and counts the occurrences of each word, displaying the results in alphabetical order.
        """
        filename=input("Enter the filename to read (including extension): ").strip('\"\'')
        if os.path.isdir(filename):
            print("The path provided is a directory. Please provide a file path.")
            return     
        wc={}
        try:
            with open(filename,'r') as file:
                text=file.read().lower()
                words=text.split()
                for i in words:
                    wc[i]=wc.get(i,0)+1
            sorted_words=sorted(wc.items())
            for word,count in sorted_words:
                print(f"{word}:{count}")
        except FileNotFoundError:
            print("File not found. Please check the filename and try again.")
        except PermissionError:
            print("Permission denied. Please check the file permissions and try again.")
        except OSError as e:
            print(f"OS error: {e}")

print("TASK 1:")
Level2.guessing_game()
print()
print("TASK 2:")
Level2.number_guesser()
print()
print("TASK 3:")
Level2.password_strength_checker()
print()
print("TASK 4:")
Level2.fibonacci_sequence()
print()
print("TASK 5:")
Level2.file_manipulation()