def setup():
     # Adding the canvas size to 500 pixels in width and 500 pixels in height
    size(500, 500)
    
    # Adding a white background color to the canvas
    background('#FFFFFF')
    
    # Adding parameters for the grid of circles
    num_rows = 9                      # Adding the number of rows in the grid
    num_cols = 9                      # Adding the number of columns in the grid
    dot_spacing = 50                  # Adding the spacing between the circles in the grid
    circle_offset = 25                # Adding an offset to center the grid on the canvas
    
    # Adding parameters for the concentric circles
    num_concentric = 4                # Adding the number of concentric circles
    radius_step = 53                  # Adding the step size between each concentric circle
    concentric_offset = 40            # Adding an offset for the concentric circles
    
    # Drawing the grid of alternating circles
    draw_grid(
        num_rows=num_rows,            # Adding the number of rows
        num_cols=num_cols,            # Adding the number of columns
        dot_spacing=dot_spacing,      # Adding the spacing between circles
        circle_offset=circle_offset,  # Adding the offset for the grid
        color_alternate=True          # Adding a flag to alternate colors
    )
    
    # Drawing the concentric circles
    draw_concentric_circles(
        num_concentric=num_concentric,  # Adding the number of concentric circles
        radius_step=radius_step,        # Adding the step size between circles
        concentric_offset=concentric_offset  # Adding the offset for the concentric circles
    )
    
def draw_grid(num_rows, num_cols, dot_spacing, circle_offset, color_alternate):
    # Adding a loop to iterate through each row
    for i in range(num_rows):
        # Adding a loop to iterate through each column
        for j in range(num_cols):
            # Calculating the x and y coordinates for the current circle
            x = width / 2 + (j - num_cols / 2) * dot_spacing + circle_offset  # Adding the x-coordinate
            y = height / 2 + (i - num_rows / 2) * dot_spacing + circle_offset  # Adding the y-coordinate
            
            # Determining the color based on the position of the circle
            if color_alternate and (i + j) % 2 == 0:
                stroke('#FF0000')     # Adding red outline for alternating circles
            else:
                stroke('#00FF00')     # Adding green outline for non-alternating circles
            
            # Adding no fill to the circles
            no_fill()
            
            # Adding a stroke weight of 4 pixels to the circles
            stroke_weight(4)
            
            # Defining the radius of the circles
            radius = 20               # Adding the radius value
            
            # Drawing the ellipse (circle) with the calculated coordinates and radius (py5coding.org, n.d., ellipse())
            ellipse(x, y, radius, radius)
            
def draw_concentric_circles(num_concentric, radius_step, concentric_offset):
    # Adding a black outline for the concentric circles
    stroke('#000000')
    
    # Adding a stroke weight of 4 pixels to the concentric circles
    stroke_weight(4)
    
    # Adding no fill to the concentric circles
    no_fill()
    
    # Adding a loop to draw each concentric circle
    for k in range(num_concentric):
        # Calculating the radius for the current concentric circle
        radius = concentric_offset + k * radius_step  # Adding the radius calculation
        
        # Drawing the ellipse (circle) with the calculated radius (py5coding.org, n.d., ellipse())
        ellipse(width / 2, height / 2, radius * 2, radius * 2)  # Adding the ellipse to the canvas 
        

if __name__ == '__main__':
     setup()