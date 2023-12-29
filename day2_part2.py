
codeFile = open('C:/Users/jclay/OneDrive/Desktop/Personal Projects/Elf  project/Day 2/input_day2_pt1.txt', 'r')


id = 0

itr = 8

r_min = 0
g_min = 0
b_min = 0

sum = 0

check = True


for line in codeFile:
    id += 1
    itr = 8

    r_min = 0
    g_min = 0
    b_min = 0

    check = True

    while itr < len(line):
            
        #if line[itr].isnumeric(): 
            #print(line[itr:itr + 2])
        
        match line[itr:itr+2]:
            case ' r':
                if int(line[itr-2:itr]) > r_min:
                    r_min = int(line[itr-2:itr])
                    

        
            case ' g':
                if int(line[itr-2:itr]) > g_min:
                    g_min = int(line[itr-2:itr])
                    
        
                
            case ' b':
                if int(line[itr-2:itr]) > b_min:
                    b_min = int(line[itr-2:itr])
                    
        

        itr += 1
        
    
    sum += r_min * g_min * b_min
    
     

    #if id == 4:
        #break
    #print(" ")
print(sum)



        


    
    
                
      

          
                






    




