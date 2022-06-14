# main program for window breakfast App
import tkinter as tk
from window import Window

# What I think I need for this APP

# windowhandler
# fileHandler
# colorHandler
# breakfast-item
	# input-, edit-, insert-, remove-handler
# dbHandler
# passwordHandler
# keypressHandler




size = '1280x720'
width = 1280
height = 720
title = 'BreakfastLogger'

breakfastList = ['01-06-2022 Havregrøt', '02-06-2022 Havregrøt']



# initialize window
windowObj = Window(tk, width, height, title, breakfastList)

if __name__ == '__main__':
	print(windowObj)
	windowObj.start()

