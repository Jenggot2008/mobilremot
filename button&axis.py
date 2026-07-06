import pygame

pygame.init()
pygame.joystick.init()

if pygame.joystick.get_count() == 0:
    print("Joystick tidak ditemukan")
    exit()

joy = pygame.joystick.Joystick(0)
joy.init()

print("Nama:", joy.get_name())
print("Axis:", joy.get_numaxes())
print("Buttons:", joy.get_numbuttons())

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # Tombol
        elif event.type == pygame.JOYBUTTONDOWN:
            print(f"Button {event.button} ditekan")

        # Axis
        elif event.type == pygame.JOYAXISMOTION:
            print(f"Axis {event.axis} = {event.value:.3f}")