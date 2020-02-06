#The ultimate hello world
import random as rnd
import hashlib as hs
import time 

starttime = time.time()
def hi(isItDumb, printIters):
    chars = [chr(i) for i in range(32,128)]
    charMatrix = []
    for i in range(len(chars)):
        charMatrix.append(chars[i:len(chars):1] + chars[:i:1])
    iters = 0
    
    
    
    hello = ""
    if isItDumb:
        
        while True:
            
            num1 = rnd.choice(range(0,len(charMatrix[0])))
            num2 = rnd.choice(range(0,len(charMatrix[0])))
            hello += charMatrix[num1][num2]
            iters+=1
            if hs.sha265(hello.encode()).hexdigest() == hs.sha265("Hello World!".encode()).hexdigest():
                print(hello)
                print(time.time() - starttime)
                break
            if iters%printIters==0:
                print(iters, time.time()-starttime, hello)
            elif len(hello) > 15:

                hello=""

    
    else:
        while True:
            
            num1 = rnd.choice(range(0,len(charMatrix[0])))
            num2 = rnd.choice(range(0,len(charMatrix[0])))
            hello += charMatrix[num1][num2]
            iters+=1
            if hello == "Hello world!":
                print(hello)
                print(time.time() - starttime)
                break
            if iters%printIters==0:
                print(iters, time.time()-starttime, hello)
            elif len(hello) > 15:
                hello=""

    
hi(False,10000000)