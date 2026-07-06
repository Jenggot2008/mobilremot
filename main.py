import pygame
import serial
import time

#==========================
# Serial
#==========================
ser = serial.Serial("COM4", 115200)
time.sleep(2)

#==========================
# Pygame
#==========================
pygame.init()
pygame.joystick.init()

if pygame.joystick.get_count() == 0:
    print("PXN tidak ditemukan!")
    exit()

joy = pygame.joystick.Joystick(0)
joy.init()

print("Joystick :", joy.get_name())

#==========================
# Gear
#==========================

gear = "N"

last_button16 = 0
last_button22 = 0
last_cmd = ""

while True:

    pygame.event.pump()

    steering = joy.get_axis(0)
    gas = joy.get_axis(2)
    rem = joy.get_axis(5)

    b16 = joy.get_button(16)
    b22 = joy.get_button(22)

    #==========================
    # Gear
    #==========================

    if b16 and not last_button16:
        gear = "D"
        print("Gear : DRIVE")

    if b22 and not last_button22:
        gear = "R"
        print("Gear : REVERSE")

    last_button16 = b16
    last_button22 = b22

    #==========================
    # Steering
    #==========================

    left = 0
    right = 0

    if steering < -0.30:
        left = 1

    elif steering > 0.30:
        right = 1

    #==========================
    # Motor
    #==========================

    maju = 0
    mundur = 0

    # Rem = Netral
    if rem > 0.80:

        gear = "N"

    else:

        if gas > 0.80:

            if gear == "D":
                maju = 1

            elif gear == "R":
                mundur = 1

    cmd = f"{maju},{mundur},{left},{right}\n"

    if cmd != last_cmd:
        ser.write(cmd.encode())
        print(cmd.strip(), "| Gear =", gear)

        last_cmd = cmd

    time.sleep(0.01)