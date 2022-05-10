def calculate(num1, num2):
    operand_enum_add = ("add", "addition")
    operand_enum_sub = ("sub", "subtract", "subtraction")
    operand_enum_mult = ("mult", "multiply", "multiplication")
    operand_enum_div = ("div", "divide", "division")
    operand_enum = operand_enum_add + operand_enum_sub + operand_enum_mult + operand_enum_div  #combined tuple of all the operands
    #operand_enum = ("add","addition","sub","subtract","subtraction","mult","multiply","multiplication","div","divide","division")#test values

    num_result = 0
    statement_exception = "Please input a valid operand"
    filler_words = "Your result is "

    var_operand = input("""Input your operator of choice
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    Input here: """)

    # Testing if it's a valid text input for the operand
    if var_operand in operand_enum:
        if var_operand in operand_enum_add:  # addition
            var_operand = 1
        elif var_operand in operand_enum_sub:  # subtraction
            var_operand = 2
        elif var_operand in operand_enum_mult:  # multiplication
            var_operand = 3
        elif var_operand in operand_enum_div:  # division
            var_operand = 4
        else:
            print("I don't know how we got here")  # I don't think this is a possible error
    else:
        try:
            var_operand = int(
                var_operand)  # If a number input already corresponded to an operand, otherwise could break if it were a string?
        except ValueError:
            print(statement_exception)
            return filler_words + "Invalid"

    # Actual calculator
    if var_operand == 1:  # addition
        num_result = num1 + num2
    elif var_operand == 2:  # subtraction
        num_result = num1 - num2
    elif var_operand == 3:  # mult
        num_result = num1 * num2
    elif var_operand == 4:  # Division
        num_result = num1 / num2
    else:  # If the number input didn't correspond to any operand
        print(statement_exception)
        return filler_words + "Invalid"
    return filler_words + str(num_result)


print(calculate(2, 4))
