#               Python Cookbook
#               Chapter 10 - Variables - Global vs Local Scope

# Variable scope is a container of variable
# Each function has its own local scope
# Variables are either local or global
# Global Scope is code outside all functions
# Global Var created at the beginnning of a program and destroy at the end of the program
# Local Var are created and destroyed within the function

# Importance of Scope
#   1) Global code CANNOT access local var
#   2) Local code CAN access Global Var
#   3) Local code CANNOT another Local Scope Var
#   4) You can use the same Var name if there are in different scopese

# Scopes compartmentlize variables/code

spam - 42 # global varuabke

def eggs():
    spam = 42 # this is a local variable

print("Some code here")
print("Some more code.")

eggs =101
def spam():
    # As long as there is a local eggs var the function yours it
    # But if only a global eggs var is present it is used
    eggs = 99
    bacon()
    print(eggs)

def bacon():
    global ham = 101 # Global ham variable
    eggs =0  # Local eggs variables are created and destroyed here


spam() # Local eggs var
print(eggs) # Global eggs var
