fileWithPeople = open('people.csv','r',encoding = 'utf-8')

countM=0
countF=0

#for line in fileWithPeople:
    #mas = line.split(',')
    #for i in range (1,len(mas)):
    #    if i==1 or i==2 or i==3:
   #         countM+=int(mas[i])
  #      else:
 #           countF+= int(mas[i])
            
#if countM > countF:
  #  more=countM-countF
 #   print('Мужчин больше на', more)

#elif countF > countM:
  #  more=countF-countM
 #   print('Женщинин больше на', more)

#else:
 #   print (countM)
#    print (countF)





#region_num=[]
#region_name=[]
#for line in fileWithPeople:
   # mas = line.split(',')
  #  peaple=0
    #for x in range(1,len(mas)):
    #    peaple+=int(mas[x])
   # region_num.append(peaple)
  #  region_name.append(mas[0])
 #   print('В',mas[0],peaple,'людей')

#max_index=region_num.index(max(region_num))


#print(region_name[max_index])    

#fileWithPeople.close()

file_fios = open('fios.csv','r',encoding = 'utf-8')
new_file_fios = open('fios2.csv','w',encoding = 'utf-8')

import random
first_names = []
last_names = []
middle_names= []
for i in file_fios:
    mas = i.split(',')
    first_names.append(mas[0])
    last_names.append(mas[1])
    middle_names.append(mas[2])
num1 =int(input())

for i1 in range(num1):
    x=random.randint(0, 300)
    y=random.randint(0, 300)
    z=random.randint(0, 300)
    print(first_names[x])
    print(last_names[y])
    print(middle_names[z])
    new_file_fios.write(first_names[x]+ ' ' )
    new_file_fios.write(last_names[y]+' ')
    new_file_fios.write(middle_names[z])
new_file_fios.close()
file_fios.close()
