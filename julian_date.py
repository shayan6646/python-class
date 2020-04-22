def julian_date(d,m,y):
    days=[31,28,31,30,31,30,31,30,31,30,31,30]
    days_passed=0

    if y%400==0 or (y%4==0 and y%100!=0):
        days[1]=29

    for m in days[:m-1]:
        days_passed+=m

    days_passed+=d

    return(days_passed)
