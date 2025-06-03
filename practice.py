# from collections import deque
# # list operations
# a=[1,2,3]
# b=[2,3,4,5,6,7 ,8,8,9,10,11]
# c=[14,49,58,72,96]
# a[:len(a)]=[9,5,4]
# a[len(a):]=[7,4,6,2,3,1,8,9,10,11,12,4,13,18]# same as append
# print(a)
# print(a.count(5))
# print(a.index(4,5))
# a.extend(b)
# a.insert(0,c)
# a.remove(5)
# a.pop(0)
# d=a.copy()
# print(a)
# e=c.reverse()
# print(e)
# array = ["one","two","three","four","five","six","seven","eight"]
# queue=deque(array)
# queue.append("nine")
# queue.append("ten")
# queue.popleft()
# queue.popleft()
# print(queue)
# squares = list(map(lambda x: x**2, range(10)))
# print(squares)
# arr=[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
# print(arr)
# vec = [-4, -2, 0, 2, 4]
# # apply a function to all the elements
# [abs(x) for x in vec]
# # call a method on each element
# freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
# [weapon.strip() for weapon in freshfruit]
# # create a list of 2-tuples like (number, square)
# [(x, x**2) for x in range(6)]
# the tuple must be parenthesized, otherwise an error is raised
# vec = [[1,2,3], [4,5,6], [7,8,9]]
# wow=[num for elem in vec for num in elem]
# print(wow)
# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]]
#arr1=list(zip(*matrix))
#print(arr1)
#wow1=[[row[i] for row in matrix] for i in range(4)]
#print(wow1)
#transposed = []
#for i in range(4):
#    transposed.append([row[i] for row in matrix])
#print(transposed)
#d=1,5,"is this real"
#f=d,(4,5,4)
#print(d)
#print(f)
#x, y, z = f
# basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# print(basket)                      # show that duplicates have been removed
# 'orange' in basket                 # fast membership testing
# 'crabgrass' in basket
# a = set('abracadabra')
# b = set('alacazam')
# a                                  # unique letters in a
# a - b                              # letters in a but not in b
# a | b                              # letters in a or b or both
# a & b                              # letters in both a and b
# a ^ b                              # letters in a or b but not both

# def zeroSumSlice(lst):
#     n = len(lst)
#     for i in range(n+1):
#         for j in range(i + 1, n+1):
#             someSlice = lst[i:j]
#             if sum(someSlice) == 0:
#                 return someSlice
# print(zeroSumSlice([1,3,2,-3]))

# n=int(input('Please enter a positive integer between 1 and 15: '))
# for row in range(1,n+1):
#     for col in range(1,n+1):
#         print(row*col, end="\t")
#     print()
    
    
    
    
# n=int(input('Please enter a positive integer between 1 and 15: '))
# for row in range(1,n+1):
# print(*("{:3}".format(row*col) for col in range(1, n+1))
    
    
    
    
# for row in range(1, n + 1):
# print(*(f"{row*col:3}" for col in range(1, n + 1)))
    
    
# for i in range(1, 10) :
#     for j in range(1, 10):
#         print(repr(i*j).rjust(4),end=" ")
# print()
# print()




# for i in range(1, 11):
#     for j in range(1, 11):
#         print(("{:6d}".format(i * j,)), end='')
# print()





# def main():

#     rows = int(input("Enter the number of rows that you would like to create a multiplication table for: "))
#     counter = 0
#     multiplicationTable(rows,counter)

# def multiplicationTable(rows,counter):

#     size = rows + 1

#     for i in range (1,size):
#         for nums in range (1,size):
#             value = i*nums
#             print(value,sep=' ',end="\t")
#             counter += 1
#             if counter%rows == 0:
#                 print()
#             else:
#                 counter
# main()



# n=int(input('Please enter a positive integer between 1 and 15: '))
# for row in range(1,n+1):
#     s = ''
#     for col in range(1,n+1):
#         s += '{:3} '.format(row * col)
#     print(s)
    
    
    
    
    # OK here is my 2 cents. It uses Python3 f strings to dynamically adjust column width based on the square of the table size (m*m):

# m = int(input("Multiplcation table to?: "))
# w = len(str(m*m)) # Column size
# for i in range(1,m+1):
#     print(*(f"{j*i:{w}d}" for j in range(1,m+1)))
    
    
    
    
############## number of elements that are n and n + 1 that have equal number of divisors.

# arr = []
# for i in range(2, 10000):
#     even = x = i + 1 if i % 2 else i
#     odd =  i  if i % 2 else i + 1
#     f_even = 0
#     f_odd = 0
#     exp = 0
#     while True:
#         if x % 2 == 0:
#             x = x // 2
#             exp += 1
#         elif x == 1:
#             f_even = exp + 1
#             break
#         else:
#             break
#     count1 = 0
#     if x != 1:
#         for j in range(1, x , 2):
#             y =  x // j
#             if x % j == 0 and y > j:
#                 count1 += 2
#             elif x % j == 0 and y == j:
#                 count1 += 1
#             elif y < j:
#                 break
#         f_even = count1* (1 + exp)
#     count2 = 0
#     z = odd
#     for j in range(1, odd + 1, 2):
#         z = odd // j   
#         if odd % j == 0 and z > j:
#             count2 += 2
#         elif odd % j == 0 and z == j:
#             count2 += 1
#         elif z < j:
#             break  
#     f_odd = count2
#     if f_even == f_odd:
#         arr.append([i, i+1])
# print(len(arr))
# # print(arr)

    