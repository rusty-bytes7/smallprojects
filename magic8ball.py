#this is a project for rusty's magic 8 ball for the sense hat!

from sense_hat import SenseHat
import random

sense = SenseHat()

purple = (160,32,240)
red = (255,0,0)
orange = (255,69,0)
yellow = (255,215,0)
green = (0,255,0)
blue = (0,191,255)
pink = (255,20,147)
w = (255,255,255)
b = (0,0,0)

possiblemessages = ["I will allow it.", "Try again after my nap.", "Sounds like you need a snack!", "That sounds like a you problem.", "Only if it involves treats!", "Sounds purrfect.", "All signs point to: nap!", "Outlook fuzzy, like my belly.", "I'm busy loafing.", "Hiss-terically unlikely.", "The stars align!", "Pawsitively!", "You'll land on your feet!", "Go for it!", "No doubts, only purrs!"]

rainbow = [red,orange,yellow,green,blue,purple,pink]

sense.show_message("Welcome to Rusty's Magic 8 Ball!", text_colour = purple, scroll_speed = .08)
sense.show_message("Shake to see what Rusty has to say!",text_colour = pink, scroll_speed = .08)

while True:
    messagenumber = random.randint(0,14)
    randomcolor = random.randint(0,6)
    acceleration = sense.get_accelerometer_raw()
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']

    x = abs(x)
    y = abs(y)
    z = abs(z)

    if x > 3 or y > 3 or z > 3:
        sense.show_message(possiblemessages[messagenumber], scroll_speed = .08, text_colour = rainbow[randomcolor])
        continue
    else:
        sense.clear()