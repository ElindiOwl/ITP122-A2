# Importing "random" library
import random

# Defining global tile size
tile_size = 25

def setup():
    # Adding the canvas size to 500 pixels in width and 500 pixels in height
    size(500, 500)                 # Adding the canvas size
    
    # Adding a white background color to the canvas
    background('#FFFFFF')          # Adding the background color
    
    # Removing the outline for the shapes to ensure only the filled shapes are visible
    no_stroke()                    # Adding no stroke
    
    # Defining the four different tile colors
    colors = {
        'black': '#000000',        # Adding black color
        'red': '#FF0000',          # Adding red color
        'green': '#00FF00',        # Adding green color
        'blue': '#0000FF'          # Adding blue color
    }
    
    # Filling the canvas with tiles by calling the function that handles tile placement
    fill_canvas_with_tiles(
        tile_size=tile_size,       # Adding the size of each tile
        colors=colors,             # Adding the dictionary of colors
        rows=20,                   # Adding the number of rows
        cols=20                    # Adding the number of columns
    )
    
def fill_canvas_with_tiles(tile_size, colors, rows, cols):
    # Adding a loop to iterate through each row
    for row in range(rows):
        # Adding a loop to iterate through each column
        for col in range(cols):
            # Randomly selecting a tile type (color) from the colors dictionary values (py5coding.org, n.d., random_choice())
            tile_type = random.choice(list(colors.values()))  # Adding random tile type selection
            
            # Randomly selecting a rotation angle from 0, 90, 180, 270 degrees (py5coding.org, n.d., random_choice())
            rotation = random.choice([0, 90, 180, 270])  # Adding random rotation selection
            
            # Calculating the position of the tile based on the current row and column
            x = col * tile_size    # Adding the x-coordinate calculation
            y = row * tile_size    # Adding the y-coordinate calculation
            
            # Drawing the tile by calling the draw_tile function with the calculated parameters
            draw_tile(
                tile_type=tile_type,  # Adding the tile type (color)
                x=x,                  # Adding the x-coordinate
                y=y,                  # Adding the y-coordinate
                rotation=rotation     # Adding the rotation angle
            )
            
def draw_tile(tile_type, x, y, rotation):
    with push_matrix():             # Adding push_matrix to isolate transformation
        # Moving to the center of the tile
        translate(x + tile_size / 2, y + tile_size / 2)  # Adding translation to center
        
        # Applying rotation to the tile
        rotate(radians(rotation))   # Adding rotation
        
        # Moving back to the top-left corner of the tile
        translate(-tile_size / 2, -tile_size / 2)  # Adding translation back to top-left
        
        # Drawing the first triangle (white)
        fill('#FFFFFF')             # Adding white fill for the first triangle
        triangle(0, 0, tile_size, 0, tile_size, tile_size)  # Adding the first triangle (py5coding.org, n.d., triangle())
        
        # Drawing the second triangle (colored)
        fill(tile_type)             # Adding color fill for the second triangle
        triangle(0, 0, 0, tile_size, tile_size, tile_size)  # Adding the second triangle (py5coding.org, n.d., triangle())
        

if __name__ == '__main__':
    setup()
