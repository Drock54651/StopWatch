import customtkinter as ctk
from settings import *


class App(ctk.CTk): #! window and also methods for button functionality logic
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
		self.control_buttons = ControlButtons(
			self, 
			self.button_fonts,
			start = self.start,
			pause = self.pause,
			resume = self.resume,
			reset = self.reset,
			create_lap = self.create_lap)

		#* RUN
		self.mainloop()


	def start(self):
		print('start')

	def pause(self):
		print('pause')

	def resume(self):
		print('resume')

	def reset(self):
		print('reset')

	def create_lap(self):
		print('lap')


class ControlButtons(ctk.CTkFrame): #! frame for all the buttons
	def __init__(self, parent, button_font, start, pause, resume, reset, create_lap):
		super().__init__(parent, corner_radius = 0, fg_color = 'transparent')
		self.grid(row = 1, column = 0, sticky = 'news')

		#* INTERACTION METHODS
		self.start = start
		self.pause = pause
		self.resume = resume
		self.reset = reset
		self.create_lap = create_lap
		self.state = 'OFF'
		

		#* GRID LAYOUT
		self.rowconfigure(0, weight = 1, uniform = 'b')
		self.columnconfigure(0, weight = 1, uniform = 'b') #! weights 1 for padding
		self.columnconfigure(1, weight = 9, uniform = 'b')
		self.columnconfigure(2, weight = 1, uniform = 'b')
		self.columnconfigure(3, weight = 9, uniform = 'b')
		self.columnconfigure(4, weight = 1, uniform = 'b')


		#* BUTTONS
		self.lap_button = ctk.CTkButton( #! lap button
			self, 
			text = 'lap',
			command = self.lap_handler,
			state = 'disabled',
			fg_color = GREY,
			font = button_font)
		
		self.lap_button.grid(row = 0, column = 1, columnspan = 1, sticky = 'news')

		self.start_button = ctk.CTkButton( #! start button
			self, 
			text = 'Start',
			command = self.start_handler,
			fg_color = GREEN,
			hover_color = GREEN_HIGHLIGHT,
			text_color = GREEN_TEXT,
			font = button_font)
		
		self.start_button.grid(row = 0, column = 3, columnspan = 1, sticky = 'news')

	def start_handler(self): #! handles the start, pause, and resume methods for start button
		if self.state == 'OFF':
			self.start()
			self.state = 'ON'

		elif self.state == 'ON':
			self.pause()
			self.state = 'PAUSE'

		elif self.state == 'PAUSE':
			self.resume()
			self.state = 'ON'

		self.update_buttons()	


	def lap_handler(self): #! handles create_lap and reset method for lap button
		if self.state == 'ON':
			self.create_lap()

		else:
			self.reset()
			self.state = 'OFF'

		self.update_buttons()			
	
	def update_buttons(self): #! button state changes in the lap and start handlers, therefore functionality of buttons changes
		if self.state == 'ON':
			self.start_button.configure(text = 'Stop', fg_color = RED, hover_color = RED_HIGHLIGHT, text_color = RED_TEXT)
			self.lap_button.configure(state = 'normal',  text = 'Lap', fg_color = ORANGE_DARK, text_color = ORANGE_DARK_TEXT, hover_color = ORANGE_HIGHLIGHT)
			
		elif self.state == 'OFF':
			self.start_button.configure(text = 'Start')
			self.lap_button.configure(state = 'disabled', text = 'Lap', fg_color = GREY)

		elif self.state == 'PAUSE':
			self.start_button.configure(text = 'Start', fg_color = GREEN, hover_color = GREEN_HIGHLIGHT, text_color = GREEN_TEXT)
			self.lap_button.configure(text = 'Reset')


if __name__ == '__main__':
	App()
		