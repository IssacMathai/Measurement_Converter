from tkinter import *
from functools import partial 
import random

class Welcome_Screen:
    def __init__(self, partner):
        
        # Formatting variables
        background_color = "light blue"
        
        # Welcome Screen GUI
        self.welcome_screen_frame = Frame(width=600, height=600, bg=background_color, pady=10)
        self.welcome_screen_frame.grid()

        # Main Heading (row 0)
        self.measurement_welcome_screen_label = Label(self.welcome_screen_frame, text="Measurement Converter", font=("Arial", "16", "bold"), bg=background_color, padx=10, pady=10)
        self.measurement_welcome_screen_label.grid(row=0)

        # Centimetres and Inches Button (row 1)
        self.cm_and_in_welcome_screen_button = Button(self.welcome_screen_frame, text="Centimetres and Inches", font=("Arial", "14"), command=self.Centimetres_and_Inches_Converter, padx=10, pady=10)
        self.cm_and_in_welcome_screen_button.grid(row=1)

    def Centimetres_and_Inches_Converter(self):
        get_Centimetres_and_Inches_Converter = Centimetres_and_Inches_Converter(self)
        get_Centimetres_and_Inches_Converter.Centimetres_and_Inches_Converter_text.configure(text="text goes here")

class Centimetres_and_Inches_Converter:
    def __init__(self, partner):
        
        # Formatting variables
        background = "lime green"

        # disable Centimetres and Inches button while window is open
        partner.cm_and_in_welcome_screen_button.config(state=DISABLED)

        # Centimetres and Inches Converter child window
        self.Centimetres_and_Inches_Converter_box = Toplevel()
        
        # If users press cross at top, closes Centimetres_and_Inches_Converter and 'releases' Centimetres_and_Inches_Converter button


        # GUI Frame
        self.Centimetres_and_Inches_Converter_frame = Frame(self.Centimetres_and_Inches_Converter_box, bg=background)
        self.Centimetres_and_Inches_Converter_frame.grid()

        # Centimetres and Inches Converter heading (row 0)
        self.Centimetres_and_Inches_Converter_heading = Label(self.Centimetres_and_Inches_Converter_frame, text="Centimetres and Inches Converter",
                                 font="arial 18 bold", bg=background, padx=10, pady=10)
        self.Centimetres_and_Inches_Converter_heading.grid(row=0)

        #User instructions (row 1)
        self.cm_and_in_instructions_label = Label(self.Centimetres_and_Inches_Converter_frame, text="Type in a measurement below and push the button you wish to convert the measurement to.",
                                        font="Arial 10 italic", wrap=300,
                                         justify=CENTER, bg=background,
                                        padx=10, pady=10)
        self.cm_and_in_instructions_label.grid(row=1)




# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Measurement Converter Tool")
    something = Welcome_Screen(root)
    root.mainloop()

