import random
import time


def generate_dict(str_in):
    dict_out = dict()
    for i in range(len(str_in)):
        for j in range(len(str_in)):
            for k in range(len(str_in)):
                n_random = random.randint(1, 10000)
                dict_out["{}{}{}".format(str_in[i],str_in[j],
                                         str_in[k])] = n_random
    print("")
    print("Create dict with numbers of keys: ", len(dict_out.keys()))
    print("")
    return dict_out

def generate_random_keys(str_in, dict_in):
    random_keys = list()
    for i in range(20):
        random_key = "".join(random.choice(str_in) for i in range(3))
        random_keys.append(random_key)
    return random_keys

def get_values_from_dict(random_keys, dict_in):
    for i,item in enumerate(random_keys):
        print("")
        print("--------------------------")
        print("Get value #{} for key: {}".format(i + 1, item))
        print("--------------------------")
        start_time = time.clock()
        result = dict_in[item]
        print("Value: ", result)
        end_time = time.clock()
        print("Time elapsed = ", end_time - start_time)
        print("")


if __name__ == "__main__":
    str_in = "abcdefghijklmnopqrstuvwxyz"
    dict_in = generate_dict(str_in)
    random_keys = generate_random_keys(str_in, dict_in)
    get_values_from_dict(random_keys, dict_in)

