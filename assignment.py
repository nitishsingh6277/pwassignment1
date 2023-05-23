        #Q1
s1 = 'newton'
list1= [1, 3, 'hero', 4+89j, 45.678, {1,2,4,5}]
float1 = 45.678
tuple1 = (3, 5, 8, 'newton', )
print(tuple1)

#Q2
var1= ''
var2 = '[Ds, ML, python]'
var3 = ['DS', 'ML', 'Python']
var4 = 1.
print(type(var1))
print(type(var2))
print(type(var3))
print(type(var4))

#Q3:
values = 10/4
print(values, 'values after diving 10 by 4')

values2 = 10 %4
print(values2, 'so after diving 10 by 4 then reminder will be the output')
values3 = 10//4
print(values3, 'floor values when 10 is divided by 4 then float values comes up them lowest whole integral values of that floor will be returned..')
values4 = 2**3
print(values4, 'here we have the exponentiation of 2 to the power 3')

#Q4:
list1 = [1, 3, 4, 7, 8, 3.456, 7.89, 7+8j, (3,5,7.5, 8+8j), {3,5,7}, {'key': 45, 'key2':67}]
print(list1)

for i in list1:
    print(i, type(i))


#Q5
A = 100
B = 10
count = 0
temp1 = A
temp2 = B
while(temp1 > 0):
    temp1 = temp1 % temp2
if(temp1 == 0):
    print(A/B)

#Q6:

list2 = [3, 6, 8, 14, 17, 32, 76574, 4, 9, 8776, 123, 354, 4765, 364, 346, 4325, 325, 2532, 253, 253, 345, 535, 25323, 3253, 65456, 2352, 32424, 23432]
for values in list2:
    if(values % 3 == 0):
        print('divisible by 3')
    else:
        print('not divisible by 3')
#Q7
# MUtable data types are like its values at the index can be changed like in case of list we can change the values at particular index... 
list3 = [1, 5, 5+7j, 'hero']
list3[3] = 'sude' #here we are making the changes at index 3 from complex to string values.. so its mutable data type...
#immutable data types are like its index can't be values can't be edited.. like in case of tuples we see.
tuplese1 = (1, 4, 50)
#if we try to change tuples values like tuples1[2] = 34 then its will give error like asssignment not alloweed so its index values can't be changed..
#this is immutable objects
#likewise string is also immutable object.. 



