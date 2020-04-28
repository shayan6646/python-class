class time:
    def __init__(obj,h,m,s):
        obj.hour = h
        obj.minute = m
        obj.second = s
    def show(obj,ruz):
        obj.date = ruz
        return str(obj.hour)+':'+str(obj.minute)+':'+str(obj.second)
    def number_of_seconds(obj):
        return str (obj.hour*3600+obj.minute*60+obj.second)
    def sub(obj,obj2):
        obj.hour -= obj2.hour
        obj.minute -= obj2.minute
        obj.second -= obj2.second
    def kam_kardan(obj,hh,mm,ss):
        obj1.hour -= hh
        obj1.minute -= mm
        obj1.second -= ss
        
    def __add__(obj,obj2):
        obj.hour += obj2.hour
        obj.minute += obj2.minute
        obj.second += obj2.second

    def __sub__ (obj,obj2):
        obj.hour -= obj2.hour
        obj.minute -= obj2.minute
        obj.second -= obj2.second


    def __eq__(obj,obj2):
        if (obj.hour==obj2.hour) and (obj.minute==obj2.minute) and (obj.second==obj2.second):
            return True
        return False
    
    def __gt__(obj,obj2):
        if obj.hour>obj1.hour:
            return True
        if obj.hour==obj2.hour and obj.minute>obj2.minute:
            return True
        if obj.hour==obj2.hour and obj.minute==obj2.minute and obj.second>obj2.second:
            return True
        return False

    def __ge__ (obj,obj2):
        if obj.hour>obj1.hour:
            return True
        if obj.hour==obj2.hour and obj.minute>obj2.minute:
            return True
        if obj.hour==obj2.hour and obj.minute==obj2.minute and obj.second>=obj2.second:
            return True
        return False
    
    def __lt__(obj,obj2):
        if obj.hour<obj1.hour:
            return True
        if obj.hour==obj2.hour and obj.minute<obj2.minute:
            return True
        if obj.hour==obj2.hour and obj.minute==obj2.minute and obj.second<obj2.second:
            return True
        return False
    
    
    def __le__ (obj,obj1):
        if obj.hour<obj2.hour:
            return True
        if obj.hour==obj2.hour and obj.minute<obj2.minute:
            return True
        if obj.hour==obj2.hour and obj.minute==obj2.minute and obj.second<=obj2.second:
            return True
        return False
    
