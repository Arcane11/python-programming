import math
import sys
import copy
# import this
# print(7/0) # division by zero error
# print(7//0) # interger division by zero error
# print(7%0)  # integer modulo by zero error
# print(7/2)
# print(7//2)
# print(type(1.0)==type(1)) # false
# print(-10//-3)
# print(7/-4)
# print(-7/4)
# print(7%4)
# print(5%5)
# print(8%-4)
# print(7%(-4))
# print(-7%4)
# print(-7%-4)
# print(10%-3)
# print(10//-3)
###################################
# # challenge 1
# price = int(100)
# n = int(7)
# t=int(12) # since there are 12 months in a year
# rate =0.1
# formula = float((1 + (rate /n)) ** (t*n))
# print(price*formula)  

####################################
# *****
# ****
# ***
# **
# *

# for i in range(0,1):
#     for j in range(5,0,-1):
#         print("*"*j)

# or

# n = int(input("numbner of cycles"))
# for i in range(n, 0, -1):
#   print('*'*i)
 

        
#####################################
# *
# **
# ***
# ****
# *****
# n=6
# for i in range(0,1):
#     for j in range(0,n):
#         print("*"*j)

#or

# n = 5
# for i in range(n+1):
#   for j in range(1, i + 1):
#     print("*", end = '')
#   print() 


# or

# n = 5
# for i in range(n):
#     final1=''
#     for j in range(n):
#         if(j>i):
#             final1+=""
#         else:
#             final1+= "*"
#     print(final1)
    
######################################
# n = 5
# for i in range(n):
#     final2=''
#     for j in range(n):
#         if j>=i:
#             final2 +="* "
#         else:
#             final2 += " " # you can change the angle of the central triangle by editing the space in these string
#     print(final2)
    
###################################### triangle(decreasing)
# b=int(input("number of cycles"))
# for i in range(b):
#     count=0
#     arr3=[]
#     for j in range(b):
#         arr3.append("*")
#     while count != i:
#         arr3.remove("*"),arr3.insert(0," "),arr3.pop()
#         count +=1
#         if arr3.count("*")<=2:
#             break              
#     final3 = ' '.join(arr3)
#     print(final3)
#     if(arr3.count("*")<=2):
#         break  

# ########################################## triangle (increasing)
# b= int(input("number of cycle"))
# for i in range(b):
#     count=math.ceil(((b-2*i)/2)-1) 
#     # print(count)
#     if count < 0:
#         break
#     arr4=[]
#     for j in range(b):
#         arr4.append("*")
#     while count > 0:
#         arr4.remove("*") 
#         arr4.pop(-1)
#         arr4.insert(0," ")
#         count -= 1    
#     final4=" ".join(arr4)
#     print(final4)
    
#####################################triangle simplified(decreasing)

# x = 11
# y = 0
# while x > 0:
#     print(" "*y + "* "*x)
#     x -= 2
#     y += 2 

#####################################triangle simplified(increasing)

# x = int(input("number of cycle"))
# y = 0
# while x > 0:
#     if x % 2 != 0:
#         print(" "*(x-1) + "* "*(y+1))
#     else:
#         print(" "*(x-2) + "* "*(y+2))
#     x-=2
#     y+=2
    
    
# or



# x = int(input("number of cycle"))
# y = (x-1)//2 * 2
# z = 2 - x % 2
# while x >= z:
#     print(" " * y + "* " * z)
#     z += 2
#     y -= 2


# or 

# x = int(input("number of cycle"))
# y = 2 - x % 2
# while x>0:
#     print(" "*(x-1) + "* "*y)
#     x-=2
#     y+=2

# or

# n = 6
# for i in range(1, n + 1):
#  print(' ' * (n - i)+'* ' * i)

# or 

# n =  int(input("number of cycles"))
# for i in range(2-n%2,n+2,2):
#     print(("*"*i).center(n," "))
############################################# code I (triangles)


# rows = int(input("number of cycle"))
# for i in range(rows):
#     print(" " * (rows - i - 1) + "* " * (i + 1))
    
# rows = 7
# for i in range(rows):
#     print(" " * (i ) + "* " * (rows - i))    
    
