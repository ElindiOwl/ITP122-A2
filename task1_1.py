def setup():
    # Adding the canvas size to 500 pixels in width and 500 pixels in height
    size(500, 500)
    
    # Adding a white background color to the canvas
    background('#FFFFFF')
    
    # Defining the number of concentric circles to be drawn
    num_circles = 9                      # Adding the value for the total number of circles
    
    # Defining the initial multiplier for calculating the radius of the first circle
    initial_multiplier = 50              # Adding the initial multiplier value
    
    # Adding a call to the function that draws the concentric circles
    draw_concentric_circles(
        center_x=width / 2,              # Adding the X-coordinate for the center of the circles
        center_y=height / 2,             # Adding the Y-coordinate for the center of the circles
        multiplier=initial_multiplier,   # Adding the multiplier for radius calculation
        num_circles=num_circles,         # Adding the number of circles to be drawn
        color='#FF0000',                 # Adding the color for the circles (red)
        stroke_weight_val=5              # Adding the stroke weight (thickness) for the circles
    )
    
def draw_concentric_circles(center_x, center_y, multiplier, num_circles, color, stroke_weight_val):
    # Adding no fill to the shapes, ensuring only the outlines are drawn
    no_fill()
    
    # Adding the specified color to the stroke of the circles
    stroke(color)
    
    # Adding the specified stroke weight to the circles
    stroke_weight(stroke_weight_val)
    
    # Adding a loop to iterate through the number of circles to be drawn
    for i in range(1, num_circles + 1):
        # Calculating the radius for the current circle by adding the multiplier times the loop index
        radius = multiplier * i
        
        # Adding the ellipse (circle) to the canvas with the calculated radius (py5coding.org, n.d., ellipse())
        ellipse(center_x, center_y, radius, radius)


if __name__ == '__main__':
     setup()