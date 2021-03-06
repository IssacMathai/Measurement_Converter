from tkinter import *
from functools import partial 
import re


class WelcomeScreen:
    def __init__(self, parent):
        # Formatting variables
        background_colour = "light blue"
        cm_and_in_button_colour = "lime green"
        m_and_ft_button_colour = "orange"

        # Create conversion history list
        WelcomeScreen.conv_history_list = []

        # Frame
        self.welcome_screen_frame = Frame(width=200, height=200, bg=background_colour, pady=10)
        self.welcome_screen_frame.grid()

        # Main Heading (row 0)
        self.measurement_welcome_screen_label = Label(self.welcome_screen_frame, text = "Measurement Converter", font="Arial 20 bold", bg=background_colour, padx=10)
        self.measurement_welcome_screen_label.grid(row=0)

        # Welcome Screen Instructions (row 1)
        self.instructions_welcome_screen_label = Label(self.welcome_screen_frame, text="Choose the units you will convert between below.", font="Arial 10 italic", bg=background_colour, padx=10, pady=10)
        self.instructions_welcome_screen_label.grid(row=1)

        # Welcome Screen Buttons Frame
        self.welcome_screen_buttons_frame = Frame(self.welcome_screen_frame, bg=background_colour)
        self.welcome_screen_buttons_frame.grid(row=2)

        # Centimetres and Inches Button (row 2)
        self.cm_and_in_welcome_screen_button = Button(self.welcome_screen_buttons_frame, text="Centimetres and Inches", font="Arial 10 bold", bg=cm_and_in_button_colour, command=self.CentimetresAndInchesConverter, padx=10, pady=10)
        self.cm_and_in_welcome_screen_button.grid(row=2, column=0, padx=5)

        # Metres and Feet Button (row 2)
        self.m_and_ft_welcome_screen_button = Button(self.welcome_screen_buttons_frame, text="Metres and Feet", font="Arial 10 bold", bg=m_and_ft_button_colour, command=self.MetresAndFeetConverter, padx=10, pady=10)
        self.m_and_ft_welcome_screen_button.grid(row=2,column=1, padx=5)
    
    def CentimetresAndInchesConverter(self):
        get_CentimetresAndInchesConverter = CentimetresAndInchesConverter(self)
    
    def MetresAndFeetConverter(self):
        get_MetresAndFeetConverter = MetresAndFeetConverter(self)

