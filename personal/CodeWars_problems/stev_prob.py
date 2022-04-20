# #Problem:
# Question 8 (20 marks)

# Band matrices. Write a program BandMatrix.java that takes two integer command-line arguments n and width and prints an n-by-n pattern like the ones below, with a (*) or (x)  (* and x will come in an alternative way, main diag will start with * and next one is x and next one is * again)for each element whose distance from the main diagonal is strictly less than  to width, and an (0) for each entry that is not. 

# Here, distance means the minimum number of cells you have to move (either left, right, up, or down) to reach any element on the main diagonal. 
# ~/Desktop/loops> java BandMatrix 8 1
# *  0  0  0  0  0  0  0  
# 0  *  0  0  0  0  0  0  
# 0  0  *  0  0  0  0  0  
# 0  0  0  *  0  0  0  0  
# 0  0  0  0  *  0  0  0  
# 0  0  0  0  0  *  0  0  
# 0  0  0  0  0  0  *  0  
# 0  0  0  0  0  0  0  *  

# ~/Desktop/loops> java BandMatrix 8 2
# *  x  0  0  0  0  0  0  
# x  *  x  0  0  0  0  0  
# 0  x  *  x  0  0  0  0  
# 0  0  x  *  x  0  0  0  
# 0  0  0  x  *  x  0  0  
# 0  0  0  0  x  *  x  0  
# 0  0  0  0  0  x  *  x  
# 0  0  0  0  0  0  x  * 

# ~/Desktop/loops> java BandMatrix 8 3
# *  x  *  0  0  0  0  0  
# x  *  x  *  0  0  0  0  
# *  x  *  x  *  0  0  0  
# 0  *  x  *  x  *  0  0  
# 0  0  *  x  *  x  *  0  
# 0  0  0  *  x  *  x  *  
# 0  0  0  0  *  x  *  x  
# 0  0  0  0  0  *  x  *  

# ~/Desktop/loops> java BandMatrix 8 4
# *  x  *  x  0  0  0  0  
# x  *  x  *  x  0  0  0  
# *  x  *  x  *  x  0  0  
# x  *  x  *  x  *  x  0  
# 0  x  *  x  *  x  *  x  
# 0  0  x  *  x  *  x  *  
# 0  0  0  x  *  x  *  x  
# 0  0  0  0  x *  x  *  
# Note: you may assume that n and width are non-negative integer.

#Solution:

n = int(input())
width = int(input())-1
for x in range(n):
    main = "*"
    other = "x"
    char = []
    if x < width: s_length = x 
    else: s_length = width
    
    if (n-1) - x < width: e_length = (n-1)-x
    else: e_length = width
    
    if x < width: start_z = 0 
    else: start_z = x - width
    
    char.append(main)
    
    for y in range(s_length):
         if char[0] == main: char.insert(0, other)
         else: char.insert(0, main)
    for y in range(start_z): char.insert(0,'0')
    for y in range(e_length): 
        if char[-1] == main: char.append(other) 
        else: char.append(main)
    for y in range(n - len(char)): char.append('0')
    print(' '.join(char))
    
        
    
        
        
    