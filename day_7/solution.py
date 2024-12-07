# Check an operation set against an equation
def check_op_set(equation, op_set):
    # 0 -> +, 1 -> *
    solution = equation[0]
    result = equation[1]
    for i in equation[2:]:
        if op_set & 1: result *= i
        else: result += i
        op_set = op_set >> 1
    return result

# Check if an equation can be satisfied
def check_equation(equation):
    solution = equation[0]
    max_inc = 2 ** (len(equation[1:]) - 1)

    for i in range(0, max_inc):
        if check_op_set(equation, i) == solution:
            return True
    return False

# Load the input
with open("input.txt", "r") as filein:
    raw_data = filein.read()
equations = raw_data.split("\n")
equations = [i.replace(":", "").split(" ") for i in equations]
for i in range(0, len(equations)):
    equations[i] = [int(j) for j in equations[i]]

# Calculate the result
total = 0
for i in equations:
    if check_equation(i):
        total += i[0]
print(f"Total: {total}")