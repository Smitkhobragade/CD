ll1_table = {'S' : {'a' : ['A'], 'b' : ['A'], 'c' : ['BC']}, 'A' : {}, 'B' : {}} # parsing table

def parse(user_input, start_symbol, ll1_table):
    flag = 0
    user_input = user_input + "$"
    stack = []
    buffer = list(user_input)

    stack.append("$")
    stack.append(start_symbol)

    input_len = len(user_input)
    index = 0

    print("{:<20} {:<20} {:<20}".format("Stack", "Buffer", "Action"))
    print("-" * 50)

    while len(stack) > 0:
        top = stack[len(stack) - 1]
        current_input = buffer[index]

        if top == current_input:
            stack.pop()
            index = index + 1
        else:
            key = top, current_input
            if top == '$':
                flag = 1
                break
            if ll1_table[top][current_input] == []:
                flag = 1
                break
            value = ll1_table[top][current_input]

            if value != ['#']:
                value = str(value[0])
                value = value[::-1]
                value = list(value)
                stack.pop()

                for element in value:
                    stack.append(element)
            else:
                stack.pop()
        if current_input == '$':
          break
        print("{:<20} {:<20} {:<20}".format("".join(stack), "".join(buffer[index:]), " ".join(value)))

    if flag == 0:
        print("String accepted!")
    else:
        print("String not accepted!")

print("---------- Case 1 : String Acceptance -----------\n")
# parse("pc", "S", ll1_table)
parse("c", "S", ll1_table)
# print("\n--------- Case 2 : String Rejection -----------\n")
# parse("ap", "S", ll1_table)