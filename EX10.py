class coordination:
    x=0
    y=0
%%%%%%%%%%%%%%%%%%%%%%%
Inputs:
    
obj1=coordination()
obj2=coordination()

obj1.x=3
obj1.y=4
obj2.x=7
obj2.y=9

%%%%%%%%%%%%%%%%%%%%%%%
def distance(a,b):
    return ((a.x-b.x)**2+(a.y-b.y)**2)**0.5
