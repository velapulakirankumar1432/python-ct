s=[1,5,7,10,-1]
i=0
j=4
while i<j:
    s[i],s[j]=s[j],s[i]
    i=i+1
    j=j-1
print(s)
