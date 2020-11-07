
a=[]
idx=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010]
name=["Rashi Bank","Premium Bank Corp.","New Walth Trust","IDIDI Bank","Premium Bank Corp","IDIDI Bank","New Wealth Trust","Rashi Bank","Rashi Bank","New Wealth Trust"]
amount=[50000,30000,5000,45000,80000,50000,5000,7000,12500,50000]
duration=[6,4,1,1,5,8,3,2,3,12]
ty=["Business","Personal","Business","Personal","Personal","Business","Personal","Business","Personal","Personal"]
interest=[10,9,8,10,11,10,10,10.5,10,9.5]
for i in range(10):
    d={}
    d["id"]=idx[i]
    d["name"]=name[i]
    d["amount"]=amount[i]
    d["duration"]=duration[i]
    d["type"]=ty[i]
    d["interest"]=interest[i]
    a.append(d)
print(a)