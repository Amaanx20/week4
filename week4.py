def dog(number):
    if 0 <= number <= 100:
        return True
    else:
        return False

number_check = 55
awnser = dog(number_check)
print(awnser)

def num_count(len_case):
    upper = 0
    lower = 0
    for case in len_case:
        if case.isupper():
            upper +=1
        elif case.islower():
            lower +=1
    print("upper case:", upper)
    print("Lowercase:", lower)

    len_case('The Man')

