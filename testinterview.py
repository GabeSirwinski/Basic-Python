import math

per1 = [['8:04','9:00'],['12:02','13:10'],['15:45','16:30']]
per2 = [['10:00','11:30'],['12:50','13:15'],['16:30','18:45']]
times = [['6:00','20:00']]

def findopenslots():
    sched1 = []
    sched2 = []
    dailyAllowed = []
    dailyMinutes = []
    subtractTime = []
    available = []
    def convertToInt(x,y):
        for i in x:
            for r in i:
                t = r.split(':')
                m = int((int(t[0]) * 60)) + int(t[1])
                y.append(m)
    convertToInt(times,dailyAllowed)        
    convertToInt(per1,sched1)
    convertToInt(per2,sched2)
    convertToInt(times,dailyAllowed)
    def subtract(x,y,z):
        for i in range(x[y],x[z]-1):
            subtractTime.append(i)        
    def createMinutes():    
        for i in range(dailyAllowed[0],dailyAllowed[1]-1):
            dailyMinutes.append(i)
    createMinutes()
    subtract(sched1,0,1)
    subtract(sched1,2,3)
    subtract(sched1,4,5)
    subtract(sched2,0,1)
    subtract(sched2,2,3)
    subtract(sched2,4,5)
    for i in subtractTime:
        if i in dailyMinutes:
            dailyMinutes.remove(i)
    available.append(dailyMinutes[0]+1)    
    for x,y in zip(dailyMinutes,dailyMinutes[1:]):
        if (x + 1) != y:
            available.append(x+1)
            available.append(y+1)
    available.append(dailyMinutes[len(dailyMinutes)-1]+1)
    for i in available:
        m = i % 60
        h = int(i / 60)
        i = available.index(i)
        available[i] = '{:02d}:{:02d}'.format(h,m)    
    counter = 0
    for x,y in zip(available,available[1:]):
        if x == y:
            counter += 1
            continue
        elif counter % 2 == 0:
            print('{} to {} is free'.format(x,y))
            counter += 1
        else:
            counter += 1
    print('There is no more availability until tomorrow.')

findopenslots()
