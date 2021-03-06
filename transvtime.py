import pandas as pd
def send_json(file_name):
    def Transaction(df):
        D={}
        for i in range(len(df["transactions"][0])):
            d={}
            f=df["transactions"][0][i]
            d["Type"]=f["Type"]
            d["Mode"]=f["Mode"]
            d["Amount"]=f['Amount']
            d["CurrentBalance"]=f["CurrentBalance"]
            d["valueDate"]=f["valueDate"]  
            D[f['Txnid']]=d

        return D

    def SUMMA(df):
        d={}
        d["Type"]=df['summary.Type'][0]
        d["OpenDate"]=df["summary.openingDate"][0]
        d["Currency"]=df['summary.Currency'][0]
        d["BalanceDate"]=df['summary.balanceDateTime'][0][:len("2020-06-22")]
        d["CurrentBalance"]=df['summary.CurrentBalance'][0]
        d["Branch"]=df["summary.branch"][0]
        d["Staus"]=df['summary.Status'][0]
        return d
    
    def SUMMARY(df):
        summary={}
        summary["Type"]=df["profile.Account.fitype"][0]
        summary["Freq"]=df['summary.compoundingFrequency'][0]
        summary["tenure_days"]=df['summary.tenureDays'][0]
        summary["tenure_months"]=df['summary.tenureMonths'][0]
        summary["Interest"]=df["summary.interestRate"][0]
        summary["OpenDate"]=df['summary.openingDate'][0]
        summary["Principle"]=df['summary.principalAmount'][0]
        try:
            summary["RA"]=df['summary.recurringAmount'][0]
        except:
            print("")
        summary["EndDate"]=df["summary.maturityDate"][0]
        summary["InterestAmount"]=df["summary.interestOnMaturity"][0]
        summary["Current"]=df['summary.currentValue'][0]
        summary["MaturityAmount"]=df["summary.maturityAmount"][0]
        return summary

    def Profile(df):
        dick=df["profile.Holders.Holder"][0][0]
        dick["Account Number"]=df["profile.Account.number"][0]
        dick["Account Type"]=df["profile.Account.acctype"][0]
        dick["fitype"]=df["profile.Holders.type"][0]
        dick["IFSC"]=df["summary.ifsc"][0]
        try:
            dick["CurrentAmount"]=df['summary.currentValue'][0]
        except:
            dick["CurrentAmount"]=df['summary.CurrentBalance'][0]
        return dick
    
    def Trans(df):
        D={}
        for i in range(len(df['transactions'][0])):
            d={}
            f=df['transactions'][0][i]
            #d['Txnid']=f['Txnid']
            d['Amount']=f['Amount']
            d['Balance']=f['Balance']
            d['valueDate']=f['valueDate'][:len("2020-01-22")]
            try:
                d['TransactionsEndDate']=f['TransactionsEndDate']
            except:
                d["endDate"]=f['endDate']
            D[f['Txnid']]=d
        return D
    
    df1=pd.read_json(file_name)
    d={}
    A=pd.json_normalize(df1["accounts"][0])  ### Transact
    B=pd.json_normalize(df1["accounts"][1]) ####FD
    C=pd.json_normalize(df1["accounts"][2])
    D={}
    D["profile"]=Profile(A)
    D["summary"]=SUMMA(A)
    D["Details"]=Transaction(A)
    d["transactions"]=D
    D={}

    D["profile"]=Profile(B)
    D["summary"]=SUMMARY(B)
    D["Details"]=Trans(B)
    d["fixed"]=D
    D={}

    D["profile"]=Profile(C)
    D["summary"]=SUMMARY(C)
    D["Details"]=Trans(C)
    d["recurring"]=D
    return d


def pro(s):
    file_name=s+".json"
    z=send_json(file_name)
    D={}
    D['name']=z['transactions']['profile']['name']
    #D['dob']=z['transactions']['profile']['Dob']
    sa=z['transactions']['profile']['Dob']
    D['dob']=sa[:2]+"-"+sa[2:4]+"-"+sa[4:]
    D['mob']="+91 "+z['transactions']['profile']['mobile']
    D['email']=z['transactions']['profile']['email']
    D['AA']="1999999999@onemoney"
    D["status"]="Linked"
    return D

