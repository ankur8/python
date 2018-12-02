import itertools
l=[1,3,5,6,7]

for i,j in enumerate(l):
    print(i,j,l[i]==j)


for p in range(len(l),0,-1):
    print(p,"wow")

for i in range(1,len(l)):
    for seq in itertools.combinations(l, i):
        print(seq)
        if sum(seq) == 6:
            print("sum",seq)