#I am given a long list of strings, where each string contains at least one number, where the rules are the first and last number in the string make up the value for that specific code

#I need to find the sum of all these codes in order to get the result



#I need to make a nested for loop, first one is running through all the codes, second runs through the current string 

#In the inner loop, I can have one var looking at the first value, and another looking at the very last value, and I check to see if either are numbers, if not, i iterate them either forward and backward

#Once either iterator finds a number, it stops iterating and waits until the other one finds a number. 
#Ci12139352#
#Once both iterators are on a number, I take both, make them a string, convert it into an int value, and add it to the running total



sum = 0 

codeFile = open('C:/Users/jclay/OneDrive/Desktop/Personal Projects/Elf  project/Day 1/Project 1/codes.txt', 'r')

for line in codeFile:
    l = 0
    r = len(line) - 1

    while (not line[l].isnumeric()) or  (not line[r].isnumeric()):
        if not line[l].isnumeric():
            l += 1
        if not line[r].isnumeric():
            r -= 1
    #l and r are now the indexes for the first and last instances of numbers in the string, now I just need to combine them into a string and add the int into the sum 

    num_string = line[l] + line[r]
    sum += int(num_string)
    
print(sum)





    

    