class CentimetresAndInchesConverter:
    def __init__(self, partner):
        
        # Formatting variables
        background = "lime green"
        to_cm_button_background = "yellow"
        to_in_button_background = "#e9d3f2"

        # disable converter buttons in welcome screen when window is opened
        partner.cm_and_in_welcome_screen_button.config(state=DISABLED)
        partner.m_and_ft_welcome_screen_button.config(state=DISABLED)

        # Centimetres and Inches Converter child window
        self.cm_and_in_box = Toplevel()
        
        # If users press cross at top, closes window and re-enables Centimetres and Inches button
        self.cm_and_in_box.protocol('WM_DELETE_WINDOW', partial(self.close_CentimetresAndInchesConverter, partner))

        # GUI Frame
        self.cm_and_in_frame = Frame(self.cm_and_in_box, bg=background)
        self.cm_and_in_frame.grid()

        # Centimetres and Inches Converter heading (row 0)
        self.cm_and_in_heading = Label(self.cm_and_in_frame, text="Centimetres and Inches Converter",
                                 font="arial 18 bold", bg=background, padx=10, pady=10)
        self.cm_and_in_heading.grid(row=0)

        # User instructions (row 1)
        self.cm_and_in_instructions_label = Label(self.cm_and_in_frame, text="Type in a measurement below and push the button you wish to convert the measurement to.",
                                        font="Arial 10 italic", wrap=300,
                                         justify=CENTER, bg=background,
                                        padx=10, pady=10)
        self.cm_and_in_instructions_label.grid(row=1)

        # Measurement input box (row 2)
        self.to_convert_cm_in_input = Entry(self.cm_and_in_frame, width=20, font="Arial 20 bold")
        self.to_convert_cm_in_input.grid(row=2)

        # "To Convert" buttons frame
        self.to_cm_and_in_buttons_frame = Frame(self.cm_and_in_frame, bg=background)
        self.to_cm_and_in_buttons_frame.grid(row=3, pady=10)

        # To Centimetres button (row 3)
        self.to_cm_button = Button(self.to_cm_and_in_buttons_frame, text="To Centimetres", font="Arial 10 bold", bg=to_cm_button_background, command=lambda: self.cm_in_convert(cm_inapplicable=0, inch_inapplicable=0), padx=10, pady=10)
        self.to_cm_button.grid(row=3, column=0, padx=5)

        # To Inches button (row 3)
        self.to_in_button = Button(self.to_cm_and_in_buttons_frame, text="To Inches", font="Arial 10 bold", bg=to_in_button_background, command=lambda: self.cm_in_convert(cm_inapplicable=0, inch_inapplicable=0.0000000000000001), padx=10, pady=10)
        self.to_in_button.grid(row=3,column=1, padx=5)

        # Conversion Result subheading (row 4)
        self.cm_and_in_result_subheading_label = Label(self.cm_and_in_frame, font="Arial 14", bg=background, pady=10, text="Conversion Result:")
        self.cm_and_in_result_subheading_label.grid(row=4)

        # Conversion Result (row 5)
        self.cm_and_in_result_label = Label(self.cm_and_in_frame, font = "Arial 11 bold", bg=background, fg="blue", pady=10, text="")
        self.cm_and_in_result_label.grid(row=5)

        # Conversion History, Help and Dismiss buttons frame (row 6)
        self.cm_and_in_history_help_dismiss_buttons_frame = Frame(self.cm_and_in_frame, bg=background)
        self.cm_and_in_history_help_dismiss_buttons_frame.grid(row=6, pady=10)

        # Conversion History button (row 6)
        self.conversion_history_button = Button(self.cm_and_in_history_help_dismiss_buttons_frame, text="Conversion History", font="Arial 10 bold", command=lambda: self.ConversionHistory(WelcomeScreen.conv_history_list), padx=10, pady=10)
        self.conversion_history_button.grid(row=6,column=0, padx=5)

        # If list is empty, disable history button
        if len(WelcomeScreen.conv_history_list) == 0:
            self.conversion_history_button.config(state=DISABLED)

        # Help button (row 6)
        self.help_button = Button(self.cm_and_in_history_help_dismiss_buttons_frame, text="Help", font="Arial 10 bold", command=self.Help, padx=10, pady=10)
        self.help_button.grid(row=6, column=1, padx=5)

        # Dismiss button (row 6)
        self.cm_and_in_dismiss_button = Button(self.cm_and_in_history_help_dismiss_buttons_frame, text="Dismiss", font="Arial 10 bold", command=partial(self.close_CentimetresAndInchesConverter, partner), padx=10, pady=10)
        self.cm_and_in_dismiss_button.grid(row=6, column=2, padx=5)

    def close_CentimetresAndInchesConverter(self, partner):
        # Restore converter buttons in welcome screen
        partner.cm_and_in_welcome_screen_button.config(state=NORMAL)
        partner.m_and_ft_welcome_screen_button.config(state=NORMAL)
        self.cm_and_in_box.destroy()
    
    def cm_in_convert(self, inch_inapplicable, cm_inapplicable):
        
        # Format variables
        error_message_background = "red"
        input_box_error_background = "pink"

        # Get user input from input box
        to_convert_cm_in = self.to_convert_cm_in_input.get()

        try:
            to_convert_cm_in = float(to_convert_cm_in)
            cm_in_errors = "no"

            # Convert to centimetres if input is 0 or greater
            if inch_inapplicable == 0 and to_convert_cm_in >= inch_inapplicable:
                cm = (to_convert_cm_in * 2.54)
                to_convert_cm_in = self.rounding(to_convert_cm_in)
                cm = self.rounding(cm)
                answer = "{} in is {} cm".format(to_convert_cm_in, cm)

            # Convert to inches if input is 0 or greater
            elif cm_inapplicable == 0 and to_convert_cm_in >= cm_inapplicable:
                inches = (to_convert_cm_in / 2.54)
                to_convert_cm_in = self.rounding(to_convert_cm_in)
                inches = self.rounding(inches)
                answer = "{} cm is {} in".format(to_convert_cm_in, inches)

            else:
                # Input is unsuitable due to being negative or 0
                answer = "Please enter a number greater than 0"
                cm_in_errors="yes"
            
            # Display conversion result
            if cm_in_errors == "no":
                self.cm_and_in_result_label.configure(text=answer, fg="blue")
                self.to_convert_cm_in_input.configure(bg="white")

            # Display error message
            else:
                self.cm_and_in_result_label.configure(text=answer, fg=error_message_background)
                self.to_convert_cm_in_input.configure(bg=input_box_error_background)
            
            # If there are no errors, add conversion to conversion history list
            if cm_in_errors !="yes":
                WelcomeScreen.conv_history_list.append(answer)
                self.conversion_history_button.config(state=NORMAL)
            
        # If the user doesn't enter a number, display error message
        except ValueError:
            self.cm_and_in_result_label.configure(text="Please enter a positive number", fg=error_message_background)
            self.to_convert_cm_in_input.configure(bg=input_box_error_background)
            
    def rounding(self, to_round):

        # If there is no remainder, print to 0dp
            if to_round %1 == 0:
                rounded = int(to_round)
        # Else, print to 2dp
            else:
                rounded = round(to_round, 2)
            return rounded
    
    def ConversionHistory(self, conv_history):
        get_ConversionHistory = ConversionHistory(self, conv_history)

    def Help(self):
        get_help = Help(self)

