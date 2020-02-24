from tkinter import *
import random
import time


class Ball:
	def __init__(self, canvas, paddle, color):
		self.canvas = canvas
		self.paddle = paddle
		self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
		self.canvas.move(self.id, 245, 100)
		starts = [-3, -2, -1, 1, 2, 3]
		random.shuffle(starts)
		self.x = starts[0]
		self.y = -3
		self.canvas_height = self.canvas.winfo_height()
		self.canvas_width = self.canvas.winfo_width()
		self.hit_bottom = False
		self.score = 0
	
	def myscores(self):
		return self.score

	def hit_paddle(self, pos):
		paddle_pos = self.canvas.coords(self.paddle.id)
		if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
			if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
				return True
		return False
	def draw(self):
		global score
		self.canvas.move(self.id, self.x, self.y)
		pos = self.canvas.coords(self.id)
		if pos[1] <= 0:
			self.y = 3
		if pos[3] >= self.canvas_height:
			self.hit_bottom = True
		if self.hit_paddle(pos) == True:		
			self.y = -3
			#sss = 0
			self.score += 1
			#canvas.delete(sss)
			#sss = canvas.create_text(100,10,fill="red",font="Times 20", text="Score %s" % score)
		if pos[0] <= 0:
			self.x = 3
		if pos[2] >= self.canvas_width:
			self.x = -3
class Paddle:
	def __init__(self, canvas, color):
		self.canvas = canvas
		self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
		self.canvas.move(self.id, 200, 300)
		self.x = 0
		self.canvas_width = self.canvas.winfo_width()
		self.canvas.bind_all("<KeyPress-Left>", self.turn_left)
		self.canvas.bind_all("<KeyPress-Right>", self.turn_right)
	def draw(self):
		self.canvas.move(self.id, self.x, 0)
		pos = self.canvas.coords(self.id)
		if pos[0] <= 0:
			self.x = 0
		elif pos[2] >= self.canvas_width:
			self.x = 0
	def turn_left(self, evt):
			self.x = -2
	def turn_right(self, evt):
			self.x = 2


def main():
	def rest():
		tk.destroy()
		try:
			main()
		except:
			pass
	tk = Tk()
	tk.title("Bounce game OrangoMangoGames Paul Kocian")
	tk.resizable(0, 0)
	tk.wm_attributes("-topmost", 1)
	canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
	iptext = canvas.create_text(100,10,fill="red",font="Times 20")
	b = Button(tk, text="Exit", command=tk.destroy)
	b.grid()
	b2 = Button(tk, text="Restart", command=rest)
	b2.grid(row=0,column=1)
	def update_ip():
		#try:
		canvas.itemconfigure(iptext, text="Score: %s" % ball.myscores())
		    #tk.after(1000, update_ip)
		#except StopIteration:
		#    pass

	canvas.grid(columnspan=2)
	tk.update()

	paddle = Paddle(canvas, "blue")
	ball = Ball(canvas, paddle, "red")
	while 1:
		if ball.hit_bottom == False:
			ball.draw()
			paddle.draw()
		    
		tk.update_idletasks()
		tk.update()
		#print(ball.myscores())
		update_ip()
		time.sleep(0.01)

try:
	main()
except:
	pass
