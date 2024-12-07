# Increment an operation set
def inc_op_set(op_set):
    # + -> * -> ||
    idx = 0
    while True:
        if idx >= len(op_set): break
        if op_set[idx] == "+":
            op_set[idx] = "*"
            break
        if op_set[idx] == "*":
            op_set[idx] = "||"
            break

        # Carry case
        if op_set[idx] == "||":
            op_set[idx] = "+"
            idx += 1
    return op_set

# Check an operation set against an equation
def check_op_set(equation, op_set):
    solution = equation[0]
    result = equation[1]
    for idx, i in enumerate(equation[2:]):
        op = op_set[idx]
        if op == "+": result += i
        if op == "*": result *= i
        if op == "||": result = int(str(result) + str(i))
    return result

# Check if an equation can be satisfied
def check_equation(equation):
    solution = equation[0]
    init_op_set = ["+"] * (len(equation[1:]) - 1)
    op_set = list(init_op_set)

    while True:
        if check_op_set(equation, op_set) == solution:
            return True
        op_set = inc_op_set(op_set)
        if op_set == init_op_set:
            break
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