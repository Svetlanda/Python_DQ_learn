# HOME TASK 2
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

# declaration of variables:

dictElements = random.randint(2, 10)  # random value of dict limit
a = 0  # random start value
b = 100  # random end value
letters = "abcdef"  # for random key names
randomlist = []

print('Dicts elements= ', dictElements)

# creation random list of dictionary:

for i in range(dictElements):
    dict = {}
    for j in range(dictElements):
        d_letter = random.choice(letters)
        d_number = random.randint(a, b)
        dict[d_letter] = d_number
    randomlist.append(dict)
print('Random list of dicts: ', randomlist)

# creation temporary dictionary with key, max value, index and is_updated flag

tmpDict = {}
dictRn = 1

for dict_ in randomlist:
    for key, value in dict_.items():  # for each dictionary in randomlist
        isUpdated = False  # indicator of updated value
        if key not in tmpDict:  # if it first or unique key
            tmpDict[key] = (value, dictRn, isUpdated)  # just insert as is
        else:  # means that key has already been inserted
            isUpdated = True  # means that value need to be updated OR index should be updated
            if value > tmpDict[key][0]:
                tmpDict.update({key: (value, dictRn, isUpdated)})  # update value
            else:
                tmpDict.update({key: (tmpDict[key][0], tmpDict[key][1], isUpdated)})  # update index
    dictRn += 1
# print('Temporary dicts set: ', tmpDict)

# Creation result dictionary with max value for each key:

dictMaxResult = {}

for key, value in tmpDict.items():
    if value[2]:  # If returns TRUE. Means that value has been updated for this key
        dictMaxResult.update({key + '_' + str(value[1]): value[0]})  # add index for key name
    else:
        dictMaxResult.update({key: value[0]})  # just leave key name as is
print("Result dict with max value: ", dictMaxResult)
