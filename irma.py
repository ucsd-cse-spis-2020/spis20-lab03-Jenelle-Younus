# Jenelle Truong and Younus Ahmad
import turtle
import csv

def irma_setup():
    """Creates the Turtle and the Screen with the map background
       and coordinate system set to match latitude and longitude.

       :return: a tuple containing the Turtle and the Screen

       DO NOT CHANGE THE CODE IN THIS FUNCTION!
    """
    import tkinter
    turtle.setup(965, 600)  # set size of window to size of map

    wn = turtle.Screen()
    wn.title("Hurricane Irma")

    # kludge to get the map shown as a background image,
    # since wn.bgpic does not allow you to position the image
    canvas = wn.getcanvas()
    
    turtle.setworldcoordinates(-90, 0, -17.66, 45)  # set the coordinate system to match lat/long

    map_bg_img = tkinter.PhotoImage(file="images/atlantic-basin.gif")

    # additional kludge for positioning the background image
    # when setworldcoordinates is used
    canvas.create_image(-1175, -580, anchor=tkinter.NW, image=map_bg_img)

    
    t = turtle.Turtle()
    wn.register_shape("images/hurricane.gif")
    t.shape("images/hurricane.gif")

    return (t, wn, map_bg_img)

        

def irma():
    """
    Animates the path of hurricane Irma by iterating through each
    data point in irma.csv
    """

    # Do not change this line
    # t is the turtle, and you will not need the other variables
    (t, wn, map_bg_img) = irma_setup()

    hurricaneFile = "data/irma.csv"
    # The line below is a little magical. It opens the file,
    # with awareness of any errors that might occur.
    with open(hurricaneFile, 'r') as csvfile:
        # This line gives you an "iterator" you can use to get each line
        # in the file.
        pointreader = csv.reader(csvfile)
        # You'll need to add some code here, before the loop
        # One thing you'll need to figure out how to do is to
        # skip the first line of the file (which is the header).
        # You might use a boolean variable, or you can
        # look into Python's built-in next function
        #(https://docs.python.org/3/library/functions.html#next)
        # pointreader is an iterator
        next(pointreader)
        t.penup()
        t.setpos(-30.3, 16.4)   #Moves turtle onto screen
        t.pendown()
        for row in pointreader:
            # row is a list representing each line in the csv file
            # Each comma separated element is in its own index position
            t.setpos(float(row[3]), float(row[2]))  #Moves turtle to appropriate lat/log
            hurCategory(t, float(row[4])) #changes pen size and color and adds hurricane category 
            print("Date:", row[0], "Time:", row[1])
    # Hack to make sure a reference to the background image stays around
    # Do not remove or change this line
    return map_bg_img


# Feel free to add "helper" functions here
"""
This function checks the hurricane windspeed at each data point, assigns appropriate category/color
"""
def hurCategory(t, wSpeed):   #Prints category based on wind speed in data set
    if wSpeed >= 157:
        t.pen(pencolor = "red", pensize = "18")
        t.write("5")
    elif wSpeed >= 130 and wSpeed <= 156:
        t.pen(pencolor = "Orange", pensize = "12")
        t.write("4")
    elif wSpeed >= 111 and wSpeed <= 129:
        t.pen(pencolor = "yellow", pensize = "9")
        t.write("3")
    elif wSpeed >= 96 and wSpeed <= 110:
        t.pen(pencolor = "green", pensize = "6")
        t.write("2")
    elif wSpeed >= 74 and wSpeed <= 95:
        t.pen(pencolor = "blue", pensize = "3")
        t.write("1")
    else:
        t.pen(pencolor = "white", pensize = "1")
        
if __name__ == "__main__":
    bg=irma()
