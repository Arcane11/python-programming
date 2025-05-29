# question number 1 ############################################################

# n =  int(input("enter a number"))
# list = [x for x in range(1,n) if x % 5 ==0]
# print(list)

# question number 2 #####################################################

# n = 5
# for x in range(1,n+1):
#     print(f"{x}"*x)

# question number 3

# def collect_even(a):
#     str1 = ""
#     y = list(str(a)) 
#     for i in y:
#         if int(i) % 2 == 0:
#             str1 += (str(i))
#     if len(str1) == 0:
#         return 0
#     return str1 
# print(collect_even(input("enter a number")))
# 3
# def collect_even(a):
#     str2= ""
#     for i in str(a):
#         if int(i) % 2 == 0:
#             str2 += str(i)
#     if len(str2)==0:
#         return 0
#     return str2
# print(collect_even(int(input("enter a number"))))

# quesiton number 4##############################################

# def gcf(a,b):
#     factors_of_a = []
#     factors_of_b = []
#     for i in range(1,a+1):
#         if a % i == 0:
#             factors_of_a.append(i)
#     for j in range(1,b+1):
#         if b % j==0:
#             factors_of_b.append(j)
#     global gcf
#     gcf = 1
#     for x in factors_of_a:
#         for y in factors_of_b:
#             if x == y:
#                 gcf = x      
#     return (gcf)           
# print(gcf(120,24))

#question number 5

# n = 5  #int(input("enter a number"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(f" {i*j}" ,end="")
#     print()