##############################################pyramid 
# count=0
# x = int(input("number of cycle"))
# y=w= 2 - x % 2
# z=x
# while (z>0) or (x>0):
#     count+=1
#     if x > 0:
#         print(" "*(x) + "* "*y)
#         x-=2
#         y+=2
#     else:
#         print(" "*w + "* "*z)
#         z-=2
#         w+=2
# print(count)
############################################ pyramid minimised

# x = int(input("number of cycles: "))
# y = (x-1)//2 * 2
# z = 2 - x % 2
# a = y
# count = 0
# while y < x:
#     count +=1
#     print(" " * y + "* " * z)
#     a -= 2
#     y = y - 2 if a >= 0 else y + 2
#     z = z + 2 if a >= 0 else z - 2
# print(count)
#############################################                   RANDOM CODES 102
# w = ""
# x =11
# x1 = 11.0
# a=5
# y=-0
# x = ''' this is a 'multi'
# line string
#                 aint this amazing brother
#                 bro it can also have single or double" quote in it'''
# z = 53j # only J is considered as a complex number
# # print((y or a)>0)
# # print(bool(y))
# # print(type(z))

# string1= '''A backslash character in \na string indicates that one or more\t characters that follow \\\\\ it should be treated\b specially. (This is referred to as an escape sequence, because the\f backslash causes the subsequent character sequence to “escape”\r its usual meaning.)
 # '''
# print(string1)
# print(not {}) ## true
# print( x is x1) ### false
# grades = [98, 76, 71, 87, 83, 90, 57, 79, 82, 94]
# print(sum(grades)/len(grades))
# x=[1,2,3,4,5]
# x1=sum(x[0:3])
# print(x1)
#######################################
       
# n = 5 
# count=0
# for i in range(n*2-1):
#  count+=1   . 
#  # Print leading spaces 
#  for j in range(abs(n - i - 1)):
#    count+=1
#    print(' ', end=' ')
#  # Print asterisks
#  for k in range(n - abs(n - i - 1)):
#    count+=1
#    print('*', end=' ')
#  print()


# x = {}
# z = ()
# print(type(x))
# print(type(z))
# print(5&3) 
# 0101
# 0011 


##############################################weekdate distunguisher
# day = input("Enter the day: ")
# match day:
#   case "Mon" | "Tue" | "Wed" | "Thu" | "Fri":
#     print("It's a weekday")
#   case "Sat" | "Sun":
#     print("It's a weekend")
#   case _:
#     print("Invalid day")

##################################################string basic operations

# str1 =  str.lower("I'M GOING TO CHANGE THIS TO LOWER CASE.")
# str2=str1.upper()
# str3=str2.capitalize()
# str4=str3.casefold()
# str5=str4.center(50,"*")
# str6=str5.count("i'm",20,30) # string, start, end
# str7=str1.endswith("i",0,1)
# str8=str5.find("i'm")
# str9=str5.index("i'm") # find and index are the same thing
# str10=str5.partition("e")
# str11=str5.swapcase()
# str12=str5.split("e",8)
# str13=str5.upper()
# str14=list(str13)
# str15=str13
# print(str1)
# print(str2)
# print(str3)
# print(str4)
# print(str5)
# print(str6)
# print(str7)
# print(str8)
# print(str9)
# print(str10)
# print(str11)
# print(str12)
# print(str13)
# print(str14)

####################################################### number basic operation

# x = 222
# y = 40
# x1 = x.__invert__()
# y1=y.__gt__(4)
# # x2 = x1.bit_length()
# x3 = x.__and__(77)
# x4=x1.__abs__()
# x5=x1.__eq__(67)
# print(x1)
# # print(x2)
# print(x3,x4)
# print(x5)
# print(y1)

########################################## half pyramid(right handed)

# m=int(input("number of cycle"))
# for i in range(1,m*2+1):
#     print(" "*abs(m-i),end="")
#     print("*"*abs(i)) if i<=m else print("*"*(m*2-i))

########################################## half pyramid(left handed)

# m=int(input("number of cycle "))
# for i in range(1,m*2+1):
#     print("*"*i) if i<m else print("*"*abs(m*2-i))

##########################################################################################################################################################################################################
 

#########################################################################################################################################################################################################

# data1 = {
#     "key1": 1,
#     "key2": 2,
#     "key3": 3
# }
# print(data1.get("key1"))
# print(data1.items())
# data1.pop("key2")
# data1.popitem()
# print(data1)


###################################################################################################################################################class quiz