class MetresAndFeetConverter:
    def __init__(self, partner):
        
        # Formatting variables
        background = "orange"
        to_m_button_background = "yellow"
        to_ft_button_background = "#e9d3f2"

        # disable converter buttons in welcome screen when window is opened
        partner.m_and_ft_welcome_screen_button.config(state=DISABLED)
        partner.cm_and_in_welcome_screen_button.config(state=DISABLED)

        # Metres and Feet Converter child window
        self.m_and_ft_box = Toplevel()
        
        # If users press cross at top, closes window and re-enables Metres and Feet button
        self.m_and_ft_box.protocol('WM_DELETE_WINDOW', partial(self.close_MetresAndFeetConverter, partner))

        # GUI Frame
        self.m_and_ft_frame = Frame(self.m_and_ft_box, bg=background)
        self.m_and_ft_frame.grid()

        # Metres and Feet Converter heading (row 0)
        self.m_and_ft_heading = Label(self.m_and_ft_frame, text="Metres and Feet Converter",
                                 font="arial 18 bold", bg=background, padx=10, pady=10)
        self.m_and_ft_heading.grid(row=0)

        # User instructions (row 1)
        self.m_and_ft_instructions_label = Label(self.m_and_ft_frame, text="Type in a measurement below and push the button you wish to convert the measurement to.",
                                        font="Arial 10 italic", wrap=300,
                                         justify=CENTER, bg=background,
                                        padx=10, pady=10)
        self.m_and_ft_instructions_label.grid(row=1)

        # Measurement input box (row 2)
        self.to_convert_m_ft_input = Entry(self.m_and_ft_frame, width=20, font="Arial 20 bold")
        self.to_convert_m_ft_input.grid(row=2)

        # "To Convert" buttons frame
        self.to_m_and_ft_buttons_frame = Frame(self.m_and_ft_frame, bg=background)
        self.to_m_and_ft_buttons_frame.grid(row=3, pady=10)

        # To metres button (row 3)
        self.to_m_button = Button(self.to_m_and_ft_buttons_frame, text="To Metres", font="Arial 10 bold", bg=to_m_button_background, command=lambda: self.m_ft_convert(m_inapplicable=0, ft_inapplicable=0), padx=10, pady=10)
        self.to_m_button.grid(row=3, column=0, padx=5)

        # To ft button (row 3)
        self.to_ft_button = Button(self.to_m_and_ft_buttons_frame, text="To Feet", font="Arial 10 bold", bg=to_ft_button_background, command=lambda: self.m_ft_convert(m_inapplicable=0, ft_inapplicable=0.0000000000000001), padx=10, pady=10)
        self.to_ft_button.grid(row=3,column=1, padx=5)

        # Conversion Result subheading (row 4)
        self.m_and_ft_result_subheading_label = Label(self.m_and_ft_frame, font="Arial 14", bg=background, pady=10, text="Conversion Result:")
        self.m_and_ft_result_subheading_label.grid(row=4)

        # Conversion Result (row 5)
        self.m_and_ft_result_label = Label(self.m_and_ft_frame, font = "Arial 11 bold", bg=background, fg="blue", pady=10, text="")
        self.m_and_ft_result_label.grid(row=5)

        # Conversion History, Help and Dismiss buttons frame (row 6)
        self.m_and_ft_history_help_dismiss_buttons_frame = Frame(self.m_and_ft_frame, bg=background)
        self.m_and_ft_history_help_dismiss_buttons_frame.grid(row=6, pady=10)

        # Conversion History button (row 6)
        self.conversion_history_button = Button(self.m_and_ft_history_help_dismiss_buttons_frame, text="Conversion History", font="Arial 10 bold", command=lambda: self.ConversionHistory(WelcomeScreen.conv_history_list), padx=10, pady=10)
        self.conversion_history_button.grid(row=6,column=0, padx=5)

        # If list is empty, disable history button
        if len(WelcomeScreen.conv_history_list) == 0:
            self.conversion_history_button.config(state=DISABLED)

        # Help button (row 6)
        self.help_button = Button(self.m_and_ft_history_help_dismiss_buttons_frame, text="Help", font="Arial 10 bold", command=self.Help, padx=10, pady=10)
        self.help_button.grid(row=6,column=1, padx=5)

        # Dismiss button (row 6)
        self.m_and_ft_dismiss_button = Button(self.m_and_ft_history_help_dismiss_buttons_frame, text="Dismiss", font="Arial 10 bold", command=partial(self.close_MetresAndFeetConverter, partner), padx=10, pady=10)
        self.m_and_ft_dismiss_button.grid(row=6,column=2, padx=5)

    def close_MetresAndFeetConverter(self, partner):
        # Restore converter buttons in welcome screen 
        partner.m_and_ft_welcome_screen_button.config(state=NORMAL)
        partner.cm_and_in_welcome_screen_button.config(state=NORMAL)
        self.m_and_ft_box.destroy()
    
    def m_ft_convert(self, ft_inapplicable, m_inapplicable):
        
        # Format variables
        error_message_background = "red"
        input_box_error_background = "pink"

        # Get user input from input box
        to_convert_m_ft = self.to_convert_m_ft_input.get()

        try:
            to_convert_m_ft = float(to_convert_m_ft)
            m_ft_errors = "no"

            # Convert to metres if input is 0 or greater
            if ft_inapplicable == 0 and to_convert_m_ft >= ft_inapplicable:
                m = (to_convert_m_ft / 3.281)
                to_convert_m_ft = self.rounding(to_convert_m_ft)
                m = self.rounding(m)
                answer = "{} ft is {} m".format(to_convert_m_ft, m)

            # Convert to ft if input is 0 or greater
            elif m_inapplicable == 0 and to_convert_m_ft >= m_inapplicable:
                ft = (to_convert_m_ft * 3.281)
                to_convert_m_ft = self.rounding(to_convert_m_ft)
                ft = self.rounding(ft)
                answer = "{} m is {} ft".format(to_convert_m_ft, ft)

            else:
                # Input is unsuitable due to being negative or 0
                answer = "Please enter a number greater than 0"
                m_ft_errors="yes"
            
            # Display conversion result
            if m_ft_errors == "no":
                self.m_and_ft_result_label.configure(text=answer, fg="blue")
                self.to_convert_m_ft_input.configure(bg="white")

            # Display error message
            else:
                self.m_and_ft_result_label.configure(text=answer, fg=error_message_background)
                self.to_convert_m_ft_input.configure(bg=input_box_error_background)
            
            # If there are no errors, add conversion to conversion history list
            if m_ft_errors !="yes":
                WelcomeScreen.conv_history_list.append(answer)
                self.conversion_history_button.config(state=NORMAL)
            
        # If the user doesn't enter a number, display error message
        except ValueError:
            self.m_and_ft_result_label.configure(text="Please enter a positive number", fg=error_message_background)
            self.to_convert_m_ft_input.configure(bg=input_box_error_background)
            
    def rounding(self, to_round):

        # If there is no remainder, print to 0dp
            if to_round %1 == 0:
                rounded = int(to_round)
        # Else, print to 2dp
            else:
                rounded = round(to_round, 2)
            return rounded
    
    def Help(self):
        get_Help = Help(self)

    def ConversionHistory(self, conv_history):
        get_ConversionHistory = ConversionHistory(self, conv_history)

