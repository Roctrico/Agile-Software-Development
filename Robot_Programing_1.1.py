#Package Imports
import runloop
import color_sensor
import color
import motor
import runloop
import hub
import time
from hub import port


hub.sound.beep(500, 200)# pitch 60, duration 500ms
time.sleep(1)

while True:
#Movement commands for when sesor reads white/path
    async def main ():
        async def white ():
            if color_sensor.color(port.E) is color.WHITE:
                hub.sound.beep(400,200)
                await motor.run_for_degrees (port.D, -150, 200)
                motor.run_for_degrees (port.C, 150,200)
        runloop.run(white()) 
#Search command for when sensor reads black/Road
        async def black ():
          if color_sensor.color(port.E) is color.BLACK:
                hub.sound.beep(500,500)
                motor.run_for_degrees (port.D, 20, 200)
                await motor.run_for_degrees (port.C, 20, 200)
                if color_sensor.color(port.E) is color.WHITE:
                    return
                hub.sound.beep(500,200)
                motor.run_for_degrees (port.D, -40, 200)
                await motor.run_for_degrees (port.C, -40, 200)
                if color_sensor.color(port.E) is color.WHITE:
                    return
                hub.sound.beep(500,200)
                motor.run_for_degrees (port.D, 60, 200)
                await motor.run_for_degrees (port.C, 60, 200)
                if color_sensor.color(port.E) is color.WHITE:
                    return
                hub.sound.beep(500,200)
                motor.run_for_degrees (port.D, -80, 200)
                await motor.run_for_degrees (port.C, -80, 200)
                if color_sensor.color(port.E) is color.WHITE:
                    return
                hub.sound.beep(500,200)
                motor.run_for_degrees (port.D, 100, 200)
                await motor.run_for_degrees (port.C, 100, 200)
                if color_sensor.color(port.E) is color.WHITE:
                    return
                hub.sound.beep(500,200)
                motor.run_for_degrees (port.D, -120, 200)
                await motor.run_for_degrees (port.C, -120, 200)
                if color_sensor.color(port.E) is color.WHITE:
                    return
                hub.sound.beep(500,200)
                motor.run_for_degrees (port.D, 140, 200)
                await motor.run_for_degrees (port.C, 140, 200)
                if color_sensor.color(port.E) is color.WHITE:
                    return
                hub.sound.beep(500,200)
                motor.run_for_degrees (port.D, -160, 200)
                await motor.run_for_degrees (port.C, -160, 200)
                if color_sensor.color(port.E) is color.WHITE:
                    return
                hub.sound.beep(500,200)
                motor.run_for_degrees (port.D, 180, 200)
                await motor.run_for_degrees (port.C, 180, 200)
                if color_sensor.color(port.E) is color.WHITE:
                    return
                hub.sound.beep(500,200)
                motor.run_for_degrees (port.D, -200, 200)
                await motor.run_for_degrees (port.C, -200, 200)
                if color_sensor.color(port.E) is color.WHITE:
                    return
                hub.sound.beep(500,200)
                motor.run_for_degrees (port.D, 220, 200)
                await motor.run_for_degrees (port.C, 220, 200)
                if color_sensor.color(port.E) is color.WHITE:
                    return
                hub.sound.beep(500,200)
                motor.run_for_degrees (port.D, -240, 200)
                await motor.run_for_degrees (port.C, -240, 200)
                if color_sensor.color(port.E) is color.WHITE:
                    return
        runloop.run(black())
    runloop.run(main())



        

