for i in range(1, 100+1):
    output = ""

    divisibleBy3 = i % 3 == 0
    divisibleBy5 = i % 5 == 0

    if divisibleBy3 and divisibleBy5:
        output = "FizzBuzz"
    elif divisibleBy3:
        output = "Fizz"
    elif divisibleBy5:
        output = "Buzz"
    else:
        output = str(i)

    print(output)

