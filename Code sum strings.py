
#Need to do the same as Code sum.py, but now take into account the numbers that could be written in english intead as digits 
#I still need to take into account the digits, so I need to check both at the same time, gonna try to do this all in one iteration of the code

#I could use the find() function, might not be the best solution but its the best I can think of at the moment, I could look for the digits like normal and once those are found, i do find for "one" to "nine"
#Should probably lower() everything 


sum = 0 
numbersAsString = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

codeFile = open('C:/Users/jclay/OneDrive/Desktop/Personal Projects/Elf  project/Day 1/Project 1/codes.txt', 'r')

for line in codeFile:

    l = 0
    r = len(line) - 1

    check = 0

    #Running through current line and find the first and last instances of digits in the code, gets indexes
    while (not line[l].isnumeric()) or  (not line[r].isnumeric()):
        if not line[l].isnumeric():
            l += 1
            check += 1
        if not line[r].isnumeric():
            r -= 1
            check += 1
        if check > len(line):
            l = 0
            r = len(line) - 1
            break
        
    #Running through current line and find the first and last instances of digits as substrings in the code, gets indexes
    low = len(line)
    high = 0

    low_num = ''
    high_num = ''
    for x in numbersAsString:
        temp_low = line.find(x)
        temp_high = line.find(x, r)
        while True:
            if temp_high == len(line) - 1:
                    break
            elif line.find(x, temp_high + 1) == -1:
                break
            else:
                temp_high = line.find(x, temp_high + 1)
        if temp_low == -1:
            continue
        else:
            if temp_low < low:
                low = temp_low
                low_num = x
            if temp_high > high:
                high = temp_high
                high_num = x
    
    #compares the 4 indexes and sees which ones are the first and last, and saves the digit it is supposed to be into left and right digit
    left_digit = 0
    right_digit = 0

    if l > low:
        left_digit = numbersAsString.index(low_num)
        left_digit += 1
        left_digit = str(left_digit)
    else:
        left_digit = str(line[l])

    if r < high:
        right_digit = numbersAsString.index(high_num)
        right_digit += 1
        right_digit = str(right_digit)
    else:
        right_digit = str(line[r])
    
    sum += int(left_digit + right_digit)

    
print(sum)


