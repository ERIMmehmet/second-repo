liste = [11, 45, 8, 11, 23, 45, 23, 45, 89]

dic = dict().fromkeys(liste, 0) # atama gerekiyor key listeden value = 0 , 
{}.fromkeys(liste, 0)
print(dic)

for i in liste:  # 9 defa
    dic[i]+=1  # dic[i]= dic[i] + 1
print(dic)
