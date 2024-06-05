def frequency_Of_eachChar(s):
    new_dict = {}
    for i in s:
        if i not in new_dict:
            new_dict[i] = 1 
        else:
            new_dict[i] += 1
    return new_dict

frequency_of_all_char = frequency_Of_eachChar("abadbccacca")
print(frequency_of_all_char)