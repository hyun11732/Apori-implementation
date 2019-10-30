from itertools import combinations
from collections import OrderedDict

# This function takes dic and minsup as parameters and eliminate a word which has lower frequency than minsup
def cut_minsup(dic, minsup):
    words = dic.keys()
    for word in list(words):
        if dic[word] < minsup:
            del dic[word]
    return dic

# Simply count the word in the initial input
def count_first_freq(inputs, minsup):
    dic = dict()
    for line in inputs:
        for word in line:
            if word not in dic.keys():
                dic[word] = 1
            else:
                dic[word] += 1
    return cut_minsup(dic, minsup)

# Sort dictionary by alphabetical order
def tuple_sort(dic, count):
    new_dic = dict()
    for t in dic.keys():
        t_sorted = sorted(t)
        new_dic[tuple(t_sorted)] = dic[t]
    return new_dic

# Sort dictionary by frequency
def sorting(dic):
    new_dic = dict()
    alpha_sort = sorted(list(dic.keys()))
    num_sort = sorted(alpha_sort, key=dic.get, reverse=True)
    for i in num_sort:
        new_dic[i] = dic[i]
    return new_dic

# Self join k-itemset to create k+1 itemset
def self_join(sets, length):
    l = []
    if length == 2:
        return list(combinations(sets, length))
    else:
        for s in sets:
            for elem in s:
                if elem not in l:
                    l.append(elem)
        return list(combinations(l, length))

# Pruneing process to delete k+1 itemset which subsets are not in k itemset
def prune(candidate, previous_set, length, inputs, minsup):
    dic = dict()
    if length == 2:
        for candid in candidate:
            dic[candid] = 0
    else:
        for t in candidate:
            subsets = combinations(list(t), length - 1)
            count = 0
            subsets = list(subsets)
            for subset in subsets:
                if set(subset).issubset(set(previous_set)):
                    break
                count += 1
            if count == len((subsets)):
                dic[t] = 0
    for key in dic.keys():
        for line in inputs:
            if set(list(key)).issubset(set(line)):
                dic[key] += 1
    return cut_minsup(dic, minsup)

# Create string dictionary from tuple to count its frequency
def make_string_dic(dic):
    new_dic = dict()
    for t in list(dic.keys()):
        if type(t) == type(tuple()):
            string = ""
            for elem in t:
                string += elem + " "
            string = string[:-1]
            new_dic[string] = dic[t]
        else:
            new_dic[t] = dic[t]
    return new_dic

# make closed set result
def closed_compression(dic):
    closed_dic = dict()
    for key1 in list(dic.keys()):
        test = True
        string1 = key1
        if type(key1) == type(string) and len(key1) != 1:
            key1 = (key1,)
        for key2 in list(dic.keys()):
            string2 = key2
            if type(key2) == type(string) and len(key2) != 1:
                key2 = (key2,)
            if key1 != key2 and set(list(key1)).issubset(set(list(key2))) and dic[string1] == dic[string2]:
                test = False
                break;
        if (test):
            closed_dic[string1] = dic[string1]
    return make_string_dic(closed_dic)

# make max set result
def max_compression(dic):
    max_dic = dict()
    for key1 in list(dic.keys()):
        test = True
        string1 = key1
        if type(key1) == type(string) and len(key1) != 1:
            key1 = (key1,)
        for key2 in list(dic.keys()):
            string2 = key2
            if type(key2) == type(string) and len(key2) != 1:
                key2 = (key2,)
            if key1 != key2 and set(list(key1)).issubset(set(list(key2))):
                test = False
                break
        if (test):
            max_dic[string1] = dic[string1]
    return make_string_dic(max_dic)


if __name__ == "__main__":
    minsup = int(input())
    string = input()
    inputs = []
    while string != "":
        temp = string.split()
        inputs.append(temp)
        try:
            string = input()
        except:
            break
    dic = count_first_freq(inputs, minsup)
    dic = sorting(dic)
    previous_length = 0
    count = 2
    m = 0
    sorted_set = []
    # apori algorithm keep going up until it returns nothing
    while True:
        previous_set = list(dic.keys())[previous_length:len(dic)]
        previous_length = len(dic)
        candidate = self_join(previous_set, count)
        if len(candidate) == 0:
            break
        temp = prune(candidate, previous_set, count, inputs, minsup)
        temp = tuple_sort(temp, count)
        if len(temp) == 0:
            break
        dic.update(temp)
        count += 1
        m += 1
    string_dic = make_string_dic(dic)
    keys = sorted(string_dic, key=lambda l: (-string_dic[l], l))
    closed_dic = closed_compression(dic)
    closed_keys = sorted(closed_dic, key=lambda l: (-closed_dic[l], l))
    max_dic = max_compression(dic)
    max_keys = sorted(max_dic, key=lambda l: (-max_dic[l], l))
    for key in keys:
        print(string_dic[key], " ", "[", key, "]", sep="")
    print("")
    for key in closed_keys:
        print(string_dic[key], " ", "[", key, "]", sep="")
    print("")
    for key in max_keys:
        print(string_dic[key], " ", "[", key, "]", sep="", end='\n')


