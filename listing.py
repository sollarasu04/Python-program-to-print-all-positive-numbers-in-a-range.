#Write a Python program to print all positive numbers in a range.
list1 = [12,-7,5,64,-14]
list2 = [12,14,-95,3]
list3 = list1 + list2
print(list3) 
for num in list3:
    if num>0:
        print(num, end=" ")
