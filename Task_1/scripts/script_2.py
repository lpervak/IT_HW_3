from script_1 import subs


def print_all_values_in_string(dic):   # Printing ALL values in a single string
    print(''.join(dic.values()))


print_all_values_in_string(subs)

print("---------------------------------------")

def print_each_value_in_string(dic):   # Printing EACH value in a single string
    for value in dic.values():
        print(value)


print_each_value_in_string(subs)