class Help:
    def __init__(self, partner):

        # Formatting variables
        help_background = "light blue"

        # Disable Help button while window is open
        partner.help_button.config(state=DISABLED)
         
        # Help GUI child window
        self.help_box = Toplevel()

        # If users press cross at top, closes window and re-enables Help button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_Help, partner))

        # GUI Frame
        self.help_frame = Frame(self.help_box, bg=help_background)
        self.help_frame.grid()

        # Help heading (row 0)
        self.help_heading = Label(self.help_frame, text="Help", font="arial 18 bold", bg=help_background)
        self.help_heading.grid(row=0)

        # Help text (row 1)
        self.help_text = Label(self.help_frame, text="Enter a number into the input box and then click on one of the two buttons underneath "
                                                     "to convert the measurement. \n\nEnsure the number you enter is a positive number, or an error will be "
                                                     "returned."
                                                     "\n\nE.g. If you wish to convert from inches to centimetres, type in a number and click "
                                                     "the 'To Centimetres' button. \n",
                                 justify=CENTER, width=60, bg=help_background, wrap=400)
        self.help_text.grid(row=1)

        # Dismiss button (row 2)
        self.help_dismiss_button = Button(self.help_frame, text="Dismiss", width=10, font="Arial 10 bold", command=partial(self.close_Help, partner), padx=10, pady=10)
        self.help_dismiss_button.grid(row=2, pady=10)



    def close_Help(self, partner):
        # Restore Help button in measurement converter if the measurement converter window is still open
        if partner.help_button.winfo_exists():
            partner.help_button.config(state=NORMAL)
        self.help_box.destroy()        

