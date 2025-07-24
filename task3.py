def setup():
    # Adding the canvas size to 800 pixels in width and 500 pixels in height
    size(800, 500)
    
    # Adding a white background color to the canvas
    background('#FFFFFF')
    
    # Adding a black outline color for the lines
    stroke('#000000')
    
    # Adding a stroke weight of 5 pixels to the lines
    stroke_weight(5)
    
    # Defining parameters for the first pattern
    num_lines_first = 30                      # Adding the number of lines for the first pattern
    line_length_first = 150                   # Adding the length of each line in the first pattern
    
    # Defining parameters for the second pattern
    num_lines_second = 32                     # Adding the number of lines for the second pattern
    initial_spacing = 0                       # Adding the initial spacing for the second pattern
    spacing_increment = 0.1                   # Adding the spacing increment for the second pattern
    
    # Defining parameters for the third pattern
    num_lines_third = 15                      # Adding the number of lines for the third pattern
    line_length_third = 70                    # Adding the length of each line in the third pattern
    
    # Drawing the first pattern (First Column)
    draw_first_pattern(
        num_lines=num_lines_first,            # Adding the number of lines
        line_length=line_length_first,        # Adding the length of each line
        start_x=50,                           # Adding the starting x-coordinate
        start_y=90                            # Adding the starting y-coordinate
    )
    
    # Drawing the second pattern (Second Column)
    draw_second_pattern(
        num_lines=num_lines_second,           # Adding the number of lines
        line_length=line_length_first,        # Adding the length of each line
        initial_spacing=initial_spacing,      # Adding the initial spacing
        spacing_increment=spacing_increment,  # Adding the spacing increment
        start_x=330,                          # Adding the starting x-coordinate
        start_y=90                            # Adding the starting y-coordinate
    )
    
    # Drawing the third pattern (Third Column)
    draw_third_pattern(
        num_lines=num_lines_third,            # Adding the number of lines
        line_length_third=line_length_third,  # Adding the length of each line
        start_x=610,                          # Adding the starting x-coordinate
        start_y=103                           # Adding the starting y-coordinate
    )
    
    # Drawing the fourth pattern (Fourth Column)
    draw_fourth_pattern(
        num_lines=num_lines_third,            # Adding the number of lines
        line_length_third=line_length_third,  # Adding the length of each line
        start_x=680,                          # Adding the starting x-coordinate
        start_y=90                            # Adding the starting y-coordinate
    )
    
def draw_first_pattern(num_lines, line_length, start_x, start_y): 
    push_matrix()                             # Saving the current transformation matrix (py5coding.org, n.d., push_matrix())
    translate(start_x, start_y)               # Moving the origin to the starting point (py5coding.org, n.d., translate())
    for i in range(num_lines):
        # Drawing a line with the specified parameters
        line(0, i * 13, line_length, i * 13 - 50)
    pop_matrix()                              # Restoring the previous transformation matrix (py5coding.org, n.d., pop_matrix())
    
def draw_second_pattern(num_lines, initial_spacing, spacing_increment, start_x, start_y, line_length):
    push_matrix()                             # Saving the current transformation matrix (py5coding.org, n.d., push_matrix())
    translate(start_x, start_y)               # Moving the origin to the starting point
    for i in range(num_lines):
        current_spacing = initial_spacing + i * (spacing_increment * 4)  # Calculating current spacing
        # Drawing a line with the specified parameters
        line(0, i * current_spacing - 50, line_length, i * current_spacing)
    pop_matrix()                              # Restoring the previous transformation matrix (py5coding.org, n.d., pop_matrix())
    
def draw_third_pattern(num_lines, line_length_third, start_x, start_y):
    push_matrix()                             # Saving the current transformation matrix (py5coding.org, n.d., push_matrix())
    translate(start_x, start_y)               # Moving the origin to the starting point
    for i in range(num_lines):
        # Drawing a line with the specified parameters
        line(0, i * 25, line_length_third, i * 25 - 20)
    pop_matrix()                              # Restoring the previous transformation matrix (py5coding.org, n.d., pop_matrix())
    
def draw_fourth_pattern(num_lines, line_length_third, start_x, start_y):
    push_matrix()                             # Saving the current transformation matrix (py5coding.org, n.d., push_matrix())
    translate(start_x, start_y)               # Moving the origin to the starting point
    for i in range(num_lines):
        # Drawing a line with the specified parameters
        line(0, i * 25 - 20, line_length_third, i * 25)
    pop_matrix()                              # Restoring the previous transformation matrix (py5coding.org, n.d., pop_matrix())


if __name__ == '__main__':
     setup()