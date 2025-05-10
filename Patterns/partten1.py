# Question - 1 right angle

'''
num = int(input("Enter the number: "))

if num <= 0:
    print("Please enter postive.")
else:
    for i in range (1 ,num + 1):
        for j in range(1 ,i + 1):
            print("*" * j)
        print("")
'''   
        
# *
# **
# ***
# ****       
            
# Question -2  Squrare pattern 

'''
num = 5 #(0,1,2,3,4)

for i in range(1 , num+1):
    for j in range(num - i): # i= 1 ,2
        print(" ", end=" ")
    for k in range(1, 2*i):
        print("*",end=" ")
    print()
    '''
    
    
    
#         * 
#       * * * 
#     * * * * *
#   * * * * * * *
# * * * * * * * * *
    
    
# Question -3 inverted pyramid in python
'''
num = 5
for i in range(-(num),0):
    for j in range(1,-(i) + 1):
        print("*" , end="")
    print("")
    
    '''
    
# *****
# ****
# ***
# **
# *



# Question -4 

'''
num = 5
for i in range(-(num),0):
    for j in range(1,-(i) + 1):
        print("*" , end="")
    print("")
for i in range (1 ,num + 1):
    for j in range(1 ,i + 1):
        print("*" , end="")
    print("")
    
    '''
# *****
# ****
# ***
# **
# *
# *
# **
# ***
# ****
# *****

 
# Question - 5 
'''
num = 5 

for i in range (1 ,num + 1):
    for j in range(1 ,i + 1):
        print("*" , end="")
    print("")
for i in range(-(num),0):
    for j in range(1,-(i) + 1):
        print("*" , end="")
    print("")



'''

# *
# **
# ***
# ****
# *****
# *****
# ****
# ***
# **
# *


# Question - 6 
'''
num = 5

for i in range(num, 0,-1):
    for j in range(num - i):
        print(" " ,end="")
    for j in range(2*i -1):
        print('*', end="")
    print()
    '''
    
# *********
#  *******
#   *****
#    ***
#     *


# Question - 7 
'''
num = 5

for i in range(1, num + 1):
    for j in range(i):
        print("*", end=" ")
    print()

for i in range(num - 1, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
    '''
# *  
# * * 
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
    

# Question - 8

n= 6 
for i in range (1,6):
    for j in range(1,i+1):
        print(j, end=" ")
    print()
for i in range (6 - 1, 1):
    for j in range(1,i+1):
        print(j, end=" ")
    print()

    
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5   
        
        