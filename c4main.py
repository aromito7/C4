import numpy
import random
from graphics import *

class Player:
	player_types = ["AI", "ML", "PL"]
	player_type = None
	def __init__(self, player_type):
		self.player_type = player_type

	def decide(self, board, player_number):
		if self.player_type == "AI":
			return self.ai_decide(board, player_number)
		
	def ai_decide(self, board, player_number):
		max_chains = [-1,0,0,0,0,0,0,0,-1]
		opp_chains = [-1,0,0,0,0,0,0,0,-1]
		for a in range(1,8):
			max_chains[a] = board.check_all_chains_with_expansion([a, board.available[a]], player_number)
			opp_chains[a] = board.check_all_chains_with_expansion([a, board.available[a]], 3-player_number)
		
		#print(max_chains)
		#print(opp_chains)

		for a in range(1,8):			#First priority is winning immediately
			if max_chains[a] > 3: return a
		for a in range(1,8):				#Second priority is preventing opponent from winning
			if opp_chains[a] > 3: return a
		
		possible_moves = []
		for a in range(len(board.available)):		#Third priority is creating the longest chain possible
			if max_chains[a] == max(max_chains):
				possible_moves.append(a)
		return random.choice(possible_moves)



class Board:
	def __init__(self):
		self.available = [7,1,1,1,1,1,1,1,7]
		self.previous = [None, None]
		self.victory = 0

		rows = [[0 for y in range(8)] for x in range(9)]
		for x in range(9):
			for y in range(8):
				if x%8 == 0 or y%7 == 0: 
					rows[x][y] = -1


		self.rows = rows

	def create(self):
		win = GraphWin('Connect 4', 350, 300)
		self.win = win
		rows = self.rows

		background = Rectangle(Point(0, 0), Point(350, 300))
		background.setFill('yellow')
		background.draw(win)
		colors = ['white', 'red', 'black']
		for x in range(1, 8): 
			for y in range(1, 7):
				circle = Circle(Point(-25 + x*50, 325 - y*50), 20)
				circle.setFill(colors[rows[x][y]])
				circle.draw(win)
		win.getMouse()

	def update(self, move):
		if not hasattr(self, 'win'):
			self.create()
			return

		rows = self.rows
		win = self.win

		x = move
		y = self.available[move]-1
		colors = ['white', 'red', 'black']

		circle = Circle(Point(-25 + x*50, 325 - y*50), 20)
		circle.setFill(colors[rows[x][y]])
		circle.draw(win)

		win.getMouse()

	def __str__(self):
		self.update(self.previous[0])

		self.win.close()
		return("Board being displayed")

	def place(self, x, player):
		if self.available[x] > 6:
			print("Too high to place.")
			return
		self.previous = [x, self.available[x]]
		self.rows[x][self.available[x]] = player
		self.available[x]+=1


		if self.is_victory():
			self.victory = player

		return self

	def is_victory(self):
		rows = self.rows

		if self.is_horizontal_victory() or self.is_vertical_victory() or self.is_diagonal_downward_victory() or self.is_diagonal_upward_victory():
			return True

		return False

	def check_all_chains_with_expansion(self, start, player):
		hori = self.check_maximum_chains(start, 1, 0, player)
		vert = self.check_maximum_chains(start, 0, 1, player)
		diup = self.check_maximum_chains(start, 1, 1, player)
		dido = self.check_maximum_chains(start, 1,-1, player)

		chains = [hori, vert, diup, dido]

		for chain in chains:
			if chain[0] + chain[1] < 4:
				chain[0] = 0

		max_chain = max(hori[0], vert[0], diup[0], dido[0])

		return max_chain

	def check_all_chains(self, start, player):
		hori = self.check_maximum_chains(start, 1, 0, player)
		vert = self.check_maximum_chains(start, 0, 1, player)
		diup = self.check_maximum_chains(start, 1, 1, player)
		dido = self.check_maximum_chains(start, 1,-1, player)

		max_chain = max(hori[0], vert[0], diup[0], dido[0])

		return max_chain

	def check_maximum_chains(self, start, dx, dy, player):
		count = 1
		expand = 0
		x = start[0]
		y =  start[1]

		if y > 6: return [0,0]


		temp = 1
		while self.rows[x-temp*dx][y-temp*dy] == player:
			temp+=1
			count+=1

		
		while self.rows[x-temp*dx][y-temp*dy] == 0:
			temp+=1
			expand+=1

		temp = 1
		while self.rows[x+temp*dx][y+temp*dy] == player:
			count+=1
			temp+=1
		
		while self.rows[x+temp*dx][y+temp*dy] == 0:
			temp+=1
			expand+=1

		return [count, expand]

	def is_horizontal_victory(self):
		count = self.check_maximum_chains(self.previous, 1, 0, self.rows[self.previous[0]][self.previous[1]])[0]
		if count > 3:
			return True
		return False

	def is_vertical_victory(self):
		count = self.check_maximum_chains(self.previous, 0, 1, self.rows[self.previous[0]][self.previous[1]])[0]
		if count > 3:
			return True
		return False

	def is_diagonal_downward_victory(self):
		count = self.check_maximum_chains(self.previous, -1, 1, self.rows[self.previous[0]][self.previous[1]])[0]
		if count > 3:
			return True
		return False

	def is_diagonal_upward_victory(self):
		count = self.check_maximum_chains(self.previous, 1, 1, self.rows[self.previous[0]][self.previous[1]])[0]
		if count > 3:
			return True
		return False

class Game:
	players = [None, None]
	def __init__(self, p0, p1):
		self.players = [p0, p1]
		self.board = Board()
		self.game_over = False
		self.current_player = 1
		self.turns = 0

	def start(self):
		while self.board.victory == 0:
			move = self.players[self.current_player-1].decide(self.board, self.current_player)
			self.board.place(move, self.current_player)
			self.board.update(move)
			self.current_player = 3 - self.current_player
			self.turns += 1
			print(self.turns)
		print("Player: " + str(self.board.victory) + " wins!")
		self.board.win.getMouse()



def main():
	p1 = Player()
	p2 = Player()

	Game(p1,p2)

if __name__ == '__main__':
	main()