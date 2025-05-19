# 1.	Write a python program to print the following number pattern using a loop.

# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5

# solution

n=int(input("number of cycles"))
for i in range(n+1):
    print(f"{i}"*i)
    n-=1

# 2.	write a python for loop to print this pattern.
# 1 1 1 1 1 
# 2 2 2 2 
# 3 3 3 
# 4 4 
# 5

# solution

n=int(input("number of cycles"))
for i in range(1,n+1):
    print(f"{i}"*n)
    n-=1


# 3.	Write a function that calculates the distance between two points in the Cartesian coordinate system accepting four arguments: x coordinate of point 1(x1), y coordinate of point 1(y1), x coordinate of point 2(x2) and y coordinate of point 2(y2).  

# solution

initial_distance = (float(input("x coordinate of initial distance")),float(input("y coordinate fo initial distance")))
final_distance = (float(input("x coordinate of final distance")),float(input("y coordinate of final distance")))
print(initial_distance) # prints the initial distance
print(final_distance) # prints the final distance
distance = ((final_distance[1]-initial_distance[1])**2 + (final_distance[0]-initial_distance[0])**2)**(1/2)
print(distance)

# 4.	Write a function that takes a character (a single letter string) and prints out the letter that comes after it. 
 
# def next_char(character): 
# 	 	# your code goes here 
 
# 	>>> next_char(‘a’)  	 # Results ‘b’ 
# 	>>> next_char(‘f’)  	 # Results ‘g’ 

# solution

char="abcdefghijklmnopqrstuvwxyz".lower()
def next_char(character):
    ind_char = char.find(character.lower())
    if (len(character) != 1 or character.isalpha() == False):
        return "please, enter single valid character."
    elif(ind_char ==25):
        return "you've reached the end. try again!!"
    return f"The letter that comes after {character} is " + char[ind_char+1]
print(next_char(input("insert a character")))