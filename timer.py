import customtkinter as ctk
from settings import *
from time import time
import tkinter as tk
from math import sin, cos, radians

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
		self.clock = Clock(self)

		#* TIMER LOGIC
		self.timer = Timer()
		self.active = False

		#* RUN
		self.mainloop()


	def animate(self):
		if self.active:
			self.clock.draw(self.timer.get_time())
			self.after(FRAMERATE, self.animate)

	def start(self):
		self.timer.start()
		self.active = True
		self.animate()

	def pause(self):
		self.timer.pause()
		self.active = False

	def resume(self):
		self.timer.resume()

	def reset(self):
		self.timer.reset()

	def create_lap(self):
		print(self.timer.get_time())


class Clock(tk.Canvas): #! drawing the clock itself
	def __init__(self, parent):
		super().__init__(parent, background = 'Black', bd = 0, highlightthickness = 0, relief = 'ridge')
		self.grid(row = 0, column = 0, sticky = 'news', padx = 5, pady = 5)
		self.bind('<Configure>', self.setup)
		

	def setup(self, event): #! gets canvas width and height, radii, in which can be used for drawing other stuff
		self.center = (event.width / 2, event.height / 2) 
		self.size = (event.width, event.height)

		#* RADIUS
		self.outer_radius = (event.width / 2) * .95 #! smaller the number the smaller the radius, i.e closer to center 
		self.middle_radius = (event.width / 2) * .9
		self.inner_radius = (event.width / 2) * .85
		
		self.number_radius = (event.width / 2) * .7
		self.start_radius = (event.width / 2) * .2

		#* DRAW CLOCK
		self.draw()

	def draw(self, milliseconds = 0): #! contains all the parts of the clock to draw

		seconds = milliseconds / 1000
		angle = (seconds % 60) * 6 #! grabs only the seconds, multiply by 6, as 1 second is every 6 degrees -> (360 / 60)
		
		self.delete('all')

		self.draw_clock()
		self.draw_hand(angle)
		self.draw_center()

	def draw_center(self): #! Draw the circle center of the clock
		self.create_oval(
				self.center[0] - CENTER_SIZE, #! left
				self.center[1] - CENTER_SIZE, #! Top
				self.center[0] + CENTER_SIZE, #! Right
				self.center[1] + CENTER_SIZE, #! Bottom
				fill = BLACK,
				width = LINE_WIDTH,
				outline = ORANGE)

	def draw_clock(self): #! clock lines
		for angle in range(360):
			sin_a = sin(radians(angle - 90))
			cos_a = cos(radians(angle - 90))

			x_outer = self.center[0] + (cos_a * self.outer_radius) #! x distance from center
			y_outer = self.center[1] + (sin_a * self.outer_radius) #! y distance from center

			# self.create_oval(x_outer - 2, y_outer - 2, x_outer + 2, y_outer + 2, fill = 'orange') #! to visualize outer circle
			if angle % 30 == 0: 
				#* DRAW LINES
				x_inner = self.center[0] + (cos_a * self.inner_radius) 
				y_inner = self.center[1] + (sin_a * self.inner_radius) 
				self.create_line((x_inner, y_inner), (x_outer, y_outer), fill = WHITE, width = LINE_WIDTH) #! draw line from inner circle to outer for the ticks

				#* DRAWING NUMBERS
				x_number = self.center[0] + (cos_a * self.number_radius)
				y_number = self.center[1] + (sin_a * self.number_radius)

				self.create_text((x_number, y_number), text = f'{int(angle / 6)}', font = f'{FONT}{CLOCK_FONT_SIZE}', fill = WHITE) 


			elif angle % 6 == 0: 
				x_middle = self.center[0] + (cos_a * self.middle_radius)
				y_middle = self.center[1] + (sin_a * self.middle_radius)

				self.create_line((x_middle, y_middle), (x_outer, y_outer), fill = GREY, width = LINE_WIDTH)

	def draw_hand(self, angle = 0): #! clock hand
		sin_a = sin(radians(angle - 90))
		cos_a = cos(radians(angle - 90))

		x_start = self.center[0] - (cos_a * self.start_radius)
		y_start = self.center[1] - (sin_a * self.start_radius)

		x_end = self.center[0] + (cos_a * self.outer_radius)
		y_end = self.center[1] + (sin_a * self.outer_radius)

		self.create_line((x_start, y_start), (x_end, y_end), fill = ORANGE, width = LINE_WIDTH)

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

class Timer: #! Timer Logic
	def __init__(self):
		self.start_time = None
		self.pause_time = None
		self.is_paused = False

	def start(self):
		self.start_time = time() #! time in seconds since 1970, this is fixed when start is pressed
		print('start')

	def pause(self):
		self.pause_time = time()
		self.is_paused = True
		print('pause')

	def resume(self):
		elapsed_time = time() - self.pause_time
		self.start_time += elapsed_time
		self.is_paused = False

	def reset(self):
		self.pause_time = 0
		self.is_paused = False
 
	def get_time(self):
		if self.is_paused:
			return int(round(self.pause_time - self.start_time, 2) * 1000)
		
		else:
			return int(round(time() - self.start_time, 2) * 1000) #! ms cause easier to work with







if __name__ == '__main__':
	App()
		