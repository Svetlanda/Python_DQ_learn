# HOME TASK 4.2
# 1. create a list of random number of dicts (from 2 to 10)
# dict's random numbers of keys should be letter,
# dict's values should be a number (0-100),
# example:[{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]

# 2. get previously generated list of dicts and create one common dict:
# if dicts have same key, we will take max value, and rename key with dict number with max value
# if key is only in one dict - take it as is,
# example:{'a_1': 5, 'b': 7, 'c': 35, 'g_2': 42}
# Each line of code should be commented with description.

import random

# constants
rnd_letters = "abcde"
rnd_number_min = 0
rnd_number_max = 100
dict_count_min = 2
dict_count_max = 10

# declaration of result variables:
random_list = []
max_value_dict = {}

def random_numbers(min_value, max_value):
    return random.randint(min_value, max_value)

def random_letters(letters):
    return random.choice(letters)

def random_dicts(min_value, max_value):
    dicts_elements = random_numbers(dict_count_min, dict_count_max)
    for i in range(dicts_elements):
        dict = {}
        for j in range(dicts_elements):
            dict[random_letters(rnd_letters)] = random_numbers(rnd_number_min, rnd_number_max)
        random_list.append(dict)
        # print(dict)
    return random_list

def get_max_value_from_list_of_dict(v_list):
    dict_rn = 1
    dict_max_result = {}
    tmp_dict = {}
    for dicts in v_list:
        for key, value in dicts.items():  # for each dictionary in random_list
            is_updated = False  # indicator of updated value
            if key not in tmp_dict:  # if it first or unique key
                tmp_dict[key] = (value, dict_rn, is_updated)  # just insert as is
            else:  # means that key has already been inserted
                is_updated = True  # means that value need to be updated OR index should be updated
                if value > tmp_dict[key][0]:
                    tmp_dict.update({key: (value, dict_rn, is_updated)})  # update value
                else:
                    tmp_dict.update({key: (tmp_dict[key][0], tmp_dict[key][1], is_updated)})  # update index
        dict_rn += 1
    # Creation result dictionary with max value for each key:
    for key, value in tmp_dict.items():
        if value[2]:  # If returns TRUE. Means that value has been updated for this key
            dict_max_result.update({key + '_' + str(value[1]): value[0]})  # add index for key name
        else:
            dict_max_result.update({key: value[0]})  # just leave key name as is
    return dict_max_result

def print_result(list, dict):
    print(f'Random_list = {list}')
    print(f'Max result with index = {dict}')


random_list = random_dicts(dict_count_min, dict_count_max)
max_value_dict = get_max_value_from_list_of_dict(random_list)
# list_for_test = [{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]
# max_value_dict = get_max_value_from_list_of_dict(list_for_test)

print_result(random_list, max_value_dict)

