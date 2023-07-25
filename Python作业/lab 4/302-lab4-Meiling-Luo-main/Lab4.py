

from sense_emu import SenseHat
import tim

s = SenseHat()
s.low_light = True

green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255, 255, 255) #c2
nothing = (0, 0, 0)
pink = (255, 105, 180)
grey = (220, 220, 220) #c1


    def trinket_logo(O=nothing, Y=yellow, B=blue, G=green):
        logo = [
            O, O, O, O, O, O, O, O,
            O, Y, Y, Y, B, G, O, O,
            Y, Y, Y, Y, Y, B, G, O,
            Y, Y, Y, Y, Y, B, G, O,
            Y, Y, Y, Y, Y, B, G, O,
            Y, Y, Y, Y, Y, B, G, O,
            O, Y, Y, Y, B, G, O, O,
            O, O, O, O, O, O, O, O,
        ]
        return logo
    trinket_logo("red","blue","yellow"):

    def raspi_logo(G=green, R=red, O=nothing):
        logo = [
            O, G, G, O, O, G, G, O,
            O, O, G, G, G, G, O, O,
            O, O, R, R, R, R, O, O,
            O, R, R, R, R, R, R, O,
            R, R, R, R, R, R, R, R,
            R, R, R, R, R, R, R, R,
            O, R, R, R, R, R, R, O,
            O, O, R, R, R, R, O, O,
        ]
        return logo

    def plus(W=white, O=nothing):
        logo = [
            O, O, O, O, O, O, O, O,
            O, O, O, W, W, O, O, O,
            O, O, O, W, W, O, O, O,
            O, W, W, W, W, W, W, O,
            O, W, W, W, W, W, W, O,
            O, O, O, W, W, O, O, O,
            O, O, O, W, W, O, O, O,
            O, O, O, O, O, O, O, O,
        ]
        return logo

    def equals(W=white, O=nothing):
        logo = [
            O, O, O, O, O, O, O, O,
            O, W, W, W, W, W, W, O,
            O, W, W, W, W, W, W, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, W, W, W, W, W, W, O,
            O, W, W, W, W, W, W, O,
            O, O, O, O, O, O, O, O,
        ]
        return logo

    def heart(P=pink, O=nothing):
        logo = [
            O, O, O, O, O, O, O, O,
            O, P, P, O, P, P, O, O,
            P, P, P, P, P, P, P, O,
            P, P, P, P, P, P, P, O,
            O, P, P, P, P, P, O, O,
            O, O, P, P, P, O, O, O,
            O, O, O, P, O, O, O, O,
            O, O, O, O, O, O, O, O,
        ]
        return logo

    def elephant(o=nothing, c1=grey, c2=white):
        logo = [
            o, o, c1, c1, o, o, o, o,
            o, c1, c1, c1, c1, c1, c1, o,
            c1, o, c1, c1, c1, c1, c1, c1,
            c1, c1, c1, c1, c1, c1, c1, c1,
            c1, c2, c2, c1, c1, c1, c1, c1,
            c1, o, c1, c1, c1, c1, c1, c1,
            c1, o, c1, c1, o, c1, c1, o,
            c1, o, c2, c1, o, c2, c1, o,
        ]
        return logo

pictures = [trinket_logo(), plus(), equals(), raspi_logo(), heart(), elephant()]
def getUserChoice():
    while True:
        try:
            choice = int(input("Choose one to display (0. to exit) 1. Logo 2. Plus sign 3. Equals sign 4. Raspberry 5. Heart 6. Elephant 0. Exit"))
        except:
            print("Try Again")
            return choice
        else:
            return choice

while True:
    choice = getUserChoice()
    if choice == 0:
        break
    elif choice > 6:
        print("Try Again")
    else:
        s.set_pixels(pictures[choice]())