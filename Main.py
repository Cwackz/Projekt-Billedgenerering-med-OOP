import streamlit as st
from PIL import Image, ImageDraw
class _Shape:
    def __init__(self, position, color):
        self.position = position
        self.color = color

class Circle(_Shape):
    def __init__(self, radius, position, color):
        super().__init__(position, color)
        self.radius = radius

    def draw(self, image):
        draw = ImageDraw.Draw(image)
        bounding_box = [
            (self.position[0] - self.radius, self.position[1] - self.radius),
            (self.position[0] + self.radius, self.position[1] + self.radius)
        ]
        draw.ellipse(bounding_box, fill=self.color)

class Rectangle(_Shape):
    def __init__(self, width, height, position, color):
        super().__init__(position, color)
        self.width = width
        self.height = height

    def draw(self, image):
        draw = ImageDraw.Draw(image)
        draw.rectangle([
            self.position,
            (self.position[0] + self.width, self.position[1] + self.height)
        ], fill=self.color)

class Triangle(_Shape):
    def __init__(self, base, height, position, color):
        super().__init__(position, color)
        self.base = base
        self.height = height

    def draw(self, image):
        draw = ImageDraw.Draw(image)
        apex = (self.position[0] + self.base / 2, self.position[1] - self.height)
        draw.polygon([
            self.position,
            (self.position[0] + self.base, self.position[1]),
            apex
        ], fill=self.color)

class Octagon(_Shape):
    def __init__(self, side, position, color):
        super().__init__(position, color)
        self.side = side

    def draw(self, image):
        draw = ImageDraw.Draw(image)
        step = self.side / 4
        draw.polygon([
            (self.position[0] + step, self.position[1]),
            (self.position[0] + 3 * step, self.position[1]),
            (self.position[0] + 4 * step, self.position[1] + step),
            (self.position[0] + 4 * step, self.position[1] + 3 * step),
            (self.position[0] + 3 * step, self.position[1] + 4 * step),
            (self.position[0] + step, self.position[1] + 4 * step),
            (self.position[0], self.position[1] + 3 * step),
            (self.position[0], self.position[1] + step)
        ], fill=self.color)

def main():
    st.title('Figurer med OOP')
    shape_options = ['Cirkel', 'Rektangel', 'Trekant', 'Ottekant']
    selected_shapes = st.sidebar.multiselect("Vælg former for at tegne:", shape_options, default=shape_options)

    image = Image.new("RGBA", (1000, 300), (255, 255, 255, 255))
    shapes = []

    for index, shape_name in enumerate(selected_shapes):
        x_position = st.sidebar.slider(f"{shape_name} X Position", 50, 950, 50 + index * 150)
        y_position = st.sidebar.slider(f"{shape_name} Y Position", 50, 250, 150)
        if shape_name == 'Cirkel':
            radius = st.sidebar.slider(f"{shape_name} Radius", 10, 100, 50)
        elif shape_name == 'Rektangel':
            width = st.sidebar.slider(f"{shape_name} Bredde", 10, 200, 100)
            height = st.sidebar.slider(f"{shape_name} Højde", 10, 200, 50)
        elif shape_name == 'Trekant':
            base = st.sidebar.slider(f"{shape_name} bredde", 10, 200, 100)
            height = st.sidebar.slider(f"{shape_name} Højde", 10, 200, 100)
        elif shape_name == 'Ottekant':
            side = st.sidebar.slider(f"{shape_name} Sidelængde", 10, 100, 50)
        
        color = st.sidebar.color_picker(f"{shape_name} Farve", '#FF6347' if index == 0 else '#4682B4' if index == 1 else '#32CD32' if index == 2 else '#FFD700')

        if shape_name == 'Cirkel':
            shapes.append(Circle(radius, (x_position, y_position), color))
        elif shape_name == 'Rektangel':
            shapes.append(Rectangle(width, height, (x_position, y_position), color))
        elif shape_name == 'Trekant':
            shapes.append(Triangle(base, height, (x_position, y_position), color))
        elif shape_name == 'Ottekant':
            shapes.append(Octagon(side, (x_position, y_position), color))

    for shape in shapes:
        shape.draw(image)

    st.image(image, caption='@1ia.tech')
    if st.button('Gem billede'):
        image.save("OOPBilledeTingeling.png")
        st.success("Billedet er gemt!")
        

if __name__ == "__main__":
    main()