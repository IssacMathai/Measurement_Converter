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

class Centimetres_and_Inches_Converter:
    def __init__(self, partner):

        # Formatting variables
        background = "lime green"
        conversion_history_list = ["8 cm is 3.15 in", "17.7 cm is 6.97 in", "2 in is 5.08 cm", "18.2 in is 46.23 cm", "80 cm is 31.50 in"]

        # Disable Centimetres and Inches button while window is open
        partner.cm_and_in_welcome_screen_button.config(state=DISABLED)

        # Centimetres and Inches Converter child window
        self.cm_and_in_box = Toplevel()

        # If users press cross at top, closes window and re-enables Centimetres and Inches button
        self.cm_and_in_box.protocol('WM_DELETE_WINDOW', partial(self.close_Centimetres_and_Inches_Converter, partner))

        # GUI Frame
        self.cm_and_in_frame = Frame(self.cm_and_in_box, bg=background)
        self.cm_and_in_frame.grid()

        # Centimetres and Inches Converter heading (row 0)
        self.cm_and_in_heading = Label(self.cm_and_in_frame, text="Centimetres and Inches Converter",
                                 font="arial 18 bold", bg=background, padx=10, pady=10)
        self.cm_and_in_heading.grid(row=0)

        # Conversion History Button
        self.conversion_history_button = Button(self.cm_and_in_frame, text="Conversion History", font=("Arial", "14"), command=lambda: self.Conversion_History(conversion_history_list), padx=10, pady=10)
        self.conversion_history_button.grid(row=1)

        # If list is empty, print message
        if len(conversion_history_list) == 0:
            self.conversion_history_button.config(state=DISABLED)

    def close_Centimetres_and_Inches_Converter(self, partner):
        # Put "Centimetres and Inches" button in welcome screen back to normal... 
        partner.cm_and_in_welcome_screen_button.config(state=NORMAL)
        self.cm_and_in_box.destroy()

    def Conversion_History(self, conversion_history_list):
        get_Conversion_History = Conversion_History(self, conversion_history_list)

class Conversion_History:
    def __init__(self, partner, conversion_history_list):

        # Formatting variables
        ch_background = "#f060f7"
        export_button_background = "grey"
        ch_dismiss_button_background = "grey"
        conversion_history_string = "" 

        # Disable Conversion History button while window is open
        partner.conversion_history_button.config(state=DISABLED)

        # Conversion History GUI child window
        self.conversion_history_box = Toplevel()

        # If users press cross at top, closes window and re-enables Conversion History button
        self.conversion_history_box.protocol('WM_DELETE_WINDOW', partial(self.close_Conversion_History, partner))

        # GUI Frame
        self.conversion_history_frame = Frame(self.conversion_history_box, width=300, bg=ch_background)
        self.conversion_history_frame.grid()

        # Heading (row 0)
        self.conversion_history_heading = Label(self.conversion_history_frame, text="Conversion History", font="arial 18 bold", bg=ch_background)
        self.conversion_history_heading.grid(row=0)

        # Instructions text (row 1)
        self.conversion_history_instructions_text = Label(self.conversion_history_frame, text="Your conversion history will appear below. "
                                                                                 "In order to export this data onto a text file, "
                                                                                 "push the export button.", font="Arial 10 italic",
                                                                                 justify=CENTER, bg=ch_background, wrap=350,
                                                                                 padx=10, pady=10)
        self.conversion_history_instructions_text.grid(row=1)

        # Print most recent 5 values
        if len(conversion_history_list) >=5:
            for value in range(0,5):
                # Get length of list, print value and subtract 1 so that the next newest item will be printed in the next loop 
                conversion_history_string += conversion_history_list[len(conversion_history_list) - value - 1]+ "\n"

        # There are less than 5 values on the list so print what's on the list in order of most recent to least recent
        else:
            for value in conversion_history_list:
                # Get length of list, print value and subtract 1 so that the next newest item will be printed in the next loop
                conversion_history_string += conversion_history_list[len(conversion_history_list) - conversion_history_list.index(value) - 1] + "\n"


        # Placeholder conversion history (row 2)
        self.conversion_history_values_label = Label(self.conversion_history_frame, text=conversion_history_string,
                                                    font="Arial 12", bg=ch_background)
        self.conversion_history_values_label.grid(row=2)

        # Export and Dismiss buttons frames
        self.export_dismiss_buttons_frame = Frame(self.conversion_history_frame)
        self.export_dismiss_buttons_frame.grid(row=3)

        # Export button (row 3)
        self.export_button = Button(self.export_dismiss_buttons_frame, text="Export", font="Arial 12", bg=export_button_background)
        self.export_button.grid(row=3)

        # Dismiss button (row 3)
        self.dismiss_button = Button(self.export_dismiss_buttons_frame, text="Dismiss", font="Arial 12", bg=ch_dismiss_button_background, command=partial(self.close_Conversion_History, partner))
        self.dismiss_button.grid(row=3, column=1)

    def close_Conversion_History(self, partner):
        #  Restore Conversion History button in centimetres and inches converter
        partner.conversion_history_button.config(state=NORMAL)
        self.conversion_history_box.destroy()



# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Measurement Converter Tool")
    something = Welcome_Screen(root)
    root.mainloop()