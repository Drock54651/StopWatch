import customtkinter as ctk
from settings import *


class App(ctk.CTk):
	def __init__(self):
		super().__init__(fg_color = BLACK)
		self.title('')
		self.geometry('300x600')
		self.iconbitmap('empty.ico')
		self.resizable(False,False)
		#* RUN
		self.mainloop()


if __name__ == '__main__':
	App()
		