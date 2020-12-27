lst=[]
n=int(input("Enter The Number"))
for i in range(0,n):
    els=int(input())
    lst.append(els)
print("Positive Number In The List Are:")
for j in range(n):
    if lst[j]>=0:
        print(lst[j],end='')
        