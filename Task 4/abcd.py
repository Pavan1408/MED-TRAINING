from Car import *
from veh import *
from Bike import *
import csv
import pandas as p
df=p.read_csv(r'vehipa.csv')
print(df)
fi=open('vehipa.csv')
c=csv.reader(fi)
header=[]
header=next(c)
print(header)
r=[]
t=0
m=0
di={}
tc={}
for row in c:
    r.append(row)
class LotManager:
    for i in range(4):
        di[r[i][0]]=[0]*10
        di[r[i][0]]=r[i][1:]
    print(di)
    def allo(self):
        p=int(input('aloocation:0 dealocation:1'))
        u=0
        v=0
        k=0
        m=0
        while(1):
            while(p==0):
                li=input("in which : :")
                k=k+1
                vn=input("enter vn:")
                win=input("enter in time")
                vehiname=input("   ")
                col=int(input("enter which column:"))
                u=(int(win[:2]))*60+(int(win[3:]))
                tc[k]=[vn,u,0]
                for i in range(4):
                    if li==r[i][0]:
                        if col<=5:
                            if vehiname=="car" and di[r[i][0]][col]=="free":
                                print("alocated at ",r[i][0],col)
                                di[li][col]=vn
                                df.iloc[i,col+1]=vn
                                df.to_csv('vehipa.csv',index=False)
                                print(df)
                                print(di)
                            else:
                                print("there is already vehiclle")
                        elif col>=6 and col<=8:
                            if vehiname=="bike" and di[r[i][0]][col]=="free":
                                print("alocated at ",r[i][0],col)
                                di[li][col]=vn
                                # df.loc[i,'car'+(str(col))]=vn
                                df.iloc[i,col+1]=vn
                                df.to_csv('vehipa.csv',index=False)
                                print(df)
                                print(di)
                            else:
                                print("there is already vehiclle")
                        else:
                            if vehiname=="bus" and di[r[i][0]][col]=="free":
                                print('alocated at ',r[i][0],col)
                                di[li][col]=vn
                                #
                                df.iloc[i,col+1]=vn
                                df.to_csv('vehipa.csv',index=False)
                                print(df)
                                print(di)
                            else:
                                print("there is already vehiclle")

                p=int(input())
            while(p==1):
                vn=input("enter vn:")
                wout=input("Enter Outime")
                t=0
                v=(int(wout[:2]))*60+(int(wout[3:]))
                for i in range(4):
                    for col in range(10):
                        for i in range(k):
                            if(vn==di[r[i][0]][col]):
                                m=m+1
                                di[r[i][0]][col]="free"
                                df.iloc[i,col+1]="free"
                                df.to_csv('vehipa.csv',index=False)
                                if(tc[k][0]==vn):
                                    tc[k][2]=v
                                    if((tc[k][2]-tc[k][1])<=60):
                                        t=20
                                    elif((tc[k][2]-tc[k][1])<=600):
                                        t=((((tc[k][2]-tc[k][1])-60)//60)*10)+20
                                    else:
                                        t=((((tc[k][2]-tc[k][1])-600)//60)*5)+110
                if(m==(4*10*k)):
                    print("no vehicl")
                print(t)
                print(di)
                p=int(input())
l=LotManager()
l.allo()