class ConversionHistory:
    def __init__(self, partner, conv_history):

        # Formatting variables
        ch_background = "#f060f7"
        conversion_history_string = "" 

        # Disable Conversion History button while window is open
        partner.conversion_history_button.config(state=DISABLED)

        # Conversion History GUI child window
        self.conversion_history_box = Toplevel()

        # If users press cross at top, closes window and re-enables Conversion History button
        self.conversion_history_box.protocol('WM_DELETE_WINDOW', partial(self.close_ConversionHistory, partner))

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
        if len(conv_history) >=5:
            for value in range(0,5):
                # Get length of list, print value and subtract 1 so that the next newest item will be printed in the next loop 
                conversion_history_string += conv_history[len(conv_history) - value - 1]+ "\n"

        # There are less than 5 values on the list so print what's on the list in order of most recent to least recent
        else:
            for value in conv_history:
                # Get length of list, print value and subtract 1 so that the next newest item will be printed in the next loop
                conversion_history_string += conv_history[len(conv_history) - conv_history.index(value) - 1] + "\n"


        # Conversion history (row 2)
        self.conversion_history_values_label = Label(self.conversion_history_frame, text=conversion_history_string,
                                                    font="Arial 12", bg=ch_background)
        self.conversion_history_values_label.grid(row=2)

        # Export button (row 3)
        self.export_button = Button(self.conversion_history_frame, text="Export", font="Arial 12 bold", command=lambda: self.Export(conv_history))
        self.export_button.grid(row=3, sticky=SW, padx=10, pady=10)

        # Dismiss button (row 3)
        self.dismiss_button = Button(self.conversion_history_frame, text="Dismiss", font="Arial 12 bold", command=partial(self.close_ConversionHistory, partner))
        self.dismiss_button.grid(row=3, sticky=SE, padx=10, pady=10)

    def close_ConversionHistory(self, partner):
        #  Restore Conversion History button in centimetres and inches converter if the window is still open
        if partner.conversion_history_button.winfo_exists():
            partner.conversion_history_button.config(state=NORMAL)
        self.conversion_history_box.destroy()

    def Export(self, conv_history):
        get_export = Export(self,conv_history)

