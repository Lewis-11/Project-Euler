months={'Jan': 31, 'Feb': 28, 'Mar': 31, 'Apr':30, 'May':31, 'Jun':30, 'Jul':31, 'Aug':31, 'Sep':30, 'Oct':31, 'Nov':30, 'Dec':31}
weekday={0:'mon', 1:'tue', 2:'wed', 3:'thu', 4:'fri', 5:'sat', 6:'sun'}
day=1
weekcount=1

year=1900
count=0

while year<2001:
    for month in months:
        while day<=months[month]:
            if day==1 and month=='Jan' and year==1901:
                count=0
            if weekday[weekcount]=='sun' and day==1:
                count+=1
            print(str(day) + "("+str(weekday[weekcount])+")" +" " +str(month)+" of " +str(year))
            day+=1
            weekcount=(weekcount+1)%7
        day=0
    if month=='Dec':
        year+=1
print(count)