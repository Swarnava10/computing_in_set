a=[]
b=[]
a=(input("Enter numbers for list A: ")).split()
a=[int (x) for x in a]
b=(input("Enter numbers for list B: ")).split()
b=[int (x) for x in b]
inters=[]
sum=[]
diff=[]
symmetricdiff=[]
a=list(set(a))
b=list(set(b))
sum=list(set(a+b))

for i in a:
    if i in b:
        inters.append(i)
    if i not in b:
        diff.append(i)


for i in sum:
    if i not in inters:
        symmetricdiff.append(i)
print("The UNION of A and B is : ",sum)
print("Intersection of A and B is : ",inters)
print("Difference of A and B is : ",diff)
print("The symmetric difference of A and B is:  ",symmetricdiff)
