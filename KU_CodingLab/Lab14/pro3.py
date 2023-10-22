def create_dict():
    my_dict = {}
    while True:
        user_input = input()
        if user_input == "-1":
            return my_dict
        vari_name, value = user_input.split(" = ")
        my_dict[vari_name] = value


def main_program():
    program = []
    while True:
        program_input = input()
        if program_input == "-1":
            return program
        program.append(program_input)


print("Enter variables and values:")
input_dict = create_dict()

print("Enter your program:")
programs = main_program()

print("Result:")
for expression in programs:
    for key in input_dict:
        expression = expression.replace(
            f"{{{key}}}", str(input_dict[key]))
    print(expression)
