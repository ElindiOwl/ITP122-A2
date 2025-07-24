def setup():
    # Adding the canvas size to 500 pixels in width and 500 pixels in height
    size(500, 500)
    
    # Adding a white background color to the canvas
    background('#FFFFFF')
    
    # Adding a clockwise rotation of approximately 6 degrees to the entire drawing space (py5coding.org, n.d., radians())
    rotate(radians(6))                      # Adding rotation to the canvas
    
    # Adding parameters for the grey lines
    line_1_x = 300                          # Adding the x-coordinate for the first grey line
    line_2_x = 400                          # Adding the x-coordinate for the second grey line
    
    # Drawing two grey lines
    stroke_weight(5)                        # Adding a stroke weight of 5 pixels to the lines
    stroke('#999999')                       # Adding grey color to the lines
    line(300, 0, line_1_x, height)          # Adding the first grey line
    line(400, 0, line_2_x, height)          # Adding the second grey line
    
    no_stroke()                             # Removing the outline for the dots to ensure only the fill is visible
    
    # Adding parameters for the dots
    num_dots = 28                           # Adding the number of blue dots per line
    num_red_dots = 16                       # Adding the number of red dots per line
    num_green_dots = 40                     # Adding the number of green dots per line
    dot_spacing = width / (num_dots - 2)    # Adding the spacing between dots
    
    # Adding offsets for better positioning of the dots
    blue_dots_offset = 15                   # Adding offset for blue dots
    red_dots_offset = 8                     # Adding offset for red dots
    green_dots_offset = 5                   # Adding offset for green dots
    
    # Drawing blue dots
    stroke('#0000FF')                       # Adding blue color to the stroke of the dots
    stroke_weight(14)                       # Adding a stroke weight of 14 pixels to the blue dots
    for i in range(num_dots):
        # Calculating the x-coordinate for the current blue dot
        x = i * dot_spacing + blue_dots_offset  # Adding the x-coordinate calculation
        y = height / 4                      # Adding the y-coordinate for the blue dots
        point(x, y)                         # Adding the blue dot to the canvas (py5coding.org, n.d., point())
    
    # Drawing red dots
    stroke('#FF0000')                       # Adding red color to the stroke of the dots
    for i in range(num_red_dots):
        # Calculating the x-coordinate for the current red dot
        x = i * dot_spacing - red_dots_offset  # Adding the x-coordinate calculation
        y = height / 2                      # Adding the y-coordinate for the red dots
        point(x, y)                         # Adding the red dot to the canvas (py5coding.org, n.d., point())
    
    # Drawing green dots
    stroke('#00FF00')                       # Adding green color to the stroke of the dots
    for i in range(num_green_dots):
        # Creating a gap in the green dots by skipping dots within a certain range
        if line_1_x - 10 < i * dot_spacing < line_2_x + 10:
            continue                        # Skipping the dot to create a gap
        
        # Calculating the x-coordinate for the current green dot
        x = i * dot_spacing - green_dots_offset  # Adding the x-coordinate calculation
        y = 3 * height / 4                  # Adding the y-coordinate for the green dots
        point(x, y)                         # Adding the green dot to the canvas (py5coding.org, n.d., point())

    
if __name__ == '__main__':
     setup()