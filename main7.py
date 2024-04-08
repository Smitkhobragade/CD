import pandas as pd

blocks_content = """
b = 1
c = 2

a = b + c
d = a - b

d = c + d

c = b + c
e = a - b

d = b + c
e = e + 1

b = c * d
c = b - d
"""

blocks = [block.strip().split('\n')
          for block in blocks_content.strip().split('\n\n')]

for t in blocks:
    for y in range(len(t)):
        t[y] = t[y].strip("\n")


class Expression:
    def __init__(self, number, expression):
        self.number = number
        self.expression = expression

    def __str__(self):
        return f"{self.number}) {self.expression}"


class Block:
    def __init__(self, block_number, expressions):
        self.expressions = expressions
        self.block_number = block_number

    def __str__(self):
        output = f"Printing block number: {self.block_number}\n"
        for expression in self.expressions:
            output += str(expression) + "\n"
        output += "\n"
        return output


expressions = []
blocks_class = []
number = 1
for i in range(len(blocks)):
    exprs = []
    for j in range(len(blocks[i])):
        exprs.append(Expression(number, blocks[i][j]))
        number += 1
    expressions.append(exprs)
    blocks_class.append(Block(i + 1, exprs))

DAG_matrix = [
    [0, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0],
    [0, 0, 0, 1, 1, 0],
    [0, 1, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
]

OUTPUT = {}
OUTPUT["Blocks"] = [f"B{block.block_number}" for block in blocks_class]
OUTPUT["GEN"] = [0] * len(blocks_class)
OUTPUT["KILL"] = [0] * len(blocks_class)
OUTPUT["Predecessor"] = [0] * len(blocks_class)
OUTPUT["IN"] = [set() for _ in range(len(blocks_class))]
OUTPUT["OUT"] = [0] * len(blocks_class)

gen_array = [[expr.number for expr in block.expressions]
             for block in blocks_class]
OUTPUT["GEN"] = [set(i) for i in gen_array]

kill_arr = []
for i in range(len(blocks_class)):
    lhs = []
    temp_kill = []
    for expression in blocks_class[i].expressions:
        parts = expression.expression.split("=")
        lhs.append(parts[0].strip())
    for j in range(len(blocks_class)):
        if i == j:
            continue
        for other_expression in blocks_class[j].expressions:
            parts = other_expression.expression.split("=")
            if parts[0].strip() in lhs:
                temp_kill.append(other_expression.number)
    kill_arr.append(temp_kill)

OUTPUT["KILL"] = [set(i) for i in kill_arr]

precedence_arr = []
for i in range(len(blocks_class)):
    temp_prec = []
    for j in range(len(blocks_class)):
        if DAG_matrix[j][i] == 1:
            temp_prec.append(j + 1)
    precedence_arr.append(temp_prec)

OUTPUT["Predecessor"] = precedence_arr
OUTPUT["OUT"] = [set(i) for i in OUTPUT["GEN"]]

df = pd.DataFrame(OUTPUT)
print(f"Iteration: {0}")
print(df)
print()

iteration = 1
change = True
while change:
    change = False
    for i in range(len(blocks_class)):
        precs = OUTPUT["Predecessor"][i]
        temp_set = set()
        for p in precs:
            temp_set = temp_set.union(OUTPUT["OUT"][p - 1])
        OUTPUT["IN"][i] = temp_set
        old_out = OUTPUT["OUT"][i]
        OUTPUT["OUT"][i] = (OUTPUT["IN"][i] - OUTPUT["KILL"]
                            [i]).union(OUTPUT["GEN"][i])
        if old_out != OUTPUT["OUT"][i]:
            change = True
    if change:
        print(f"Iteration: {iteration}")
        df_iteration = pd.DataFrame(OUTPUT)
        print(df_iteration)
        print()
        iteration += 1

print(f"Iteration: {iteration}")
final_df = pd.DataFrame(OUTPUT)
print(final_df)
