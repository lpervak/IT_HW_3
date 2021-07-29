import pickle
import numpy


def get_num_list(file_name):
    file = open(file_name, 'rb')
    num_list = pickle.load(file)
    file.close()
    print(num_list)
    return num_list


# I made a funct for getting average number with numpy lib. It also may be done with average_num=sum(num)/len(num)
def count_average(num):
    # print(numpy.mean(num))
    return numpy.mean(num)


print(count_average(get_num_list("task2")))
