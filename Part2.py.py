x=(0,20,40,60,80,100,120)
while (True):
    try:
        a = int(input("Enter your credit for pass "))
        break
    except ValueError:
        print("Integer required")
if a not in x:
    print ('Out of range')
else:           
    while (True):
        try:
            b = int(input("Enter your defer for pass "))
            break
        except ValueError:
            print("Integer required")
    if b not in x:
        print ('Out of range')
    
    else:
        while (True):
            try:
                c = int(input("Enter your fail for pass "))
                break
            except ValueError:
                print("Integer required")
        if a not in x:
            print ('Out of range')
        else:
            if a+b+c>120:
                print('Total incorrect')
            else:     
                if(a==120):
                    print('Progress')
                elif(a==100 and c<40):
                    print ('Progress(module trailer)')
                elif(a==40 and b==0):
                    print('Exclude')
                elif(a<100 and a>20 and b>=0 and c<100):
                    print('Do not progress-module retriever')
                elif(a<40 and a>0 and b>20):
                    print('Do not progress- module retriever')
                elif(a<20 and b>40):
                    print('Do not progress- module retriever')
                else:
                    print('Exclude')



