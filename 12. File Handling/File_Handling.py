#Create - x
file=open('Karan.txt','x')

#write - w
file=open('Karan.txt','w')
file.write("My Name is Karan")
#append - a
file=open('Karan.txt','a')
file.write(" Chrish")
#read - r
file=open('Karan.txt','r')
file.read()

# My Name is Karan Chrish

#Creating a text file
D = {}
D['name'] = input('Enter the Name :')
D['age'] = input('Enter Your Age :')
D['district'] = input("Enter Your District :")
print(D)
g = open('studentdata.txt','w')
g.write(str(D))
g = open('studentdata.txt','r')
g.readline()
g = open('studentdata.txt','a')
N = {}
N['name'] = input('Enter the Name :')
N['age'] = input('Enter Your Age :')
N['district'] = input("Enter Your District :")
print(N)
f = open('studentdata.txt','w')
f.write(str(N))
f = open('studentdata.txt','r')
f.readline()
f = open('studentdata.txt','a')
D = {}
D['name'] = input('Enter the Name :')
D['age'] = input('Enter Your Age :')
D['district'] = input("Enter Your District :")
print(D)
f = open('studentdata.txt','w')
f.write(str(D))
f = open('studentdata.txt','r')
f.readline()

''' 
Enter the Name :Karan
Enter Your Age :19
Enter Your District :KannyaKumari
{'name': 'Karan', 'age': '19', 'district': 'KannyaKumari'}
Enter the Name :Chrish
Enter Your Age :18
Enter Your District :Coimbatore
{'name': 'Chrish', 'age': '18', 'district': 'Coimbatore'}
Enter the Name :Karan Chrish
Enter Your Age :20
Enter Your District :Chennai
{'name': 'Karan Chrish', 'age': '20', 'district': 'Chennai'}
{'name': 'Karan Chrish', 'age': '20', 'district': 'Chennai'}
'''