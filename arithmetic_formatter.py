def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    first_line = []
    second_line = []
    dashes = []
    results = []

    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            return 'Error: Each problem must contain two operands and one operator.'
        
        num1, operator, num2 = parts

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        if not (num1.isdigit() and num2.isdigit()):
            return 'Error: Numbers must only contain digits.'

        if len(num1) > 4 or len(num2) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        width = max(len(num1), len(num2)) + 2

        first_line.append(num1.rjust(width))
        second_line.append(operator + num2.rjust(width - 1))
        dashes.append('-' * width)

        if show_answers:
            result = str(eval(f"{num1} {operator} {num2}"))
            results.append(result.rjust(width))

    arranged = "    ".join(first_line) + "\n" + \
               "    ".join(second_line) + "\n" + \
               "    ".join(dashes)

    if show_answers:
        arranged += "\n" + "    ".join(results)

    return arranged

# Call the function
print(arithmetic_arranger(["3801 - 2", "123 + 49"], show_answers=True))
