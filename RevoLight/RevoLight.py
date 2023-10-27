import pygame

pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Car Simulation")
font = pygame.font.Font(None, 36)

car_image = pygame.image.load("RevoLight/volkswagen-polo.png")  # Load the car image
headlights_on_image = pygame.image.load("RevoLight/HeadLights-On.png")  # Load the headlights on image
reverse_lights_image = pygame.image.load("RevoLight/Reverse_Light.png")  # Load the reverse lights image

night = "Press 'N' for Night"
text_surface = font.render(night, True, (255, 255, 255))

car_x, car_y = 100, 100
headlights_on = False
reverse_lights_on = False
night_time = False

# Define initial car speed
car_speed = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                car_speed = -5  # Move left
            elif event.key == pygame.K_RIGHT:
                car_speed = 5  # Move right
            elif event.key == pygame.K_n:
                night_time = not night_time  # Toggle night mode
        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                car_speed = 0  # Stop moving

    # Check if car is reversing
    reverse = False
    if car_speed < 0:
        reverse = True

    if night_time:
        headlights_on = True
        if reverse:
            reverse_lights_on = True
        else:
            reverse_lights_on = False
    else:
        headlights_on = False
        reverse_lights_on = False

    screen.blit(text_surface, (10, 10))
    # Update car position
    car_x += car_speed

    screen.fill((0, 0, 0) if night_time else (255, 255, 255))  # Set the background color

    # Draw the car image
    screen.blit(car_image, (car_x, car_y))

    if headlights_on:
        # Draw the headlights on top of the car
        screen.blit(headlights_on_image, (car_x + 0, car_y - 0))

    if reverse_lights_on:
        # Draw the reverse lights on the rear of the car
        screen.blit(reverse_lights_image, (car_x + 0, car_y + 0))

    pygame.display.flip()

pygame.quit()
