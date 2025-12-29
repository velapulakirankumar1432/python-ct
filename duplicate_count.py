s=[1,4,2,5,8,4,8,2]
res=[]
for num in s:
    if s.count(num)>1:
        if num not in res:
            res.append(num)
    print(res)
