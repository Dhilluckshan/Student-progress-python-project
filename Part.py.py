a = int(input("Enter your credit for pass "))
b = int(input("Enter your defer for pass "))
c = int(input("Enter your fail for pass "))
      
if(a==120):
    print('Progress')
elif(a==100 and c<40):
    print ('Progress(module trailer)')
elif(a==40 and b==0):
    print('Excluded')
elif(a<100 and a>20 and b>=0 and c<100):
    print('Do not progress-module retriever')
elif(a<40 and a>0 and b>20):
    print('Do not progress- module retriever')
elif(a<20 and b>40):
    print('Do not progress- module retriever')
else:
    print('Exclude')
