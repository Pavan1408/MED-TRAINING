from Car import *
from Bike import *
from Bus import *
from veh import *
import csv
from random import randrange
import datetime 
from datetime import date
from datetime import timedelta
import time
import pandas as p
df=p.read_csv(r'vehipa.csv')
print(df)
fi=open('vehipa.csv')
c=csv.reader(fi)
header=[]
header=next(c)
print(header)
zi=0
r=[]
t=0
k=0
m=0
di={}
tc={}
for row in c:
    r.append(row)
class LotManager:
    def __init__(self,vehiname,vn):
        self.vehiname=vehiname
        self.vn=vn
        if(self.vehiname=="car"):
            Car.__init__(self,vehiname,vn)
        elif(self.vehiname=="bike"):
            Bike.__init__(self,vehiname,vn)
        else:
            Bus.__init__(self,vehiname,vn)
    for i in range(4):
        di[r[i][0]]=[0]*10
        di[r[i][0]]=r[i][1:]
    print(di)
    def allo(self):
        v=0
        if(p==0):
            li=input("in which : :")
            col=int(input("enter which column:"))
            v = datetime.datetime.now()
            
            # intime= now.strftime("%H:%M")
            # v=(int(intime[:2]))*60+(int(intime[3:]))
            #v=(int(intime[:2]))*60+(int(intime[3:5]))
            for i in range(4):
                if li==r[i][0]:
                    if col<=5:
                        if self.vehiname=="car" and di[r[i][0]][col]=="free":
                            print("alocated at ",r[i][0],col)
                            di[li][col]=self.vn+":"+str(v)
                            df.iloc[i,col+1]="{}:{}".format(self.vn,v)
                            df.to_csv('vehipa.csv',index=False)
                            print(df)
                            print(di)
                        else:
                            print("there is already vehiclle")
                    elif col>=6 and col<=8:
                        if self.vehiname=="bike" and di[r[i][0]][col]=="free":
                            print("alocated at ",r[i][0],col)
                            di[li][col]=self.vn+":"+str(v)
                            df.iloc[i,col+1]=self.vn
                            df.to_csv('vehipa.csv',index=False)
                            print(df)
                            print(di)
                        else:
                            print("there is already vehiclle")
                    else:
                        if self.vehiname=="bus" and di[r[i][0]][col]=="free":
                            print('alocated at ',r[i][0],col)
                            di[li][col]=self.vn+":"+str(v)
                            df.iloc[i,col+1]=self.vn
                            df.to_csv('vehipa.csv',index=False)
                            print(df)
                            print(di)
                        else:
                            print("there is already vehiclle")
    def deal(self,vn):
        self.vn=vn
        if(p==1):
            m=0
            u=0
            peq=0
            t=0
            per="0"
            coun=0
            for i in range(4):
                for col in range(10):                        
                        coun=coun+1
                        if(self.vn==di[r[i][0]][col][:8]):
                            per=di[r[i][0]][col]
                            coun=coun-1                        
                            di[r[i][0]][col]="free"
                            df.iloc[i,col+1]="free"
                            df.to_csv('vehipa.csv',index=False)
                            #now = datetime.now()
                            # d1 = now.strftime("%H:%M:%S")
                            w= datetime.datetime.now()
                            #d2 = now.strftime("%H:%M")
                            # u=(int(d2[:2]))*60+(int(d2[3:]))
                            print(type(per),per[9:28])
                            v=datetime.datetime.strptime(per[9:28], "%Y-%m-%d %H:%M:%S")
                            #print(v)
                            #v=int(per)
                            m=w-v
                            if m.total_seconds()<=3600 and m.total_seconds()>=1800 :
                                t=20
                            elif m.total_seconds()<=39600 and m.total_seconds()>=3600 :
                                peq=m.total_seconds()//3600
                                t=20+(peq-1)*10
                            elif m.total_seconds()>39600: 
                                peq=m.total_seconds()//3600
                                t=110+(peq-11)*5
                            else:
                                t=0  
            if(coun==(4*10)):
                print("no vehicl")
            print(t)
            print(di)    
while(1):
    g=int(input("0 for exit: "))
    if(g==0):
        break
    p=int(input('aloocation:0 dealocation:1'))
    if(p==0):
        print("which vehicle: ")
        vehiname=input("   ")
        print("vehicle numer ")
        vn=input("enter vehicle numer")
        l=LotManager(vehiname,vn)
        l.allo()
    if(p==1) :
        vn=input("enter vn:")
        l=LotManager("a",vn)
        l.deal(vn)