
a = [int(input()),int(input()),int(input())]
if a[1] == 2:
    a.append(int(input()))
    if a[2] > a[3]:
        a[2],a[3] = a[3],a[2]
b = [int(input()),int(input()),int(input())]
if b[1] == 2:
    b.append(int(input()))
    if b[2] > b[3]:
        b[2],b[3] = b[3],b[2]
c = [int(input()),int(input()),int(input())]
if c[1] == 2:
    c.append(int(input()))
    if c[2] > c[3]:
        c[2],c[3] = c[3],c[2]

"""
co = [a[0],b[0],c[0]]
hr = [a[1],b[1],c[1]]
"""

ch = [a,b,c]
er = 0
for k in ch :
    if k[0] > 9999 or k[0] < 1000:
        er += 1 
    if k[1] != 1 and k[1] != 2:
        er += 1
    if int(k[2]/10) < 1 or int(k[2]/10) > 5:
        er += 1
    if k[2] - (int(k[2]/10))*10 < 1 or k[2] - (int(k[2]/10))*10 > 8:
        er += 1
    if k[1] == 2:
        if int(k[3]/10) < 1 or  int(k[3]/10) > 5:
            er += 1
        if k[3] - (int(k[3]/10))*10 < 1 or k[3] - (int(k[3]/10))*10 > 8:
            er += 1
co = 0

if er != 0:
    print('-1')
else:
    if c[0] < b[0]:
        c,b = b,c
    if b[0] < a[0]:
        b,a = a,b
    if c[0] < b[0]:
        c,b = b,c
    for i in range(a[1]):
        for g in range(b[1]):
            if a[i+2] == b[g+2]:
                print(str(a[0]) + ',' + str(b[0]) + ',' + str(a[i+2]))
                co += 1
        for h in range(c[1]):
            if a[i+2] == c[h+2]:
                print(str(a[0]) + ',' + str(c[0]) + ',' + str(a[i+2]))
                co += 1
    for t in range(b[1]):
        for r in range(c[1]):
            if b[t+2] == c[r+2]:
                print(str(b[0]) + ',' + str(c[0]) + ',' + str(b[i+2]))
                co += 1
    if co == 0:
        print('correct')

         



"""
a = [1,2,3]
b = [3,2,5]
s = a & b
print(s)
"""