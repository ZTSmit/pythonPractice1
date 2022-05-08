def calculate(num1, num2):
    var_operand = input("""Input your operator of choice
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    Input here: """)
    try:
        var_operand = int(var_operand)
    except:
        return "Invalid Operand choice"
    return 2


print(calculate(2, 4))
