import pygame
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
width, height = 1280, 720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Image Switcher")

# Load images
images = [
    pygame.image.load("G:\\Bot API\\face\\face\\a.png"),  
    pygame.image.load("G:\\Bot API\\face\\face\\b.png"),  
    pygame.image.load("G:\\Bot API\\face\\face\\c.png")   
]
current_image_index = 0

# Function to display image
def display_image(index):
    screen.fill((0, 0, 0))  # Clear screen with black
    img = pygame.transform.scale(images[index], (width, height))
    screen.blit(img, (0, 0))
    pygame.display.flip()

# Display the initial image
display_image(current_image_index)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                current_image_index = 0
            elif event.key == pygame.K_DOWN:
                current_image_index = 1
            elif event.key == pygame.K_LEFT:
                current_image_index = 2
            display_image(current_image_index)

# Quit pygame
pygame.quit()
sys.exit()