# #1
# a=1 
# n = int(input("enter a number"))
# for i in range(1,n+1):
#     a*=i
# print(f"factorial of {n} is ",a)

# #2
# n=5
# for i in range(n+1):
#     print(f"{i}"*i)
#     n-=1


##############################################################################################################################################################################################################################################################################################################################################################################################################################

# Prime number upto n

# a = int(input("number of cycle."))
# prime = []
# for i in range(2,a):
#     for j in range(2,i):
#         if i == j + 1 and i % j != 0:
#             prime.append(i)
#         elif i % j == 0:
#             break

#####################################################################################################################################

# number divisible by 9

# n = 100
# stack = []
# while n > 1:
#     if n % 9 == 0:
#         stack.append(n)
#     n-=1
# stack.sort()
# print(stack)


################## array.sort()   sorts the array in ascending order then returns none as a result


#########################################################################################################################################
                                                    # properties of loop and dictionary and lambda and function
                                                    # how to add tuple and operation on tuples and set
                                                    # time complexity

#####################################################################################################################################
# greet  = lambda : print("hello")
# greet()
# def hello():
#     print("hi Joe")

dict = {
    "key1" : "value1",
    "key2" : "value2",
    "key3" : "value3",
    "key4" : "value4",
    "key5" : "value5"
}
# x =5
# if not(x):
#     print(1)
# print(len(dict))

# print(dict)
# print(dict.get("key1"))
# print(dict.values())
# print(dict.items())
# print(dict.)




# for i,j in dict.items():
#     print(i,j)
    
# def list_element(*x):
#     return x
# print(list_element(2, 4, 6,8,10,12,14))
####################################################################################################################################### fanos code simplified

# n = 6
# for i in range(0,n*2+1,2):
#     print(" "*(n-abs(n-i)) + "* "*abs(n-i))


###################################################################################################################################

# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

#  n - abs(n-i)         operates as a function which increases to certain level and comes to decrease
# n = 6
# for i in range(0,n*2,2):
#     print("* "*(n-abs(n-i)))

#################################################################################################################################

# factorial recursion

# def factorial_recursion(n):
#     if n==1:
#         return 1
#     else:
#         return n*factorial_recursion(n-1)
# print(factorial_recursion(int(input("enter a number."))))

###################################################################################################################################

# fibonacci_sample = [0,1,1,2,3,5,8,13,21,34,55,89]0th term, first term, second term

# def fibonacci_recursion(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci_recursion(n-1)+fibonacci_recursion(n-2)
# print(fibonacci_recursion(3))

########################################################################################################################################

# zeroSumSlice

# def zerosumslice(array):
#     i=0
#     while i<len(array)-1:
#         for j in range(i+1,len(array)):
#             if sum(array[i:j]) == 0:
#                 print (array[i:j])
#         i+=1
# print(zerosumslice([1,2,3,-2,-3,5,-3,-2,3]))

###################################################################################################

            ##CIPHERING##
       
# initial = "nkq qtljsu suwkltq li u wldkqh aqylwq aqyqmxdqa uta oiqa lt nkq quhmp- nx sla-20nk wqtnohp nx dhxnqwn wxssqhwlum, aldmxsunlw, uta slmlnuhp wxssotlwunlxt. ln bui qsdmxpqa qcnqtilyqmp vp tuzl jqhsutp aohltj bxhma buh ll, lt umm vhutwkqi xr nkq jqhsut slmlnuhp. nkq qtljsu suwkltq bui wxtilaqhqa ix iqwohq nkun ln bui oiqa nx qtwldkqh nkq sxin nxd-iqwhqn sqiiujqi."
# final = ''
# d = {
#     "a" : "d",
#     "b" : "w",
#     "c" : "x",
#     "d" : "p",
#     "e" : "q",
#     "f" : "j",
#     "g" : "k",
#     "h" : "r",
#     "i" : "s",
#     "j" : "g",
#     "k" : "h",
#     "l" : "i",
#     "m" : "l",
#     "n" : "t",
#     "o" : "u",
#     "p" : "y",
#     "q" : "e",
#     "r" : "f",
#     "s" : "m",
#     "t" : "n",
#     "u" : "a",
#     "v" : "b",
#     "w" : "c",
#     "x" : "o",
#     "y" : "v",
#     "z" : "z",
# }

