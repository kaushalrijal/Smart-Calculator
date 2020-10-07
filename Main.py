__author__ = "Kaushal Rijal"

"""
Project Title: Smart Calculator
Project Author: Kaushal Rijal
Project Start: Monday, August 24, 2020
Project End: 

python "D:\Kaushal\Programming\Python\PycharmProjects\Smart Calculator\oop.py"
"""

import os

os.system("cls")
print("Hello Welcome to the Smart Calculator")
print("My name is Matthew, I can solve your Mathematical Questions...\n")

class Calculator:
    def __init__(self, problem):
        self.problem = problem
    
    def solve(self):
        if "quit" in self.problem or "exit" in self.problem or "finish" in self.problem:
            self.quitCom()

        else:
            try:
                self.calculate(self.problem)
            except:
                self.process()
    
    def calculate(self, question):
        print(eval(question))

    def process(self):
        if "creat" in self.problem or "buil" in self.problem:
            print("Kaushal Rijal The Great is my creator...")

        elif "your" in self.problem and "name" in self.problem:
            print("My name is Matthew!")

        elif "add" in self.problem or "sum of" in self.problem:
            try:
                self.simplify("and", "+")
            except:
                self.simplify("sum of", "+")

        elif "is added to" in self.problem:
            self.simplify("is added to", "+")

        elif "difference" in self.problem:
            self.simplify("and", "-")

        elif "product of" in self.problem:
            self.simplify("and", "*")

        elif "is multiplied" in self.problem and ("to" in self.problem or "with" in self.problem):
            try:
                self.simplify("is multiplied to", "*")
            except:
                self.simplify("is multiplied with", "*")
        elif "divide" in self.problem:
            try:
                self.simplify("by", "/")
            except:
                self.simplify("and", "/")

        else:
            print("Sorry I could not get you!")

    def simplify(self, phrase, operator):
        question = self.problem.replace(phrase, operator)
        question = self.translate(question)
        self.calculate(question)

    def translate(self, phrase):
        translation = ""
        for letter in phrase:
            if letter in "ABCEDFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ;":
                translation = translation + ""
            else:
                translation = translation + letter
        return translation

    def quitCom(self):
        input("Press enter key to exit:")
        quit()
    

if __name__ == "__main__":
    while True:
        question = input("Please enter a question: ")
        problem = Calculator(question)
        problem.solve()
