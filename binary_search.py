import random
import time


def generate_list_randoms():
    list_randoms = []
    for i in range(1000):
        n_random = random.randint(1, 1000)
        list_randoms.append(n_random)
        list_randoms = list(set(list_randoms))
    return list_randoms


def brute_force_search(list_search, n):
    i = 0
    for i in range(len(list_search)):
        if n == list_search[i]:
            return list_search[i]
        else:
            i += 1
    return "Number haven't found in generated list"


def binary_search(list_search, n):
    list_search.sort()
    low = 0
    high = len(list_search) - 1
    while low <= high:
        mid = int((low + high)/2)
        guess = list_search[mid]
        if guess == n:
            return guess
        elif guess > n:
            high = mid - 1
        else:
            low = mid + 1
    return "Number haven't found in generated list"


num_inp = input("Input number for search: ")
num_inp = int(num_inp)
list_num = generate_list_randoms()

print("")
print("------------------")
print("Brute-force search")
print("------------------")
start_time = time.clock()
result = brute_force_search(list_num, num_inp)
print(result)
end_time = time.clock()
print("Time elapsed = ", end_time - start_time)
print("")

print("--------------")
print("Binary search")
print("--------------")
start_time = time.clock()
result = binary_search(list_num, num_inp)
print(result)
end_time = time.clock()
print("Time elapsed = ", end_time - start_time)
print("")
