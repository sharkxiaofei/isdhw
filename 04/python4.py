import math
class Ellipse:
    @classmethod
    def Ellipse(self,a,b):
        return(math.pi*a*b)
class Square:
    @classmethod
    def Square(self,c):
        return(c*c)
class Rectangle:
    @classmethod
    def Rectangle(self,d,e):
        return d*e
class Circle:
    @classmethod
    def Circle(self,f):
        return math.pi*f*f
class Myclass(Ellipse,Square,Rectangle,Circle):
    count=0
    def compute_area(self,shapes):
        q=[]
        a=shapes
        b=a.split(',')
        i=0
        k=0
        while(i<len(b)):
            b[i]='Myclass.'+b[i]
            if(ord(b[i][len(b[i])-1])>=48 and ord(b[i][len(b[i])-1])<=57):
                b[i]=b[i]+','+b[i+1]
                q.append(i+1)
                i=i+1
            i=i+1
        for j in q:
            del b[j-k]
            k=k+1
        for i in range(0,len(b)):
            exec('Myclass.count+='+b[i])
        return(Myclass.count)
q=Myclass()
print("总面积是：",q.compute_area(input("请输入图形列表，如Ellipse(16,20),Square(15),Rectangle(20,15):")))
