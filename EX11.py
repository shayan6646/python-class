class time:
    def __init__(obj,h,m,s):
        obj.hour=h
        obj.minute=m
        obj.second=s
    def show(obj,day):
        obj.date = day
        return str(obj.hour)+':'+str(obj.minute)+':'+str(obj.second)
    def total_number_of_seconds(obj):
        return str(obj.hour*3600+obj.minute*60+obj.second)
