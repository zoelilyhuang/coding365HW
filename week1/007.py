"""
a = int(input())
b = int(input())
c = int(input())
"""
"""
num = [int(input()),int(input()),int(input())] #書本數量
dis = [0,0,0]  #折扣
#pri = [380,1200,180]
"""
"""
if num[0] <= 0:
    dis[0] = 0
elif num[0] > 0 and num[0] <= 10:
    dis[0] = 1
elif num[0] >10 and num[0] <=20:
    dis[0] = 0.9
"""
"""
a = [int(input()),int(input()),int(input())] 
b = [0,0,0]
"""
"""
if num[0] <= 10 and num[0] >0 : #以書本A數決定折扣
    dis[0] = 1   #原價
elif num[0] <= 0 :
    dis[0] = 0  #若書本A數為負或0，折扣為0
elif num[0] > 10 and num[0] <= 20 :
    dis[0] = 0.9
elif num[0] > 20 and num[0] <= 30 :
    dis[0] = 0.85
elif num[0] > 30:
    dis[0] = 0.8

if num[1] <= 10 and num[1] >0 :  #書本B
    dis[1] = 1
elif num[1] <= 0 :
    dis[1] = 0
elif num[1] > 10 and num[1] <= 20 :
    dis[1] = 0.95
elif num[1] > 20 and num[1] <= 30 :
    dis[1] = 0.85
elif num[1] > 30:
    dis[1] = 0.8

if num[2] <= 10 and num[2] >0 :  #書本C
    dis[2] = 1
elif num[2] <= 0 :
    dis[2] = 0
elif num[2] > 10 and num[2] <= 20 :
    dis[2] = 0.85
elif num[2] > 20 and num[2] <= 30 :
    dis[2] = 0.8
elif num[2] > 30:
    dis[2] = 0.7

print('%.f' %(num[0]*dis[0]*380 + num[1]*dis[1]*1200 + num[2]*dis[2]*180)) #總價
"""
"""
print(int(num[0]*dis[0]*380 + num[1]*dis[1]*1200 + num[2]*dis[2]*180)) #總價
"""
#new
a = int(input())
b = int(input())
c = int(input())
mon = 0
if a >= 1 and a <=10:
    mon += a*380
elif a > 10 and a <=20:
    mon += a*380*0.9
elif a > 20 and a <= 30:
    mon += a*380*0.85
elif a > 30:
    mon += a*380*0.8

if b >= 1 and b <=10:
    mon += b*1200
elif b > 10 and b <=20:
    mon += b*1200*0.95
elif b > 20 and b <= 30:
    mon += b*1200*0.85
elif b > 30:
    mon += b*1200*0.8

if c >= 1 and c <=10:
    mon += c*180
elif c > 10 and c <=20:
    mon += c*180*0.85
elif c > 20 and c <= 30:
    mon += c*180*0.8
elif c > 30:
    mon += c*180*0.7

print(int(mon))