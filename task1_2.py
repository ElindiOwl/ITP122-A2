def setup():
    # Adding the canvas size to 500 pixels in width and 500 pixels in height
    size(500, 500)
    
    # Adding a white background color to the canvas
    background('#FFFFFF')
    
    # Adding the horizontal and vertical center coordinates of the canvas
    cx = width / 2                      # Adding the X-coordinate for the center of the circles
    cy = height / 2                     # Adding the Y-coordinate for the center of the circles
    
    # Adding no fill to the shapes, ensuring only the outlines are drawn
    no_fill()
    
    # Adding a stroke weight of 5 pixels to the outlines of the circles
    stroke_weight(5)
    
    # Defining the number of concentric circles to be drawn
    num_circles = 9                     # Adding the value for the total number of circles
    
    # Defining the multiplier for calculating the radius of each circle
    multiplier = 55                     # Adding the multiplier value for radius calculation
    
    # Defining an offset to add spacing between the circles
    offset = 10                         # Adding the offset value for better spacing
    
    # Defining the colors for alternating circles (green and blue)
    colors = ['#00FF00', '#0000FF']     # Adding the list of colors for alternating circles
    
    # Drawing the concentric circles with alternating colors
    for i in range(num_circles):
        # Alternating between the defined colors using modulo operation
        current_color = colors[i % 2]   # Adding the logic for alternating colors
        stroke(current_color)           # Adding the current color to the stroke
        
        # Calculating the radius for the current circle with added offset
        radius = offset + i * multiplier  # Adding the calculation for the circle's radius
        
        # Drawing the ellipse (circle) with the calculated radius (py5coding.org, n.d., ellipse())
        ellipse(cx, cy, radius, radius)  # Adding the ellipse to the canvas
    
    # Drawing the horizontal gap across the center of the canvas
    stroke('#FFFFFF')                   # Adding white color for the gap
    stroke_weight(65)                   # Adding a stroke weight of 65 pixels for the gap
    line(0, cy, width, cy)              # Adding a horizontal line across the center of the canvas



if __name__ == '__main__':
     setup()