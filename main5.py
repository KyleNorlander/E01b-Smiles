#!/usr/bin/env python3

import utils, open_color, arcade

utils.check_version((3,7))

SCREEN_WIDTH = 800 #screen width is 800 pixels
SCREEN_HEIGHT = 600 #screen height is 600 pixels
SCREEN_TITLE = "Smiley Face Example" #titles the screen 

class Faces(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Show the mouse cursor
        self.set_mouse_visible(True) #This allows the users mouse to stay visiblw

        self.x = SCREEN_WIDTH / 2 #changing this to 1, for example, offsets the original placement of the smiley and cuts it in half vertically on the right side of the screen
        self.y = SCREEN_HEIGHT / 2 #changing this to 1, for example, offsets the original placement of the smiley and cuts it in half horizonatally at the top of the screen

        arcade.set_background_color(open_color.white) #sets the background color to white

    def on_draw(self):
        """ Draw the face """ #This is placing the smiley in the middle of the screen to begin with
        arcade.start_render()
        face_x,face_y = (self.x,self.y) #is this connected to lines 46-49? These lines place the full picture in the middle of the screen with the coordinates making up a smiley and not a terrifying cyclops or some other beast 
        smile_x,smile_y = (face_x + 0,face_y - 10)
        eye1_x,eye1_y = (face_x - 30,face_y + 20) 
        eye2_x,eye2_y = (face_x + 30,face_y + 20)
        catch1_x,catch1_y = (face_x - 25,face_y + 25) 
        catch2_x,catch2_y = (face_x + 35,face_y + 25) 

        arcade.draw_circle_filled(face_x, face_y, 100, open_color.yellow_3) #This is the line that make up the yellow circle background
        arcade.draw_circle_outline(face_x, face_y, 100, open_color.black,4) #This is the line that creates the solid black outline for the smiley
        arcade.draw_ellipse_filled(eye1_x,eye1_y,15,25,open_color.black) #These two lines are the black circles, or eyes
        arcade.draw_ellipse_filled(eye2_x,eye2_y,15,25,open_color.black)
        arcade.draw_circle_filled(catch1_x,catch1_y,3,open_color.gray_2) #These two lines are made for the two reflections in the eyes
        arcade.draw_circle_filled(catch2_x,catch2_y,3,open_color.gray_2) 
        arcade.draw_arc_outline(smile_x,smile_y,60,50,open_color.black,190,350,4) #This line is the arc, or the actual curved line making the smile


    def on_mouse_motion(self, x, y, dx, dy): #I think these must be the lines that, once the mouse is in the window, tracks movement of the mouse based on its current xy coordinates
        """ Handle Mouse Motion """
        self.x = x
        self.y = y



window = Faces()
arcade.run()