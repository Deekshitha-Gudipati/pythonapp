list=[10,20.7,True]#10+20+true=1 so 31.7
print(sum(list))
list1=[10,20.7,'a',True]#it will give erorr cause for character it will to add so give erorr
n=10
list2=[]
for i in range(n):
    if i%2==0:
        list2.append(i)
print(list2)
#comprehensive list mean write the whole code in one line=>used for dealind with huge data
list3=[x for x in range(n) if x%2==1]
print(list3)