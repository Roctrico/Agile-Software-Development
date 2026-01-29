# Package imports. Each import provides functions or classes used later in the program.
import color_sensor
import color
import motor
import runloop
import hub
import time
from hub import port

#preset audio input. to be called on further along the script. pitch 60, duration 200ms.
hub.sound.beep(60, 200)
time.sleep(1)


while True:

    # Main loop that keeps the program running continuously. "async def main():" starts the loop. 
    async def main ():

        # Function for following the white line.This is made into a loop with "async Def white():".
        # This loop can be called back to when needed.
        async def white ():
            # When the color sensor detects white, the robot moves forward
            # by turning each wheel 150 degrees at speed 200.
            # A short beep is played as feedback.This beep repeats every rotation of the loop.
            if color_sensor.color(port.E) is color.WHITE:
                hub.sound.beep(300,20)
                motor.run_for_degrees (port.D, -150,200)
                motor.run_for_degrees (port.C, 150,200)
        runloop.run(white()) 

        # Function for detecting red.
        # When red is detected, the robot stops.
        async def red ():
            if color_sensor.color(port.E) is color.RED:
                motor.run_for_degrees (port.D, -150,200)
                motor.run_for_degrees (port.C, 150,200)
        runloop.run(red())
        
        # Function for searching when the line is lost (sensor sees black). 
        # The robot rotates in increasing angles left and right to try to relocate the white line. 
        # After each movement, the sensor checks again for white or red. # If found, the function "return" returns immediately to resume normal behaviour.
        async def black ():
          if color_sensor.color(port.E) is color.BLACK:
                hub.sound.beep(500,500)
                motor.run_for_degrees (port.D, 20, 200)
                await motor.run_for_degrees (port.C, 20, 200)
                if color_sensor.color(port.E) is color.WHITE:
                    return
                elif color_sensor.color(port.E) is color.RED:
                    return
                hub.sound.beep(500,200)
                motor.run_for_degrees (port.D, -40, 200)
                await motor.run_for_degrees (port.C, -40, 200)
                if color_sensor.color(port.E) is color.WHITE:
                    return
                elif color_sensor.color(port.E) is color.RED:
                    return
                hub.sound.beep(500,200)
                motor.run_for_degrees (port.D, 60, 200)
                await motor.run_for_degrees (port.C, 60, 200)
                if color_sensor.color(port.E) is color.WHITE:
                    return
                elif color_sensor.color(port.E) is color.RED:
                    return
                hub.sound.beep(500,200)
                motor.run_for_degrees (port.D, -80, 200)
                await motor.run_for_degrees (port.C, -80, 200)
                if color_sensor.color(port.E) is color.WHITE:
                    return
                elif color_sensor.color(port.E) is color.RED:
                    return
                hub.sound.beep(500,200)
                motor.run_for_degrees (port.D, 100, 200)
                await motor.run_for_degrees (port.C, 100, 200)
                if color_sensor.color(port.E) is color.WHITE:
                    return
                elif color_sensor.color(port.E) is color.RED:
                    return
                hub.sound.beep(500,200)
                motor.run_for_degrees (port.D, -120, 200)
                await motor.run_for_degrees (port.C, -120, 200)
                if color_sensor.color(port.E) is color.WHITE:
                    return
                elif color_sensor.color(port.E) is color.RED:
                    return
                hub.sound.beep(500,200)
                motor.run_for_degrees (port.D, 140, 200)
                await motor.run_for_degrees (port.C, 140, 200)
                if color_sensor.color(port.E) is color.WHITE:
                    return
                elif color_sensor.color(port.E) is color.RED:
                    return
                hub.sound.beep(500,200)
                motor.run_for_degrees (port.D, -160, 200)
                await motor.run_for_degrees (port.C, -160, 200)
                if color_sensor.color(port.E) is color.WHITE:
                    return
                elif color_sensor.color(port.E) is color.RED:
                    return
                hub.sound.beep(500,200)
                motor.run_for_degrees (port.D, 180, 200)
                await motor.run_for_degrees (port.C, 180, 200)
                if color_sensor.color(port.E) is color.WHITE:
                    return
                elif color_sensor.color(port.E) is color.RED:
                    return
                hub.sound.beep(500,200)
                motor.run_for_degrees (port.D, -200, 200)
                await motor.run_for_degrees (port.C, -200, 200)
                if color_sensor.color(port.E) is color.WHITE:
                    return
                elif color_sensor.color(port.E) is color.RED:
                    return
                hub.sound.beep(500,200)
                motor.run_for_degrees (port.D, 220, 200)
                await motor.run_for_degrees (port.C, 220, 200)
                if color_sensor.color(port.E) is color.WHITE:
                    return
                elif color_sensor.color(port.E) is color.RED:
                    return
                hub.sound.beep(500,200)
                motor.run_for_degrees (port.D, -240, 200)
                await motor.run_for_degrees (port.C, -240, 200)
                if color_sensor.color(port.E) is color.WHITE:
                    return
                elif color_sensor.color(port.E) is color.RED:
                    return
                hub.sound.beep(500,200)
                motor.run_for_degrees (port.D, 260, 200)
                await motor.run_for_degrees (port.C, 260, 200)
                if color_sensor.color(port.E) is color.WHITE:
                    return
                elif color_sensor.color(port.E) is color.RED:
                    return
                hub.sound.beep(500,200)
                motor.run_for_degrees (port.D, -280, 200)
                await motor.run_for_degrees (port.C, -280, 200)
                if color_sensor.color(port.E) is color.WHITE:
                    return
                elif color_sensor.color(port.E) is color.RED:
                    return
                hub.sound.beep(500,200)
                motor.run_for_degrees (port.D, 300, 200)
                await motor.run_for_degrees (port.C, 300, 200)
                if color_sensor.color(port.E) is color.WHITE:
                    return
                elif color_sensor.color(port.E) is color.RED:
                    return
                hub.sound.beep(500,200)
                motor.run_for_degrees (port.D, -320, 200)
                await motor.run_for_degrees (port.C, -320, 200)
                if color_sensor.color(port.E) is color.WHITE or color.RED:
                    return
                hub.sound.beep(500,200)
                motor.run_for_degrees (port.D, 340, 200)
                await motor.run_for_degrees (port.C, 340, 200)
                if color_sensor.color(port.E) is color.WHITE:
                    return
                elif color_sensor.color(port.E) is color.RED:
                    return
                hub.sound.beep(500,200)
                motor.run_for_degrees (port.D, -360, 200)
                await motor.run_for_degrees (port.C, -360, 200)
                if color_sensor.color(port.E) is color.WHITE:
                    return
                elif color_sensor.color(port.E) is color.RED:
                    return
                hub.sound.beep(500,200)
                motor.run_for_degrees (port.D, 380, 200)
                await motor.run_for_degrees (port.C, 380, 200)
                if color_sensor.color(port.E) is color.WHITE:
                    return
                elif color_sensor.color(port.E) is color.RED:
                    return
        runloop.run(black())
    runloop.run(main())