def fin(s):
    file_name=s+".json"
    z=send_json(file_name)
    D={}
    D["fix"]=float(z["fixed"]["summary"]["MaturityAmount"])
    D["rec"]=float(z["recurring"]["profile"]['CurrentAmount'])
    s=0
    ss=[]
    a=z["transactions"]['Details']
    for i in a:
        if a[i]['Type']=='CREDIT':
            s+=float(a[i]['Amount'])
            t=a[i]['valueDate'][5:7]
            if t not in ss:
                ss.append(t)
    D["avg"]=round(s/len(ss),2)
    D["cur"]=float(z["transactions"]["profile"]['CurrentAmount'])
    return D

def inv(s):
    file_name=s+".json"
    D={}
    z=send_json(file_name)
    D['no']=2
    D["amount"]=float(z['fixed']['profile']['CurrentAmount'])+float(z['recurring']['profile']['CurrentAmount'])
    return D
def trans(s):
    file_name=s+".json"
    z=send_json(file_name)
    z=z["transactions"]["Details"]
    a=[]
    b=[]
    D={}
    for i in z:
        a.append(float(z[i]["CurrentBalance"]))
        b.append(z[i]['valueDate'])

    D["amount"]=a
    D["date"]=b

    return  D
def typ(s):
    file_name=s+".json"
    z=send_json(file_name)
    z=z['transactions']['Details']
    D={}
    upi=0
    card=0
    atm=0
    other=0
    ft=0
    for i in z:
        f=z[i]['Mode']
        if f=="UPI":
            upi+=1
        if f=="CARD":
            card+=1
        if f=="ATM":
            atm+=1
        if f=="FT":
            ft+=1
        if f=="OTHERS" or f=="CARD":
            other+=1   

    D['data']=[upi,card,atm,ft,other]
    return D
def loan():
    D={}
    idx=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010]
    name=["Rashi Bank","Premium Bank Corp.","New Wealth Trust","IDIDI Bank","Premium Bank Corp.","IDIDI Bank","New Wealth Trust","Rashi Bank","Rashi Bank","New Wealth Trust"]
    amount=[50000,30000,5000,45000,80000,50000,5000,7000,12500,50000]
    duration=[6,4,1,1,5,8,3,2,3,12]
    ty=["Business","Personal","Business","Personal","Personal","Business","Personal","Business","Personal","Personal"]
    interest=[10,9,8,10,11,10,10,10.5,10,9.5]
    for i in range(10):
        d={}
        d["id"]=idx
        d["name"]=name
        d["amount"]=amount
        d["duration"]=duration
        d["type"]=ty
        d["interest"]=interest
    D=d   
    return D
def bank():
    
    D={}
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
        D[i]=d
    
    for i in D:
        return D[i]
def rashi():
    idx=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010]
    name=["Rashi Bank","Premium Bank Corp.","New Walth Trust","IDIDI Bank","Premium Bank Corp","IDIDI Bank","New Wealth Trust","Rashi Bank","Rashi Bank","New Wealth Trust"]
    amount=[50000,30000,5000,45000,80000,50000,5000,7000,12500,50000]
    duration=[6,4,1,1,5,8,3,2,3,12]
    ty=["Business","Personal","Business","Personal","Personal","Business","Personal","Business","Personal","Personal"]
    interest=[10,9,8,10,11,10,10,10.5,10,9.5]
    ix=[]
    n=[]
    a=[]
    d=[]
    t=[]
    inte=[]
    j=0
    for i in range(10):
        if name[i]=="Rashi Bank":
            ix.append(idx[i])
            n.append(name[i])
            a.append(amount[i])
            d.append(duration[i])
            t.append(ty[i])
            inte.append(interest[i])
    
    D={}
    D["id"]=ix
    D["name"]=n
    D["amount"]=a
    D["duration"]=d
    D["type"]=t
    D["interest"]=inte
    return D