import os

def rule_of_three(a, b, c):
    result = (b * c) / a
    return result

def porcentage(a, b):
    result = (a / b) * 100
    return result
    
def clear_console():
    os.system('cls')
