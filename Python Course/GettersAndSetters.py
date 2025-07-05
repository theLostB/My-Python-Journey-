class Myclass:
    def __init__(self, value):
        self._value = value
    
    def show(self):
        print(f'Value is {self._value}')
        
    @property #Getters
    def ten_value(self):
        return 10* self._value
        
    @ten_value.setter #Setters
    def ten_value(self, new_value):
        self._value = new_value/10
   
obj = Myclass(10)
obj.ten_value = 67 #If I don't use setters i unable to change the value of ten_value and this line gives error but here i have used setters so now it not give any error
print(obj.ten_value)
obj.show()