import math
num1 = input() #輸入數值1
num2 = input() #輸入數值2
num1 = float(num1) #轉浮點數
num2 = float(num2) #轉浮點數
sum_num12 = int((num1+num2)*100) #計算sum後，乘100取整數
print('Sum:%.2f' % (sum_num12/100)) #除100後取到小數點後第二位
dif = int(abs(num1-num2)*100)
print('Difference:%.2f' % (dif/100))
pro = int(num1*num2*100)
print('Product:%.2f' % (pro/100))
quo = int(num1/num2*100)
print('Quotient:%.2f' % (quo/100))