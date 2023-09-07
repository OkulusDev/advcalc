#!/usr/bin/python3
# -*- coding: utf-8 -*-
from math import sin, cos, pi, factorial, sqrt
from hashlib import sha256, md5
from tkinter import *
from tkinter import messagebox
import sys

buttons: list = [
				"7", "8", "9", "+", "*", 
				"4", "5", "6", "-", "/",
				"1", "2", "3",  "=", "xⁿ",
				"0", ".", "±",  "C",
				"Exit", "π", "sin", "cos",
				"(", ")","n!","√2",
]



class App:
	def __init__(self, title: str):
		self.root = Tk()
		self.root.title(title)
		self.root.geometry('500x400')
		self.root.resizable(False, False)
		self.root.bg = '#111111'

		self.create_buttons()
		self.create_entry()

	def create_buttons(self):
		row = 1
		column = 0
		self.memory = None

		for i in buttons:
			rel = ""
			button_func = lambda x=i: self.calc(x)
			
			if i.isdigit():
				Button(self.root, text=i, font='monospace 16', command=button_func, width=10, height=4, relief='flat', bg='#111111', fg='#f8f8f8').grid(row=row, column = column)
			else:
				Button(self.root, text=i, font='monospace 16', command=button_func, width=10, height=4, relief='flat', bg='#ffa500', fg='black').grid(row=row, column = column)

			column += 1

			if column > 4:
				column = 0
				row += 1

	def create_entry(self):
		self.calc_entry = Entry(self.root, width=60, font='Monospace 18')
		self.calc_entry.grid(row=0, column=0, columnspan=5)

	def calc(self, key):
		if key == '=':
			allowed_symbols = "-+0123456789.*/)(" 
			
			if self.calc_entry.get()[0] not in allowed_symbols:
				calc_entry.insert(END, "")
				messagebox.showerror("Ошибка! Вы ввели не число")
			try:
				result = eval(self.calc_entry.get())
				self.calc_entry.insert(END, "=" + str(result))
			except:
				self.calc_entry.insert(END, "Ошибка")
				messagebox.showerror("Ошибка", "Провьте данные")
		elif key == "C":
			self.calc_entry.delete(0, END)
		elif key == "±":
			if "=" in self.calc_entry.get():
				self.calc_entry.delete(0, END)
			
			try:
				if self.calc_entry.get()[0] == "-":
					self.calc_entry.delete(0)
				else:
					self.calc_entry.insert(0, "-")
			except IndexError:
				pass
		elif key == "π":
			self.calc_entry.insert(END, pi)
		elif key == "Exit":
			self.root.after(1, self.root.destroy)
			sys.exit
		elif key == "xⁿ":
			self.calc_entry.insert(END, "**")
		elif key == "sin":
			self.calc_entry.insert(END, "=" + str(math.sin(int(self.calc_entry.get()))))
		elif key == "cos":
			self.calc_entry.insert(END, "=" + str(math.cos(int(self.calc_entry.get()))))
		elif key == "(":
			self.calc_entry.insert(END, "(")
		elif key == ")":
			self.calc_entry.insert(END, ")")
		elif key == "n!":
			self.calc_entry.insert(END, "=" + str(factorial(int(self.calc_entry.get()))))
		elif key == "√2":
			self.calc_entry.insert(END, "=" + str(sqrt(int(self.calc_entry.get()))))
		else:
			if "=" in self.calc_entry.get():
				self.calc_entry.delete(0, END)
			
			self.calc_entry.insert(END, key)


	def run(self):
		self.root.mainloop()


def main():
	app = App('AdvCalc by Okulus')
	app.run()


if __name__ == '__main__':
	main()
