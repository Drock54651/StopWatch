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

		#* GRID LAYOUT
		self.rowconfigure(0, weight = 1, uniform = 'b')
		self.columnconfigure(0, weight = 1, uniform = 'b') #! weights 1 for padding
		self.columnconfigure(1, weight = 9, uniform = 'b')
		self.columnconfigure(2, weight = 1, uniform = 'b')
		self.columnconfigure(3, weight = 9, uniform = 'b')
		self.columnconfigure(4, weight = 1, uniform = 'b')


		#* BUTTONS
		self.lap_button = ctk.CTkButton(
			self, 
			text = 'lap',
			command = lambda: print('lap'),
			state = 'disabled',
			fg_color = GREY
			)
		
		self.lap_button.grid(row = 0, column = 1, columnspan = 1)

		self.reset_button = ctk.CTkButton(self, text = 'test1')
		self.reset_button.grid(row = 0, column = 3, columnspan = 1)

if __name__ == '__main__':
	App()
		