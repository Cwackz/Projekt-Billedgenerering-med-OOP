from PIL import Image, ImageDraw
import tkinter as tk
from tkinter import simpledialog, Menu
# Definer cirkel klassen
class Circle:
    def __init__(self, radius, position, color):
        self.radius = radius
        self.position = position
        self.color = color

    def draw(self, image):
        draw = ImageDraw.Draw(image)
        left_up_point = [self.position[0] - self.radius, self.position[1] - self.radius]
        right_down_point = [self.position[0] + self.radius, self.position[1] + self.radius]
        draw.ellipse([tuple(left_up_point), tuple(right_down_point)], fill=self.color)

# Definer en rektangel-klasse
class Rectangle:
    def __init__(self, width, height, position, color):
        self.width = width
        self.height = height
        self.position = position
        self.color = color

    def draw(self, image):
        draw = ImageDraw.Draw(image)
        draw.rectangle((
            self.position[0],
            self.position[1],
            self.position[0] + self.width,
            self.position[1] + self.height
        ), fill=self.color)

# Definer trekant klassen
class Triangle:
    def __init__(self, side, position, color):
        self.side = side
        self.position = position
        self.color = color

    def draw(self, image):
        draw = ImageDraw.Draw(image)
        draw.polygon((
            self.position[0], self.position[1],
            self.position[0] + self.side, self.position[1],
            self.position[0] + self.side / 2, self.position[1] + self.side
        ), fill=self.color)

def main():
    root = tk.Tk()
    menubar = Menu(root)
    root.config(menu=menubar)

    circle_menu = Menu(menubar, tearoff=0)
    rectangle_menu = Menu(menubar, tearoff=0)
    triangle_menu = Menu(menubar, tearoff=0)

    image = Image.new("RGBA", (800, 800), (255, 255, 255, 255))
    circle = Circle(100, (200, 400), (255, 0, 0, 255))
    rectangle = Rectangle(200, 200, (300, 300), (0, 255, 0, 255))
    triangle = Triangle(200, (500, 300), (0, 0, 255, 255))

    def redraw_all():
        nonlocal image
        image = Image.new("RGBA", (800, 800), (255, 255, 255, 255))
        circle.draw(image)
        rectangle.draw(image)
        triangle.draw(image)
        image.show()

    def change_circle_color():
        new_color = simpledialog.askstring("Skift cirkel farve", "Indtast ny farve (r g b a) uden kommaer")
        if new_color is not None:
            circle.color = tuple(map(int, new_color.split()))
            redraw_all()
    def change_circle_size():
        new_radius = simpledialog.askinteger("Skift cirkel størrelse", "Indtast ny radius") # 
        if new_radius is not None:
            circle.radius = new_radius
            redraw_all()


    circle_menu.add_command(label="Skift cirkel farve", command=change_circle_color)
    circle_menu.add_command(label="Skift cirkel størrelse", command=change_circle_size)
    menubar.add_cascade(label="Cirkel indstillinger", menu=circle_menu)

    def change_rectangle_color():
        new_color = simpledialog.askstring("Skift rektangel farve", "Indtast ny farve (r g b a) uden kommaer")
        if new_color is not None:
            rectangle.color = tuple(map(int, new_color.split()))
            redraw_all()
    def change_rectangle_size():
        new_width = simpledialog.askinteger("Skift rektangel bredde", "Indtast ny bredde")
        new_height = simpledialog.askinteger("Skift rektangel højde", "Indtast ny højde")
        if new_width is not None and new_height is not None:
            rectangle.width = new_width
            rectangle.height = new_height
            redraw_all()

    rectangle_menu.add_command(label="Skift rektangel farve", command=change_rectangle_color)
    rectangle_menu.add_command(label="Skift rektangel størrelse", command=change_rectangle_size)
    menubar.add_cascade(label="Rektangel indstillinger", menu=rectangle_menu)

    def change_triangle_color():
        new_color = simpledialog.askstring("Skift trekant farve", "Indtast ny farve (r g b a) uden kommaer")
        if new_color is not None:
            triangle.color = tuple(map(int, new_color.split()))
            redraw_all()

    def change_triangle_size():
        new_side = simpledialog.askinteger("Skift trekant side", "Indtast ny side")
        if new_side is not None:
            triangle.side = new_side
            redraw_all()

    triangle_menu.add_command(label="Skift trekant farve", command=change_triangle_color)
    triangle_menu.add_command(label="Skift trekant størrelse", command=change_triangle_size)
    menubar.add_cascade(label="Trekant indstillinger", menu=triangle_menu)


    def save_image():
        image_name = simpledialog.askstring("Gem billede", "Hvad skal billedet hedde?")
        if image_name is not None:
            image.save(image_name + ".png")
        else:
            image.save("image.png")
    
    menubar.add_command(label="Gem billede", command=save_image)

    redraw_all()
    root.mainloop()

if __name__ == "__main__":
    main()
