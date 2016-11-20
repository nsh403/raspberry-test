#!/usr/bin/env python

"""

"""

import Tkinter as tk
import math
import cmath



class Graph:
	def __init__(self, canvas, x_min, x_max, y_min, y_max, x_scale, y_scale):
		self.canvas = canvas
		self.w = float(canvas.config('width')[4])
		self.h = float(canvas.config('height')[4])
		self.x_min =  x_min
		self.x_max =  x_max
		self.x_scale =  x_scale
		self.y_min =  y_min
		self.y_max =  y_max
		self.y_scale =  y_scale
		self.px_x = (self.w -100)/ ((x_max - x_min) / x_scale)
		self.px_y = (self.h -100)/ ((y_max - y_min) / y_scale)

	def drawAxes(self):
		rect = 50, 50, self.w-50, self.h-50
		
		self.canvas.create_rectangle(rect, outline="black")
		
		for x in range (0, self.x_max - self.x_min + 1, self.x_scale):
			x_step = (self.px_x * x)/self.x_scale
			coord = 50+x_step, self.h-50, 50+x_step, self.h-45
			self.canvas.create_line(coord, fill="black")
			coord = 50+x_step, self.h-40	 			
			self.canvas.create_text(coord, fill="black", text=str(self.x_min + x))

		for y in range (0, self.y_max - self.y_min + 1, self.y_scale):  
			y_step = (self.px_y * y)/self.y_scale
			coord = 45, 50+y_step, 50, 50+y_step
			self.canvas.create_line(coord, fill="black")
			coord = 35, 50+y_step			
			self.canvas.create_text(coord, fill="black", text=str(self.y_max - y))

	def plotPoint(self, x, y):
		xp = (self.px_x * (x - self.x_min)) / self.x_scale
		yp = (self.px_y * (self.y_max - y)) / self.y_scale
		coord = 50+xp, 50+yp
		#self.canvas.create_text(coord, fill="white", text="x")
		return coord
		
	def plotLine(self, points):
		last_point = ()
		for point in points:
			this_point = self.plotPoint(point[0],point[1])
			
			if last_point: 		
				self.canvas.create_line(last_point+this_point, fill="black")
			last_point = this_point	
			#print last_point

def compute_dft(input):
	n = len(input)
	output = [complex(0)] * n
	for k in range(n):  # For each output element
		s = complex(0)
		for t in range(n):  # For each input element
			s += input[t] * cmath.exp(-2j * cmath.pi * t * k / n)
		output[k] = s
	return output





def frange(x, y, jump):
	while x < y:
		yield x
		x += jump


if __name__ == "__main__":
	top = tk.Frame()
	top.pack()

	Tc = tk.Canvas(top, bg="yellow", height=300, width=700)
	#Fc = tk.Canvas(top, bg="yellow", height=300, width=700)
	
	Tg = Graph(Tc, 0, 10, -2, 2, 1, 1)
	Tg.drawAxes()
	
	#Fg = Graph(Fc, 0, 20, 0, 1, 1, 1)
	#Fg.drawAxes()


	# generate test data	
	phase = 0.1
	
	for i in range(10):
		t=[]
		plot_t=[]
		#Tg.canvas.delete('all')
		
		# get new data
		for x in frange(0, 10, 0.01):
			y = math.sin(2 * cmath.pi * x + phase*i) + (1.0/3.0)*math.sin(6 * cmath.pi * x) 
			#+ (1.0/5.0)*math.sin(10 * cmath.pi * x) 
			#+ (1.0/7.0)*math.sin(14 * cmath.pi * x)
			t.append(y)
			plot_t.append((x,y))
			
		# plot
		Tg.plotLine(plot_t)
		Tc.pack()

	top.mainloop()


