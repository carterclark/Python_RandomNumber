#Random Number and Operator

import random
def num():                       
    num1 = 0
    num = random.randrange(1, 100)
    return (num)
    

def operation():                    
    sign = random.randint(1, 4)
    if sign == 1:
        return "+"
    elif sign == 2:
        return "-"
    elif sign == 3:
        return "*"
    elif sign == 4:
        return "//"
        
def check(num1,num2,sign,guess):        
    answer = 0
    if sign == "+":
        answer = (num1 + num2)
    elif sign == "-":
        answer = (num1 - num2)
    elif sign == "*":
        answer = (num1 * num2)
    elif sign == "//":
        answer = (num1 // num2)

    if answer == guess:
        print("True, the answer is: ",answer)
        return ""
    else:
        print("False, the correct answer is: ", answer)
        return ""

def start():
    end = "y"
    while end != "n":
        sign = operation()
        num1 = num()
        num2 = num()
        print(num1,sign,num2,"= ?")
        guess = int(input("Enter guess as a number: "))
        answer = check(num1,num2,sign,guess)
        print(answer)                       
        end = input("Continue? y or n: ")
start()