# for i in range(len(initial)):
#     ind = initial[i]
#     if not(ind.isalpha()):
#         final += ind
#         continue
#     final += d[ind]
# print(final)


initial = '''hvionewvmoai ovcev ne nay qebyvk mwy xml yddyhnctysi likekiqepl xcna ykhvioncek, nay hektyvlcek ed ckdevqmncek dveq m vymbmjsy lnmny ne moomvykn keklykly. nay evcwckmnev ed mk ykhvionyb qyllmwy lamvyl nay byhebckw nyhakcupy eksi xcna cknykbyb vyhcocyknl ne ovyhspby mhhyll dveq mbtyvlmvcyl. nay hvionewvmoai scnyvmnpvy ednyk plyl nay kmqyl mschy dev nay lykbyv, jej dev nay cknykbyb vyhcocykn, mkb yty dev nay mbtyvlmvi. lckhy nay bytyseoqykn ed venev hcoayv qmhackyl ck xevsb xmv eky mkb nay mbtykn ed heqopnyvl ck xevsb xmv nxe, nay qynaebl plyb ne hmvvi epn hvionesewi amty jyheqy ckhvymlckwsi heqosyr mkb cnl mooschmncek qevy xcbylovymb.

qebyvk hvionewvmoai cl aymtcsi jmlyb ek qmnayqmnchms nayevi mkb heqopnyv lhcykhy ovmhnchy; hvionewvmoach mswevcnaql mvy bylcwkyb mvepkb heqopnmncekms amvbkyll mllpqoncekl, qmzckw lpha mswevcnaql amvb ne jvymz ck ovmhnchy ji mki mbtyvlmvi. cn cl nayevynchmssi oellcjsy ne jvymz lpha m lilnyq, jpn cn cl ckdymlcjsy ne be le ji mki zkexk ovmhnchms qymkl. nayly lhayqyl mvy nayvydevy nyvqyb heqopnmncekmssi lyhpvy; nayevynchms mbtmkhyl, dev yrmqosy, cqovetyqyknl ck cknywyv dmhnevcfmncek mswevcnaql, mkb dmlnyv heqopnckw nyhakesewi vyupcvy nayly lespncekl ne jy heknckpmssi mbmonyb. nayvy yrcln ckdevqmncek-nayevynchmssi lyhpvy lhayqyl namn ovetmjsi hmkken jy jvezyk ytyk xcna pkscqcnyb heqopnckw oexyv. mk yrmqosy cl nay eky-ncqy omb, jpn nayly lhayqyl mvy qevy bcddchpsn ne ply ck ovmhnchy namk nay jyln nayevynchmssi jvymzmjsy jpn heqopnmncekmssi lyhpvy qyhamkclql.

nay wvexna ed hvionewvmoach nyhakesewi aml vmclyb m kpqjyv ed sywms cllpyl ck nay ckdevqmncek mwy. nay oenykncms ed hvionewvmoai dev ply ml m nees dev ylocekmwy mkb lybcncek aml syb qmki wetyvkqyknl ne hsmllcdi cn ml m xymoek mkb ne scqcn ev ytyk oveacjcn cnl ply mkb yroevn. ck leqy gpvclbchncekl xayvy nay ply ed hvionewvmoai cl sywms, smxl oyvqcn cktylncwmnevl ne heqoys nay bclhselpvy ed ykhvioncek zyil dev behpqyknl vysytmkn ne mk cktylncwmncek. hvionewvmoai msle osmil m qmgev vesy ck bcwcnms vcwanl qmkmwyqykn mkb heoivcwan ckdvckwyqykn ed bcwcnms qybcm.
'''
processed = ''''''
final = ''
arr = [x for x in initial if x.isalpha()]
# print(arr)
dict = {
}
count = len(arr)
for i in arr:
    if not(dict.get(i)):
        dict[i] = 1/count
    else:
        dict[i] += 1/count
# print(dict)
sorted_dict_value = sorted(dict.values())
print(sorted_dict_value)
alpha = 'zqxjkvbpygfwmucldrhsnioate' # from the web
dict2 = {
    
}
for i in range(len(sorted_dict_value)):
    sr = sorted_dict_value[i]
    # print("sr",sr)
    # for j in range(len(sorted_dict_value)):
    #     alp = dict[alpha[j]]
    #     print("alp",alp)
        # if sr==alp:
        #     dict2[alpha[i]] = dict[sr]
        #     continue