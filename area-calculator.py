class Rectangle:
    def __init__(self, w, h):
        self.height = h
        self.width = w
        
    def set_width(self, w):
        self.width = w
        
    def set_height(self, h):
        self.height = h

    def get_area(self):
        return (self.width * self.height)

    def get_perimeter(self):
        return ((2 * self.width) + (2 * self.height))

    def get_diagonal(self):
        return (((self.width * self.width) + (self.height ** 2))** .5)

    def get_picture(self):
        picture_string = ''
        i = 0
        i1 = 0
        if self.height < 51:
            while i < self.height:
                while i1 < self.width:
                    picture_string += f"{'*'}"
                    i1+= +1
                picture_string += '\n'
                i1 = 0
                i += +1
        else:
            picture_string = "Too big for picture."
        return picture_string

    def get_amount_inside(self, r, s):
        print(r,s)
        if r < s:
           return (s / r) 
        if r > s:
           return (r / s)
    
    def __str__(self):
        return (f"Rectangle(width={self.width}, height={self.height})")

   
class Square (Rectangle):
    def __init__(self, wh):
        self.height = wh
        self.width = wh
    def set_side(self, wh):
        self.height = wh
        self.width = wh
    def __str__(self):
        return (f"Square(side={self.width})")

rect = Rectangle(5, 10)
print(rect.get_area())
rect.set_width(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())