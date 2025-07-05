class Math:
    def __init__(self, num):
        self.num = num
    
    def addtonum(self, n):
        self.num += n
       
    @staticmethod
    def add(a, b):
        return a+b
      
a = Math(5)
a.addtonum(4)
print(a.num)#We can add Like this also

#Static Method
print(a.add(6, 8))