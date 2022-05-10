
def fibonacci_check(num_check):

    test_value = True

    fib_list = [1, 1]

    try:
        num_check = int(num_check)
    except ValueError:
        print("Not a number")
        return

    x = 0
    while x > -1:
    # for x in range(200):
        if num_check == 2 or num_check == 1 or num_check == fib_list[x]:
            test_value = True
            break
        elif num_check > 2 and num_check > fib_list[x]:
            fib_list.append(fib_list[x] + fib_list[x+1])
            print(fib_list)
            x = x+1
            continue
        elif num_check < fib_list[x]:
            test_value = False
            break

    if test_value:
        print(str(num_check) + " is in a fibonnaci sequence")
    else:
        print(str(num_check) + " is not in a fibonacci sequence")


fibonacci_check(2)
