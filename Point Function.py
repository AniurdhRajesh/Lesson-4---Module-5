class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def get_cords(self):
        return f"Point ({self.x},{self.y})"
obj=point(3,4)
print(obj.get_cords())