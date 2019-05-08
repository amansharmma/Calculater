import arthmetic
from arthmetic import add
from arthmetic import subtrect
from arthmetic import multiply
from arthmetic import divizan
from arthmetic import modul
from arthmetic import sqer
from arthmetic import qube
print ("1. addition \n2. subtrection \n3. multiplication \n4. divide \n5. modulus \n6. sqere \n7. queb")
inp = str(raw_input("what do you want :- "))
if (inp == "addition"):
	x = add(int(input("Enter the 1st number :- ")) , int(input("Enter the 2nd number :- ")))
	print "your ans is that ---> ",(x)
elif (inp == "subtrection"):
	x = subtrect(int(input("Enter the 1st number :- ")) , int(input("Enter the 2nd number :- ")))
	print "your ans is that ---> ",(x)
elif (inp == "multiplication"):
	x = multiply(int(input("Enter the 1st number :- ")) , int(input("Enter the 2nd number :- ")))
	print "your ans is that ---> ",(x)
elif (inp == "divide"):
	x = divizan(int(input("Enter the 1st number :- ")) , int(input("Enter the 2nd number :- ")))
	print "your ans is that ---> ",(x)
elif (inp == "modulus"):
	x = modul(int(input("Enter the 1st number :- ")) , int(input("Enter the 2nd number :- ")))
	print "your ans is that ---> ",(x)
elif (inp == "sqere"):
	x = sqer(int(input("Enter the number :- ")))
	print "your ans is that ---> ",(x)	
elif (inp == "queb"):
	x = qube(int(input("Enter the number :- ")))
	print "your ans is that ---> ",(x)
else:
	print "wrong choice"		