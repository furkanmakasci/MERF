def incrementby(lowest,highest,increment):
    list=[lowest]
    a=(highest-lowest)/increment
    a=int(a)
    for i in range(1,a+1):
        list.append(lowest+(i*increment))
    if not list[-1]==highest:
        list.append(highest)
    return list
    
wlist=incrementby(1,1,1)
xlist=incrementby(1,1,1)
ylist=incrementby(1,20,1)
#zlist=incrementby(1,5,1)

zlist=[2,5,10]


print("w x y z result")

for w in wlist:
    for x in xlist:
        for y in ylist:
            for z in zlist:
                result=1.25/100*y*378/(z/1000)
                if 5000<result<10000:
                    result1=1.25*y*y*.125*.064/(z/1000)
                    if 125<result1<175:
                        print(w,x,y,z,result1,result) # result1=inductance, result2=magnetic density
