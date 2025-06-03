###################################Question number 3 hollow square##################################################
# n = int(input("number of cycle"))
# print("*"*n)
# for i in range(1,n-1):
#     print((" "*(n-2)).center(n,"*"))
# print("*"*n) 
# ###############################################################################################
# n = int(input("enter a number"))
# for i in range(1,n+1):
#     if i ==1 or i ==n:
#         print("*"*n)
#     else:
#         print(f"*{" "*(n-2)}*")
#################################question number 2 sum until stop###########################################################

# mainarr = [int(v) for v in iter(lambda: input("Enter value (or empty to stop): "), "stop")]
# print(sum(mainarr))

################################question number 1 lucky number###########################################################################################

# def luckynumber(n):
#     flag = False
#     if n % 7 == 0:
#         print("Lucky")
#         return     
#     piece = list(str(n))
#     flag = True if piece[-1] == "7" else False
#     print("Lucky") if flag else print("Not lucky")
# while True:
#     inp = int(input("enter a number"))
#     if inp==0:
#         break
#     luckynumber(inp)
#########################################validator question number 4################################################################################################

# def validator(input):
#     global flag
#     flag = False
#     input = list(str(input))
#     if len(input) <6:
#         return False
#     for element in input:
#         if element ==" ":
#             return False
#         elif element.isalnum():
#             flag = True
#     return flag
# print(validator(input("enter a password")))