#sets and tuple ex
# sets ex
set1= {1, 2, 3, 4, 5}
print(set1)
print(type(set1))
set1.add(6)
print(set1)
set1.remove(2)
print(set1)

set2 = {"apple", "banana", "cherry"}
print(set2)

#tuple
tuple1 = (1, 2, 3, 4, 5)
print(tuple1)
print(type(tuple1))
#tuple are immutable meaning they connot be chnaged after creatiopn 
#this makes tuples useful for storing data that shou;ld not be modified
social_security_number = (123444, 4444445, 5676789)
print(social_security_number)