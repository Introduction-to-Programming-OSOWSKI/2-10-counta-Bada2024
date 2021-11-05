#WRITE YOUR CODE IN THIS FILE
def countA(w):
    c=0
    for i in range(0,len(w)):
        if w[i] == "a":
             c=c+1
    return c
print(countA("aaaaaaaaaaaaaaaaaaaa"))