class Export:
    def __init__(self, partner, conv_history):

        # Formatting variables
        export_background = "#f060f7"

        # disable export button
        partner.export_button.config(state=DISABLED)

        # Export child window
        self.export_box = Toplevel()

        # Re-enables export button if the export window is closed using the X button
        self.export_box.protocol('WM_DELETE_WINDOW', partial(self.close_export, partner))

        # GUI Frame
        self.export_frame = Frame(self.export_box, bg=export_background)
        self.export_frame.grid()

        # Heading (row 0)
        self.export_heading = Label(self.export_frame, text="Export Conversion History", font="Arial 18 bold", bg=export_background)
        self.export_heading.grid(row=0)

        # Export Instructions (row 1)
        self.export_instructions = Label(self.export_frame, text="Enter a filename below and push the Save button to export your conversion history onto a text file.",
                                                            font = "Arial 10 italic", wrap=300, bg=export_background)
        self.export_instructions.grid(row=1)

        # Warning text (row 2)
        self.export_warning_text = Label(self.export_frame, text = "Please note that if the filename you enter below already exists, "
                                                                   "it will be replaced with your conversion history.", justify=CENTER,
                                                                   bg="pink",fg="maroon", font = "Arial 10 italic bold", wrap=300,
                                                                   padx=10, pady=10)
        self.export_warning_text.grid(row=2, padx=10, pady=10)

        # Input box (row 3)
        self.filename_input_box = Entry(self.export_frame, width=31, font="arial 12 bold")
        self.filename_input_box.grid(row=3, pady=10)

        # Error messages (row 4)
        self.save_error_label = Label(self.export_frame, text="", fg="red", bg=export_background)
        self.save_error_label.grid(row=4)

        # Save button (row 5)
        self.save_button = Button(self.export_frame, text="Save", font="Arial 13 bold", command=partial(lambda: self.save_conversion_history(partner, conv_history)))
        self.save_button.grid(row=5, sticky=SW, padx=10, pady=10)

        # Cancel button (row 5)
        self.cancel_button = Button(self.export_frame, text="Cancel", font="Arial 13 bold", command=partial(self.close_export,partner))
        self.cancel_button.grid(row=5, sticky=SE, padx=10, pady=10)

    def save_conversion_history(self, partner, conv_history):
        # Variables that set valid characters and if an error has been made 
        valid_characters = "[A-Za-z0-9_]"
        has_error = "no"

        filename = self.filename_input_box.get()
        print(filename)

        if filename == "":
            issue = "filename cannot be blank"
            has_error = "yes"

        # Checks filename for spaces or unsuitable symbols
        for character in filename:
            if re.match(valid_characters, character):
                continue

            elif character == " ":
                issue = "no spaces allowed"

            else:
                issue = ("no {}'s allowed".format(character))
            has_error = "yes"
            break

        if has_error == "yes":
            # Print error message that states which character is unsuitable
            self.save_error_label.config(text="Unsuitable filename - {}".format(issue))
            # Change input box background to pink
            self.filename_input_box.config(bg="pink")

        else:
            # Add .txt suffix
            filename = filename + ".txt"

            # Generate text file to contain conversion history
            file = open(filename, "w+")

            # Write conversions
            for value in conv_history:
                file.write(value + "\n")

            # Close file
            file.close()

            # Close export window
            self.close_export(partner)

    def close_export(self, partner):
        # Re-enable export button in Conversion History if the Conversion History window is still open
        if partner.export_button.winfo_exists():     
            partner.export_button.config(state=NORMAL)
        self.export_box.destroy() 


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Measurement Converter Tool")
    something = WelcomeScreen(root)
    root.mainloop()                                 