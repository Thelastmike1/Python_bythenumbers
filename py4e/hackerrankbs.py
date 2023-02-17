n = input(' ')

if int(n) % 2 != 0:
    print ('wierd')
elif int(n) in range (2,5):
    if int(n) % 2 == 0:
        print('Not Weird')
elif int(n) in range (6,20):
    if int(n) % 2 == 0:
        print("wierd")
elif int(n) >= 21:
    print("Not Wierd")

    