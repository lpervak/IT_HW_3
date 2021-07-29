list_old = [1, 2, "3.0", "f", 4, "4", "sd", '14', '4f']
list_new = []


def get_nums(count_nums):
    def wrap():
        for i in list_old:
            if type(i) == int:
                list_new.append(i)
            elif type(i) == float:
                list_new.append(i)
            elif type(i) == str:
                try:
                    int(i)
                    list_new.append(int(i))
                except ValueError:
                    try:
                        float(i)
                        list_new.append(float(i))
                    except ValueError:
                        pass
            else:
                pass
        print(list_new)
        result = count_nums(list_new)
        return print(result)
    return wrap


@get_nums
def count_nums(x):
    print(sum(x))


count_nums()
