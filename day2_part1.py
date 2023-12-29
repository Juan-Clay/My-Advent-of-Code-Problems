
codeFile = open('C:/Users/jclay/OneDrive/Desktop/Personal Projects/Elf  project/Day 2/input_day2_pt1.txt', 'r')


id = 0

itr = 8

r_max = 12
g_max = 13
b_max = 14

sum = 0

check = True


for line in codeFile:
    id += 1
    itr = 8

    check = True

    while itr < len(line):
            
        #if line[itr].isnumeric(): 
            #print(line[itr:itr + 2])
        
        match line[itr:itr+2]:
            case ' r':
                if int(line[itr-2:itr]) > r_max:
                    check = False
                    break

        
            case ' g':
                if int(line[itr-2:itr]) > g_max:
                    check = False
                    break
        
                
            case ' b':
                if int(line[itr-2:itr]) > b_max:
                    check = False
                    break
        

        itr += 1
        
    if check:
        sum += id
    
     

    #if id == 4:
        #break
    #print(" ")
print(sum)



        


    
    
                
      

          
                






    




