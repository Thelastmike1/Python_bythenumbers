"This is just supposed to take the transcripts file and give me the number of words used the most as a dictionary "
fname = input('Enter File: ')
if len(fname) < 1 : fname = 'transcript.txt'
fhandle = open(fname) 
countingwords = dict()
for line in fhandle:
    line = line.lstrip()
    words = line.split()
#The code above gives me the striped lines and puts those lines into a list? I think it might be a dictionary
    for x in words: 
        #oldcount = countingwords.get(x,0)
        #print(x,'old',oldcount)
        #newcount = oldcount + 1
        #countingwords[x] = newcount
# The code below replaces the code above, I do not completely understand why yet...
        countingwords[x] = countingwords.get(x,0) + 1
        if countingwords[x] > 1:
            print(x,countingwords[x])
        else:
            print(x,'NEW',countingwords[x])
# Code above is an idiom : retrieve/create/update/counter
        #if x in countingwords:
            #countingwords[x] = countingwords[x] + 1
        #else:
            #countingwords[x] = 1
        #print(x,countingwords[x])
    
    #print(countingwords)
#Now we want to find the most common word in the file
largest = -1
theword = None
for y,z in countingwords.items():
    print(y,z)
    if z > largest :
        largest = z
        theword = y

print('Done largest is word and value is :',theword, largest)

            




    
