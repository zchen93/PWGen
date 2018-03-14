#!/bin/python3
import random
import math

dict_lower_letter = 'abcdefghijklmnopqrstuvwxyz'
dict_upper_letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
dict_num = '1234567890'
dict_sign = '~!@#$%^&*()_+-=[]{};",.<>/?\|'

i = int(input('Fuck you '))
j = 1
pw = ''
result = i*[None]

for j in range(i): 
    pw = random.choice(dict_lower_letter + dict_upper_letter + dict_num + dict_sign)
    result[j] = pw
    
result_str = ''.join(map(str,result))
#print(result)
print(result_str)
#print(pw)
