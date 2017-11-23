from datetime import date
from datetime import timedelta
firstDate= "23/02/2000"
k= 2
#daysOfTheWeek= ["Monday","Tuesday","Wednesday","Thursday","Saturday","Sunday"]
daysOfTheWeek= ["Wednesday", "Friday"]
n= 4

daysWeek = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

def recurringTask(firstDate, k, daysOfTheWeek, n):
    strDate = firstDate.split('/')
    theDate = date(int(strDate[2]), int(strDate[1]), int(strDate[0]))    
    #startDayWeek = theDate.weekday()
    startDayWeek = theDate.isoweekday()
    
    myDeltaDays = []
    
    iDaysOfTheWeek = sorted([findDayOfWeek(d) for d in daysOfTheWeek])
    if startDayWeek < iDaysOfTheWeek[len(iDaysOfTheWeek)-1]:
        myDeltaDays = myDeltaDays + [findDayOfWeek(x) - startDayWeek for x in daysOfTheWeek if findDayOfWeek(x)>startDayWeek]
    if startDayWeek > iDaysOfTheWeek[0]:
        myDeltaDaysBefore = [(len(daysWeek) - startDayWeek) + findDayOfWeek(x) for x in daysOfTheWeek if findDayOfWeek(x) < startDayWeek]            
        myDeltaDays = myDeltaDays + myDeltaDaysBefore
    myDeltaDays = myDeltaDays + [k*7]
    print(myDeltaDays)
    nextDates = [theDate.strftime("%d/%m/%Y")]
    while n>len(nextDates):
        for i in myDeltaDays:
            if len(nextDates) >= n: return nextDates
            delta = timedelta(days=i)
            nextDate = theDate + delta
            print(nextDate)  
            nextDates.append(nextDate.strftime("%d/%m/%Y"))            
        theDate = nextDate
    return nextDates

def findDayOfWeek(strDay):
    for x in range(0, len(daysWeek)):
        if strDay.lower() == daysWeek[x].lower(): return x
    return -1

print(recurringTask(firstDate,k,daysOfTheWeek,n))