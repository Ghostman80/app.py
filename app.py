import sys
import datetime
import calendar
print("Python version") #system version
print(sys.version)
print("Version info.")
print(sys.version_info)

now = datetime.datetime.now() # Date and time.
print("Current date and time : ")
print(now.strftime("%Y-%m-%d %H:%M:%S"))

fname = input("Input first name... ")
lname = input("Input your last name... ")
print ("Hello " + fname + " " + lname)

values = input("2, 7, 23, 15, 24")
list = values.split(",")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)

filename = input("abc.java ")
f_extns = filename.split(".")
print("The extension of this file is : " +
      repr(f_extns[-1]))

color_list = ["Red", "Green", "White" ,"Black"]
print( "%s %s"%(color_list[0],color_list[-1]))

exam_st_date = (11,12,2014)
print( "The examination will start from : %i / %i / %i"%exam_st_date)

a = int(input("Input an integer : "))
n1 = int("%s" % a)
n2 = int("%s%s" % (a,a))
n3 = int("%s%s%s" % (a,a,a))
print(n1+n2+n3)

y = int(input("Input the year : "))
m = int(input("Input the month : "))
print(calendar.month(y, m))

print(""" 
a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string ---------------> example
""")

from datetime import date # Calculate date and time. From a calendar. 
f_date = date(2014, 7, 2)
l_date = date(2014, 7, 11)
delta = l_date - f_date
print(delta.days)

# Volume of sphere with raidus of 6
pi = 3.1415926535897931
r = 6.0
V = 4.0/3.0*pi* r**3
print('The volume of the sphere is: ',V)

#Get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.
def difference(n):
    if n <= 17:
        return 17 - n
    else:
        return (n - 17) * 2

print(difference(22))
print(difference(14))

def near_thousand(n):
    return((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))
print(near_thousand(1000))
print(near_thousand(900))
print(near_thousand(800))
print(near_thousand(2200))

def sum_thrice(x, y, z):

    sum = x + y + z

    if x == y == z:
        sum = sum * 3
    return sum
print(sum_thrice(1, 2, 3))
print(sum_thrice(3, 3, 3))

def histogram( items ): # displaying the amount of astericks a certain number.
    for n in items:
        output = ''
        times = n
        while( times > 0 ):
            output += '*'
            times = times - 1
        print(output)

histogram([20, 32, 6, 10])

color_list_1 = set(["White", "Black", "Red"]) # print a list of color.
color_list_2 = set(["Red", "Green"])
print("Original set elements:")
print(color_list_1)
print(color_list_2)
print("\nDifference of color_list_1 and color_list_2:")
print(color_list_1.difference(color_list_2))
print("\nDifference of color_list_2 and color_list_1:")
print(color_list_2.difference(color_list_1))

def test_distinct(data):
    if len(data) == len(set(data)):
        return True
    else:
        return False;
print(test_distinct([1,5,7,9]))
print(test_distinct([2,4,5,5,7,9]))


input("End Program.. ")




    
