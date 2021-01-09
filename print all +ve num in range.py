


list1=[12,-7,5,64,-14]
for l in list1:
    
    if l>0:
        print(l,end="  ")
        

list2=[12,14,-95,3]
listoutput=[]


for i in range(len(list2)):
    if list2[i]>0:
        listoutput.append(list2[i])
        
    else:
        continue
    
print(listoutput)