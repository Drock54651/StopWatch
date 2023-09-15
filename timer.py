import customtkinter as ctk


class App(ctk.CTk):
	def __init__(self):
		super().__init__(fg_color = 'black')
		self.title('')
		self.geometry('300x600')
		self.iconbitmap('empty.ico')

		#* RUN
		self.mainloop()
        
App()
		