"""
Alaa saeed Ahmed 20201023
Menna Mahmoud Sayed  20200560
"""
import random 
import matplotlib.pyplot as plt
#random.seed(10)
profit_list= list()
Demand= list()
purchase_price=50
sell_price=70
scrap_price=15
#Composite dis.
#1st Randomlly Generating number that decide the Newsday type
def RN_Newsday_Type():
    
     return  random.randint(1,100)
#2nd Randomlly Generating number that decide the distibution for a specific day type
def RN_Demand_Day():
    
     return random.randint(1,100)
'''
for i in range(1,21,1) :
  print ('random digits in day',i)
  DayType= RN_Newsday_Type()
  print('RD for Newsday Type:',DayType)
  demand= RN_Demand_Day()
  print('RD for demand :',demand)
  print('--------------------------------------------')
 '''

def get_Demand():
     
    DayType= RN_Newsday_Type()
   # print('RD for Newsday Type:',DayType)
    demand= RN_Demand_Day()
    #print('RD for demand :',demand)
    #1-Excellent Newsday type
    if DayType>= 1 and DayType<= 18:
    
        if demand>=1 and demand <7:
            Demand=50
        if demand>=8 and demand<15:
            Demand=60
        if demand>=16 and demand<27:
            Demand=70
        if demand>=28 and demand<40 :
            Demand=80
        if demand>=41 and demand<62:
            Demand=90
        if demand>=63 and demand<85:
            Demand=100
        if demand>=86 and demand<93:
            Demand=110
        if demand>=94 and demand<100:
            Demand=110
        else:
            Demand=120


   #2-Good Newsday type
    elif DayType>= 19 and DayType<= 60:
       if demand>=1 and demand<6:
           Demand=40
       if demand>=7 and demand<15:
           Demand=50
       if demand>=16 and demand<31:
           Demand=60
       if demand>=32 and demand< 50:
           Demand=70
       if demand>=51 and demand<78:
           Demand=80
       if demand>=79 and demand<90:
           Demand=90
       if demand>=91 and demand<97:
           Demand=100         
       else:
           Demand=110
           
    #3-Fair Newsday type
    elif DayType>= 61 and DayType<= 92:
         if demand>=1 and demand<15:
             Demand=40
         if demand>=16 and demand<37:
             Demand=50
         if demand>=38 and demand<65:
             Demand=60
         if demand>=66 and demand< 83:
             Demand=70
         if demand>=84 and demand<93:
             Demand=80
         if demand>=94 and demand<98:
             Demand=90
         else:
             Demand=100
             
    #4-Poor Newsday type
    else:
        if demand>=1 and demand<42:
            Demand=40
        if demand>=43 and demand<70:
            Demand=50
        if demand>=71 and demand<84:
            Demand=60
        if demand>=85 and demand< 94:
            Demand=70
        if demand>=95 and demand<99:
            Demand=80
        else:
            Demand=90
    return Demand
    

for i in range (10) :      
    Demand.append(get_Demand())

Avg_Prof_40=0
Avg_Prof_60=0 
Avg_Prof_80=0
Avg_Prof_90=0 
Avg_Prof_100=0
Avg_Prof_120=0 
     
#for i in range(start,stop,step)
for bundles in range (40,120,20):
    for Day in range (10) :  
   
        #In case demand less than Available_Papers/ bundles
        if Demand[Day]< bundles :
            sold = Demand[Day]
            bundles -= Demand[Day]
            scrap=bundles 
            lost_opp=0

        #In case demand bigger than Available_Papers
        elif Demand[Day] > bundles :
            sold = bundles
            scrap=0
            lost_opp=(Demand[Day]-sold)

        #In case demand equal Available_Papers
        else :
            sold = Demand[Day]
            bundles = 0
            scrap=0
            lost_opp = 0
        profit = ((sold *sell_price) - (sold * purchase_price) +(scrap * scrap_price) - (lost_opp * (sell_price-purchase_price)))/100 #20 is the pure revenue 70(sell)-50(cost) =20
        
    
        if profit >= 0 :
            profit_list.append(profit)
            #print (profit_list)
            
            plt.hist(profit_list)
            plt.title("profit ")
            plt.xlabel("profit")
            plt.ylabel("trials")
            plt.show()
            
    
    if bundles == 40:
        Avg_Prof_40 = sum(profit_list) / 10
       # print(" 40 bundle",Avg_Prof_40)
        profit_list.clear()
    elif bundles == 60:
        Avg_Prof_60 = sum(profit_list) / 10
        #print(" 60 bundle",Avg_Prof_60)
        profit_list.clear()
    elif bundles == 80:
        Avg_Prof_80 = sum(profit_list) / 10
       # print(" 80 bundle",Avg_Prof_80)
        profit_list.clear()
   
    else :
        Avg_Prof_100 = sum(profit_list) / 10
       # print(" 100 bundle",Avg_Prof_100)
        profit_list.clear()
        Avg_Prof_120 = sum(profit_list) / 10
        #print(" 120 bundle",Avg_Prof_120)
        profit_list.clear()
#Comparison
if Avg_Prof_40 > Avg_Prof_60 and Avg_Prof_40 > Avg_Prof_80 and Avg_Prof_40 > Avg_Prof_100 and Avg_Prof_40 > Avg_Prof_120:
    print("Seller must order 40 bundle")
elif Avg_Prof_60 > Avg_Prof_40 and Avg_Prof_60 > Avg_Prof_80 and Avg_Prof_60 > Avg_Prof_100 and Avg_Prof_60 > Avg_Prof_120:
    print("Seller must order 60 bundle")
elif Avg_Prof_80 > Avg_Prof_40 and Avg_Prof_80 > Avg_Prof_60 and Avg_Prof_80 > Avg_Prof_100 and Avg_Prof_80 > Avg_Prof_120:
    print("Seller must order 80 bundle")
elif Avg_Prof_100 > Avg_Prof_40 and Avg_Prof_100 > Avg_Prof_60 and Avg_Prof_100 > Avg_Prof_80 and Avg_Prof_100 > Avg_Prof_120:
    print("Seller must order 100 bundle")
elif Avg_Prof_120 > Avg_Prof_40 and Avg_Prof_120 > Avg_Prof_60 and Avg_Prof_120 > Avg_Prof_80 and Avg_Prof_120 > Avg_Prof_100:
    print("Seller must order 120 bundle")
