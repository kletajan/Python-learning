class Rectangle:
    def __init__(self, width, height):
        self.width = width       
        self.height = height
    
    def set_width(self, width):
        self.width = width       
        
    def set_height(self, height):
        self.height = height
    
    def get_area(self):
        return self.width * self.height
        
    def get_perimeter():
        return (2 * width + 2 * height)
        
    def get_diagonal(self):
        return ((width ** 2 + height ** 2) ** .5)
    
    def get_picture(height, width):
        if height > 50 or width > 50: return "Too big for picture."
        saveWidth = width
        picture = ""
        while height > 0:
            width = saveWidth
            while width > 0:
                picture = picture + "*"
                width = width - 1
            picture = picture + "\n"
            height = height - 1
        return picture
        
    def get_amount_inside():
        return ""
        
class Square(Rectangle):
    def __init__(self, side):
        self.width = side       
        self.height = side

rect = Rectangle(10, 5)
#print(rect.get_area())
#print("test: 50")
#rect.set_height(3)
#print(rect.get_perimeter())
#print("test: 26")
print(rect.height)
print("test: Rectangle(width=10, height=3)")
#print(rect.get_picture())
#print("""**********
#**********
#**********""")

#sq = shape_calculator.Square(9)
#print(sq.get_area())
#print("test: 81")
#sq.set_side(4)
#print(sq.get_diagonal())
#print("test: 5.656854249492381")
#print(sq)
#print("test: Square(side=4)")
#print(sq.get_picture())
#print("""****
#****
#****"""
#
#rect.set_height(8)
#rect.set_width(16)
#print(rect.get_amount_inside(sq))
#print("test: 8")

#moj
#print(rect.get_picture(4, 49))