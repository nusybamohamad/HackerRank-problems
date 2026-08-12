def print_formatted(number):
    width = len(bin(number)[2:])

    for i in range(1, number + 1):
        decimal = str(i)
        octal = oct(i)[2:]
        hexadecimal = hex(i)[2:].upper()
        binary = bin(i)[2:]

        print(decimal.rjust(width),
              octal.rjust(width),
              hexadecimal.rjust(width),
              binary.rjust(width))

    


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna