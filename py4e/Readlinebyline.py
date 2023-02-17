"Readlinebyline"
fmail = open ('transcript.txt')
for line in fmail:
    if line.startswith("Sheila"): 
        print(line.upper())
    else:
        continue