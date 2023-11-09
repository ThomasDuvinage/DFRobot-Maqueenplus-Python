import microbit
import machine
import lib_robot_maqueen as mqn
import time

mq = mqn.MaqueenPlus()

#### Example #####

mq.move(70, "F")
time.sleep(1)
mq.move(70, "R")

##################

# add your code here... :-)
