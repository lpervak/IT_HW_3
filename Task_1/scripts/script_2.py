from script_1 import subs


def print_each_value_in_string(dic):   # Printing EACH value in a single string
    for value in dic.values():
        with open("text_only.txt", "a+") as file_object:
            # Move read cursor to the start of file.
            file_object.seek(0)
            # If file is not empty then append '\n'
            data = file_object.read(100)
            if len(data) > 0:
                file_object.write("\n")
            # Append text at the end of file
            file_object.write(value)


print_each_value_in_string(subs)
