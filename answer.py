def answer():

 myli = []
 add = 0

 for i in range(1000):
    if i % 3==0 :
        myli.append(i) 
    elif i % 5==0:
        myli.append(i)  
 for num in myli:
    add = add + num
 print(add)

if __name__ == "__main__": 
 answer()



