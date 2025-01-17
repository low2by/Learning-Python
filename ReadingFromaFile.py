# This imports the turtle graphics module.
import turtle

# The main function is where the main code of the program is written.
def main():

    # This line reads a line of input from the user.
    filename = input("Please enter drawing filename: ")

    # Create a Turtle Graphics window to draw in.
    t = turtle.Turtle()

    # The screen is used at the end of the program.
    screen = t.getscreen()

    # The next line opens the file for "r" or reading.
    file = open(filename, "r")

    # The following for loop reads the lines of the file one at a time
    for line in file:
        
        # strip removes newLine character and any empty spaces 
        text = line.strip()

        # splits the texts into peaces by the deliminate
        commandList = text.split(",")

        # get the drawing command
        command = commandList[0]

        if command == "goto":
            x = float(commandList[1])
            y = float(commandList[2])
            width = float(commandList[3])
            color = commandList[4].strip()
            t.width(width)
            t.pencolor(color)
            t.goto(x,y)
        elif command == "circle":
            radius = float(commandList[1])
            width = float(commandList[2])
            color = commandList[3].strip()
            t.width(width)
            t.pencolor(color)
            t.circle(radius)
        elif command == "beginfill":
            color = commandList[1].strip()
            t.fillcolor(color)
            t.begin_fill()
        elif command == "endfill":
            t.end_fill()
        elif command == "penup":
            t.penup()
        elif command == "pendown":
            t.pendown()
        else:
            print("Unknown command found in file:" ,command)

    # Close the File
    file.close()

    # Hide the turtal
    t.ht()

    # This causes the program to hold the turtle graphics window open
    screen.exitonclick()

    print("Program Execution Completed.")


# This code calls the main function to get everything started.    
if __name__ == '__main__':
    main()