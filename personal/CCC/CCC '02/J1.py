linePatterns = ["", "", "", "", ""]
linePatterns[0] = [" * * *"]
linePatterns[1] = ["*     *"]
linePatterns[2] = ["      *"]
linePatterns[3] = [""]
linePatterns[4] = ["*"]

#create all the possible numbers using patterns
numPattern = ["", "", "", "", "", "", "", "", "", ""]
numPattern[0] = [0, 1, 1, 1, 3, 1, 1, 1, 0]
numPattern[1] = [3, 2, 2, 2, 3, 2, 2, 2, 3]
numPattern[2] = [0, 2, 2, 2, 0, 4, 4, 4, 0]
numPattern[3] = [0, 2, 2, 2, 0, 2, 2, 2, 0]
numPattern[4] = [3, 1, 1, 1, 0, 2, 2, 2, 3]
numPattern[5] = [0, 4, 4, 4, 0, 2, 2, 2, 0]
numPattern[6] = [0, 4, 4, 4, 0, 1, 1, 1, 0]
numPattern[7] = [0, 2, 2, 2, 3, 2, 2, 2, 3]
numPattern[8] = [0, 1, 1, 1, 0, 1, 1, 1, 0]
numPattern[9] = [0, 1, 1, 1, 0, 2, 2, 2, 0]

number = int(input()) #get the number to be printed

#print the number
for i in numPattern[number]:
  print(linePatterns[i][0])