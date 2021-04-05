import random
import time


def generate_list_randoms():
    list_randoms = []
    for i in range(1000):
        n_random = random.randint(1, 1000)
        list_randoms.append(n_random)
        list_randoms = list(set(list_randoms))
    return list_randoms


def findSmallest(list_in):
    smallest = list_in[0]
    smallest_index = 0
    for i in range(1, len(list_in)):
        if list_in[i] < smallest:
            smallest = list_in[i]
            smallest_index = i
    return smallest_index


def selecttionSort(list_in):
    list_out = []
    for i in range(len(list_in)):
        smallest = findSmallest(list_in)
        list_out.append(list_in.pop(smallest))
    return list_out


print("--------------")
print("Selection sort")
print("--------------")
list_in = generate_list_randoms()
start_time = time.clock()
result = selecttionSort(list_in)
print(result)
end_time = time.clock()
print("Time elapsed = ", end_time - start_time)
