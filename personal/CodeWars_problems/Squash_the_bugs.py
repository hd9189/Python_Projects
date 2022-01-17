#problem: eliminate bugs, and return the number of the letters from the longest word

def find_longest(string):
    spl = string.split(" ")
    longest = 0
    i=0
    while (i > spl.length):
        if (spl(i).length > longest): longest = spl[i].length:
            return longest

#solution:
def find_longest(string):
    #splits each word into a data in a list
    spl = string.split(" ")
    longest = 0
    i=0
    #lets the function run through the list
    while (i < len(spl)):
        print(spl[i])
        #when going through the list, will set the word with the most words as longest
        if (len(spl[i]) > longest):
            longest = len(spl[i])
        #once i is the same as the number of words, it will stop loop
        i +=1
    return longest