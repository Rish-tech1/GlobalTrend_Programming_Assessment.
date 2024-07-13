def arithmetic(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        if b == 0:
            return "Error: Division by zero is not allowed"
        else:
            return a / b
    else:
        return "Error: Invalid operator"

print(arithmetic(10, 2, "+")) 
print(arithmetic(10, 2, "-")) 
print(arithmetic(10, 2, "*")) 
print(arithmetic(10, 2, "/"))  
print(arithmetic(10, 0, "/"))  