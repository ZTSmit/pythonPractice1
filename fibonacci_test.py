def fibonacci_check(num_check):
    test_statement = ""  # Placeholder value

    test_value = False  # Placeholder value

    fib_list = [1, 1]  # The basic numbers where all fibonacci sequences are formed

    try:  # Checks if the input can even be converted to a string
        num_check = int(num_check)
    except ValueError:
        test_statement = "Not a number"
        print(test_statement)
        return test_statement

    x = 0
    while x > -1:  # Functionally infinite loop but should always break out
        if num_check == 2 or num_check == 1 or num_check == fib_list[x]:  # 1 and 2 are values in a fib. sequence
            test_value = True
            break
        elif num_check > 2 and num_check > fib_list[x]:  # Creates a fib. sequence from the starting list
            fib_list.append(fib_list[x] + fib_list[x + 1])
            # print(fib_list)
            x = x + 1
            continue
        elif num_check < fib_list[x]:   # If the number is higher than the latest iteration in a fibonacci sequence
            test_value = False          # and still has not been found, it means it is not in the fibonacci sequence
            break

    if test_value:
        test_statement = str(num_check) + " is in a fibonnaci sequence"
        print(test_statement)
        return test_statement
    else:
        test_statement = str(num_check) + " is not in a fibonacci sequence"
        print(test_statement)
        return test_statement
