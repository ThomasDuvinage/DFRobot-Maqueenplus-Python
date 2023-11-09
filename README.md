# DFRobot-Maqueenplus-Python

Python library for the Maqueen Plus robot developed by DFRobot. 

This library is a python version of the one proposed by DFRobot used for block coding. 

This version has been developed for students to let them play and enjoy coding this nice little robot.

Link to DFRobot page : [https://www.dfrobot.com/product-2026.html]

# Usage 

- Create robot object

Instantiate the robot object 

```python
import microbit
import lib_robot_maqueen as mqn
import time #can be removed if not used

mq = mqn.MaqueenPlus()
```

# Methods 

### Move the robot
Move the robot along 4 axis :
- F -> forward
- B -> backward 
- L -> left
- R -> right 

Function definition :
```python
def move(speed, dir):
    """
    speed(pwm) : 0 -> 255
    dir(string) : "F" or "B" or "L" or "R"
    """
```

Example :
```python 
    mq.move(70, "F")
    time.sleep(1) #wait for 1s
    mq.move(70, "R")
```

To move the robot you can also use the motorControl method.

Function definition :
```python
def motorControl(self, mot, dir, spd):
    """
        mot left: MT_L ; mot right: MT_R
        dir (forward): 1; dir (backward): 2
        spd max: 255; stop: 0
    """
```

Example :
```python 
    mq.motorControl(mq.MT_L,2,50)
    mq.motorControl(mq.MT_R,2,70)
```

### Move the robot for a precise distance
MaqueenPlus is equipped with wheel encoders. The function goto uses the wheel encoders to turn or move the robot over an exact number of encoder ticks:
- F -> drive a number of encoder ticks forward
- L -> turn left for a number of encoder ticks
- R -> turn right for a number of encoder ticks

Function definition :
```python
def goto(self, dir, spd, dist):
    """
        mot left: MT_L ; mot right: MT_R
        dir(string) : "F" or "L" or "R"
        spd max: 255; stop: 0
        dist: the number of encoder ticks the robot should move
    """
```

Example :
```python
    # drive forward with PWM speed 200 for 400 encoder ticks
    mq.goto("F", 200, 400)

    # turn left with PWM speed 70 for 144 ticks (about 180 degrees)
    mq.goto("L", 70, 144)
```

### Stop 
Stop the robot 

Function definition:
```python
    def stop(self):
        """Stop the robot 
        """
```

Example:
```python
    mq.stop()
```

### Control ServoMotor
You can move three servos with the version of the library, S1, S2, S3.

Function definition:
```python
    def servo(self, number, angle):
        """Move a servo for a given angle

        Args:
            number (int): number of the servo to move
            angle (int): rotating angle (min=0  max=180)
        """
```

Example:
```python
    mq.servo(mq.S3,90)
    time.sleep(1)
    mq.servo(mq.S3,0)
```

### Line tracking sensor
Read line tracking sensor state.
Not all the functions proposed by DFRobot have been implemented.
It is up to you to do so.

Function definition:
```python
    def getLine(self):
        """Read line tracking state

        Returns:
            dictionary of [int]: 0 : white / 1 : black
            valid keys for the dictionary are: "L3", "L2", "L1", "R1", "R2", "R3"
        """
```

Example:

```python
    #Read line tracking sensor state
    line = mq.getLine()
    print(line["L1"])
    print(line["R1"])
```

### Ultrasonic sensor 
Get the distance between the robot and an object. An optional argument maxDist was added so you can choose the range of the sensor, which can be important to limit delays in your program. The default setting is 0.4 meters.

Function definition:
```python
    def ultrasonic(self,maxDist=0.4):
        """Get the distance between the robot and an object.

        Args:
            [float, optional] The maximum distance in meters
                              If function is called with no arguments, defaults to 0.4

        Returns:
            [float]: distance to the object if one is detected, else max value.
        """
```

Example:

```python
    distance = mq.ultrasonic()
    distance = mq.ultrasonic(0.8)
```

### Motor Speed 
Get the linear speed of a given motor. 
INFO : This method has no been tested yet but you can test it and set an issue for feedback. 


Function definition:
```python
    def motorSpeed(self, mot):
        """Get the linear speed of a given motor 

        Args:
            mot (int): object attribute define in the constructor (MG, MD)

        Returns:
            [type]: [description]
        """
```

Example:

```python
    mq.move(70, "F")
    time.sleep(1) #delay is necessary. Otherwise the robot read the speed before the motor started.
    spd = mq.motorSpeed(mq.MT_L)
    display.show(str(spd))
    time.sleep(5)
    mq.stop()
```

### RGB Lights
Turn on/off the rgb light of your choice with the color you want.

* RGB LED choice:
RGB_L : left led,
RGB_R : right led,
RGB_ALL : both leds

* Color choice:
RED,
GREEN,
BLUE,
YELLOW,
PINK,
CYAN,
WHITE,
OFF

Function declaration:
```python
    def RGBLight(self, rgbshow, color):
        """Turn on/off the rbg light of your choice with the color you want.


        Args:
            rgbshow (int): rgb light object attribute defined in the constructor :
                RGB_L : left led,
                RGB_R : right led,
                RGB_ALL : both leds

            color (int): color of the led:
                RED,GREEN,
                BLUE,YELLOW,
                PINK,CYAN,
                WHITE, OFF
        """
```

Example:
```python
    mq.RGBLight(mq.RGB_L,mq.RED)
```

### Read Encoders
Read the values of the wheel encoders

Function definition:
```python
    def getEncoders(self):
        """Read the values of the wheel encoders
        
        Returns:
            [tuple of 2 int's]: Value of the left encoder and right encoder
        """
```

Example:
```python
    encoders = mq.getEncoders()
    print(encoders[0])
    print(encoders[1])
```

### Clear Encoders 
Reset the values of the wheel encoders to 0

Function definition:
```python
    def clearEncoders(self):
        """Reset the values of the wheel encoders to 0
        """
```

Example:
```python
    mq.clearEncoders()
```

### Version history
- Version 1.0: Initial version
- Version 2.0: Compacted code style (short variable names, delete unnecessary space characters) to work around memory constraints and find space for adding functionality. Added goto function for moving the robot with use of the decoders. Added optional maximum distance argument to the ultrasonic function. Should still work with the micro:bit V1. if more functions to this library are added, you will probably need to equip your Maqueen Plus with the micro:bit V2. I am considering making a separate version of this library for the micro:bit V2
