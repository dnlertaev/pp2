import pygame

def main():
    # Initialize Pygame
    pygame.init()
    
    # Create the screen
    screen = pygame.display.set_mode((800, 600))
    
    # Set up the clock
    clock = pygame.time.Clock()
    
    # Initial variable values
    radius = 15  # Brush radius
    mode = 'blue'  # Drawing mode (default - blue color)
    points = []  # List of points for drawing lines
    shapes = []  # List to store added shapes
    
    while True:
        # Get key states
        pressed = pygame.key.get_pressed()
        
        # Check if ALT and CTRL keys are held
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # Quit the program when the window is closed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return  # Quit the program with Ctrl + W
                if event.key == pygame.K_F4 and alt_held:
                    return  # Quit the program with Alt + F4
                if event.key == pygame.K_ESCAPE:
                    return  # Quit the program with Escape
                
                # Handle key presses to choose color
                if event.key == pygame.K_r:
                    mode = 'red'  # Choose red color
                elif event.key == pygame.K_g:
                    mode = 'green'  # Choose green color
                elif event.key == pygame.K_b:
                    mode = 'blue'  # Choose blue color
                elif event.key == pygame.K_e:
                    mode = 'eraser'  # Eraser mode (white color)
                elif event.key == pygame.K_c:
                    mode = 'color_select'  # Color selection mode from palette
                
                # Handle key presses to add shapes
                if event.key == pygame.K_s:
                    add_square(shapes)  # Add a square
                elif event.key == pygame.K_t:
                    add_right_triangle(shapes)  # Add a right triangle
                elif event.key == pygame.K_u:
                    add_equilateral_triangle(shapes)  # Add an equilateral triangle
                elif event.key == pygame.K_r:
                    add_rhombus(shapes)  # Add a rhombus
                    
            # Handle mouse events
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    radius = min(200, radius + 1)  # Increase brush radius (left mouse button)
                elif event.button == 3:
                    radius = max(1, radius - 1)  # Decrease brush radius (right mouse button)
            
            # Handle mouse motion events
            if event.type == pygame.MOUSEMOTION:
                position = event.pos
                points.append(position)  # Add new point to the list
                points = points[-256:]  # Limit the length of the list
                
        # Clear the screen
        screen.fill((0, 0, 0))
  
        # Draw lines between points
        i = 0
        while i < len(points) - 1:
            if mode == 'eraser':
                drawLineBetween(screen, i, points[i], points[i + 1], radius, 'white')  # Eraser
            elif mode == 'color_select':
                pygame.draw.circle(screen, (255, 255, 255), points[i], radius)  # Draw point of selected color
            else:
                drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)  # Draw line with selected color
            i += 1
        
        # Draw additional shapes
        for shape in shapes:
            pygame.draw.polygon(screen, (255, 255, 255), shape, 2)
        
        # Update the screen
        pygame.display.flip()
        
        # Cap the FPS
        clock.tick(60)

# Function to draw a line between two points
def drawLineBetween(screen, index, start, end, width, color_mode):
    # Calculate color based on index for color transition effect
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    
    # Determine color based on mode
    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    elif color_mode == 'eraser':
        color = (0, 0, 0)
    else:
        color = (255, 255, 255)  # Default to white
        
    # Calculate deltas and iterations for drawing line
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    # Draw the line
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

# Function to add a square to the list of shapes
def add_square(shapes):
    shapes.append([(50, 50), (150, 50), (150, 150), (50, 150)])

# Function to add a right triangle to the list of shapes
def add_right_triangle(shapes):
    shapes.append([(200, 50), (300, 50), (200, 150)])

# Function to add an equilateral triangle to the list of shapes
def add_equilateral_triangle(shapes):
    shapes.append([(350, 50), (450, 50), (400, 150)])

# Function to add a rhombus to the list of shapes
def add_rhombus(shapes):
    shapes.append([(500, 50), (600, 100), (500, 150), (400, 100)])

main()

# square - S
# circle - C
# triangle - T
# rhombus - R
