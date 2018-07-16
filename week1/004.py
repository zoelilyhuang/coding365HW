num = input()
num = num.split(' ')
for i in range(len(num)):
    num[i] = int(num[i])
#print(num)

num1 = num[0]
num2 = num[1]
num3 = num[2]

"""
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)
"""

def getTriangel(data1,data2,data3):  #建立function
    row_data = [data1,data2,data3]  #原始三個邊的數值
    sort_data = [0,0,0] #帶排序的list
    for i in range(len(sort_data)) : #排序
        for k in row_data :    
            if k >= sort_data[i] :
                sort_data[i] = k   #sort_data為排序好的三個邊，由大到小
        row_data.remove(sort_data[i])
    #print(sort_data)
    z = 0  #小於等於0的邊的數量
    for i in sort_data :
        if i <= 0 :
            z = z+1  #小於等於0的邊的數量
    if  sort_data[0] >= sort_data[1] + sort_data[2] or  z != 0:
        tri = 1
    elif sort_data[0] == sort_data[1] and sort_data[1] == sort_data[2]:
        tri = 2
    elif (sort_data[0] == sort_data[1] and sort_data[1] != sort_data[2] and sort_data[0]**2 + sort_data[1]**2 > sort_data[2]**2) or (sort_data[1] == sort_data[2] and sort_data[1] != sort_data[2] and sort_data[1]**2 + sort_data[2]**2 > sort_data[0]**2):
        tri = 3
    else:
        tri = 4

    return(tri)

print(getTriangel(num1,num2,num3))

        

