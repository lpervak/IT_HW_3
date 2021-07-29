def dec_num(list_nums):
    def wrap(*args, **kwargs):
        list_numbers = list_nums(*args, **kwargs)
        nums_to_str = []
        for i in list_numbers:
            nums_to_str.append(str(i))
        print(nums_to_str)
        return list_numbers
    return wrap


@dec_num
def list_nums_():
    num = int(input("Enter NUM: "))
    list_num = list(range(0, num))
    return list_num


list_nums_()
