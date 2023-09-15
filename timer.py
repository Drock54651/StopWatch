import customtkinter as ctk
from settings import *


class App(ctk.CTk):
	def __init__(self):
		super().__init__(fg_color = BLACK)
		self.title('')
		self.geometry('300x600')
		self.iconbitmap('empty.ico')
		self.resizable(False,False)


		#* LAYOUT
		self.rowconfigure(0, weight = 5, uniform = 'a')
		self.rowconfigure(1, weight = 1, uniform = 'a')
		self.rowconfigure(2, weight = 4, uniform = 'a')
		self.columnconfigure(0, weight = 1, uniform = 'a')
		#* FONTS
		self.button_fonts = ctk.CTkFont(family = FONT, size  = BUTTON_FONT_SIZE)

		#* DATA

		#* WIDGETS
		self.control_buttons = ControlButtons(self)


		#* RUN
		self.mainloop()




class ControlButtons(ctk.CTkFrame): #! frame for all the buttons
	def __init__(self, parent):
		super().__init__(parent, corner_radius = 0, fg_color = 'transparent')
		self.grid(row = 1, column = 0, sticky = 'news')


if __name__ == '__main__':
	App()
		