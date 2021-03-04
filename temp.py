import unittest
import c4main

class TestWinConditions(unittest.TestCase):
	#rows = [[0 for col in range(7)] for row in range(6)]

	def create_test_board_0(self):
		board = c4main.Board()
		board.place(3, 1).place(4,2).place(5,2).place(6,2).place(7,1).place(3,1).place(4,1).place(5,2).place(6,2).place(3,2).place(4,2).place(5,1).place(3,1).place(4,1).place(3,2)
		return board

	def create_test_board_1(self):
		board = c4main.Board()
		board.place(1,1).place(2,1).place(3,1).place(4,2).place(5,2).place(6,2).place(2,1).place(3,1).place(4,1).place(5,2).place(6,2).place(2,2).place(3,2).place(4,1).place(5,1).place(6,1).place(2,2).place(3,2).place(4,1).place(2,2).place(3,1).place(4,2)
		return board

	def create_test_board_2(self):
		board = c4main.Board()
		board.place(1,1).place(2,1).place(3,1).place(4,2).place(5,2).place(6,2).place(2,1).place(3,1).place(4,2).place(5,2).place(2,2).place(3,2).place(4,1).place(5,1).place(6,1).place(2,2).place(3,2).place(2,2).place(3,1)
		return board

	def create_test_game_0(self):
		player = c4main.Player("AI")
		game = c4main.Game(player, None)
		board = game.board
		board.place(2,1).place(3,1).place(4,1).place(5,2).place(5,2).place(5,2)
		return game

	def create_test_game_1(self):
		player = c4main.Player("AI")
		game = c4main.Game(player, None)
		board = game.board
		board.place(2,1).place(3,1).place(5,2).place(5,2)
		return game





	def test_ai_play_game_0(self):
		game = c4main.Game(c4main.Player("AI"), c4main.Player("AI"))
		game.start()

		self.assertTrue(True)	

if __name__ == '__main__':
	unittest.main()