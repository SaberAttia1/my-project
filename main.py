# program to automatically generate a PDA from a given CFG and simulate it on input strings.

def simulate_pda(cfg, start_symbol, input_str):
    stack = [start_symbol]
    input_str += '$'
    pointer = 0
    while stack:
        top = stack.pop()
        if pointer >= len(input_str):
            return False
        if top in cfg:
            for production in cfg[top]:
                if production[0] == input_str[pointer]:
                    stack.extend(reversed(production[1:]))
                    break
            else:
                return False
        elif top == input_str[pointer]:
            pointer += 1
        else:
            return False
    return input_str[pointer:] == '$'

cfg = {
    "S": [["a", "S", "b"], ["a", "b"]]
}

print(simulate_pda(cfg, "S", "aabb"))  # T
print(simulate_pda(cfg, "S", "aaabbb"))  # T
print(simulate_pda(cfg, "S", "aab"))  # F
#========================================================
# program to simulate a Turing Machine that increments a binary number by 1
def increment_binary(bin_str):
    tape = list(bin_str)
    i = len(tape) - 1
    while i >= 0:
        if tape[i] == '0':
            tape[i] = '1'
            break
        else:
            tape[i] = '0'
            i -= 1
    if i < 0:
        tape = ['1'] + tape
    return ''.join(tape)

print(increment_binary("1011"))  # => 1100
print(increment_binary("111"))   # => 1000

# id > 4490
