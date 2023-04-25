print('staff version with Hostogram\n')

n=1
m=0
f=''
g=''
h=''
j=''
q=0
w=0
e=0
r=0


while n<2:
    a = int(input("Enter your credit for pass "))
    b = int(input("Enter your defer for pass "))
    c = int(input("Enter your fail for pass "))
          
    if(a==120):
        f=f+'*'
        q=q+1
        print('Progress')
        
    elif(a==100 and c<40):
        g=g+'*'
        w=w+1
        print ('Progress(module trailer)')
    elif(a==40 and b==0):
        j=j+'*'
        r=r+1
        print('Excluded')
    elif(a<100 and a>20 and b>=0 and c<100):
        h=h+'*'
        e=e+1
        print('Do not progress-module retriever')
    elif(a<40 and a>0 and b>20):
        h=h+'*'
        e=e+1
        print('Do not progress- module retriever')
    elif(a<20 and b>40):
        h=h+'*'
        e=e+1
        print('Do not progress- module retriever')
    else:
        j=j+'*'
        r=r+1
        print('Exclude')
    print('')
        
    print('Would you like to enter another set of data')
    x=input('Enter y for yes or q to quit and view results : ')
    m=m+1

    if x=='y':
        n=1
    elif x=='q':
        n=2

        print('---------------------------')
        print('Horizonal Histogram')
        print('Progress',q, ' : ','', f)
        print('Trailor',w, ' : ','','' ,g)
        print('Retriever',e, ' : ', h)
        print('Excluded',r, ' : ','' ,j)
        print('')
        print(m ,'outcomes in total.')
        print('---------------------------')

    else:
        print ('enter yes(y) or quit(q)')
        
    print('')
