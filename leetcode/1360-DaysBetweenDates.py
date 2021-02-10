class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        def isleapyear(year):
            flag=False
            if year%4==0:
                if year%100==0:
                    if year%400==0:
                        flag=True
                else:
                    flag=True
            return flag
        
        def totaldays(year,month,day):
            md=[31,28,31,30,31,30,31,31,30,31,30,31]
            total=0
            for i in range(1971,year):
                total+=366 if isleapyear(i) else 365
            return total+sum(md[:month-1])+day
        
        y1,m1,d1=map(int,date1.split("-"))
        y2,m2,d2=map(int,date2.split("-"))
        t1=totaldays(y1,m1,d1)
        t2=totaldays(y2,m2,d2)
        if isleapyear(y1) and m1>2:
            t1+=1
        if isleapyear(y2) and m2>2:
            t2+=1
        
        return abs(t1-t2)