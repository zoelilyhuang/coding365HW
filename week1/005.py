
data = input()
data = data.split(' ')
for i in range(len(data)):
    data[i] = int(data[i])
"""
data = [] #建立空list
for i in range(5):  #將資料輸入
    i = input()
    i = float(i)
    data.append(i) #將資料加入list中
"""
datasum = sum(data)/5*100   #算總和，乘100取整數再除100
datasum = int(datasum)/100
print("%.2f" % datasum)

var = 0
for k in data:
    var = var + (k-datasum)**2   #計算變異數
var = var/5
dev = var**0.5 #計算標準差

var = var*100
var = int(var)/100
print("%.2f" % var)

dev = dev*100  #計算標準差
dev = int(dev)/100
print("%.2f" % dev)
