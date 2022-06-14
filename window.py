# window class
# frame_one = tk.Frame(root, )
# frame_one.pack()
# frame_two = tk.Frame()
# frame_two.pack()
# frame_three = tk.Frame(root, width = 50, height = 200, bg = 'blue')
# frame_three.pack()
class Window:
	def __init__(self, tk, width, height, title, breakfastList):
		# basics
		self.tk = tk
		self.root = self.tk.Tk()
		self.root.geometry(str(width)+'x'+str(height))
		self.width = width
		self.height = height
		self.breakfastList = breakfastList


		#frames 
		self.frL = tk.Frame(self.root, width = width/3, height = height, bg = 'red')
		self.frL.grid(row = 0, column = 0)

		self.frC = self.tk.Frame(self.root, width = width/3, height = height, bg = 'black')
		self.frC.grid(row = 0, column = 1)

		self.frR = tk.Frame(self.root, width = width/3, height = height, bg = 'blue')
		self.frR.grid(row = 0, column = 2)
		
		#extras
		self.message = 'Nail to the polish'
		self.root.title(title)

	def __str__(self):
		return self.message


	def dosomething(self):
		self.mylabel.config(bg = 'hotpink')
		self.mybutton.config(text = 'Click Me', bg = 'cyan')

		self.frL.config(height = self.height/2, bg = 'pink')

		print(self.mylabel.config()['text'])
		
		# self.leftLabel.config(bg = 'cyan', width = 10)
		# self.rightLabel.config(bg = 'cyan', width = 25)
		# print(self.frL.winfo_width())
		# print(self.frR.winfo_width())
		textFieldContent = self.text.get(1.0, "end-1c")
		print(textFieldContent)




	def start(self):
		


		# TOP LABEL
		self.mylabel = self.tk.Label(self.frC, text = "BreakfastLogger", bg = "red", fg = 'white')
		self.mylabel.grid(row = 0, column = 0, padx = 20, pady = 20)
	
		# TOP BUTTON
		self.mybutton = self.tk.Button(self.frC, text = "Click Me", command = self.dosomething, bg = 'orange')
		self.mybutton.grid(row = 0, column = 1, padx = 20, pady = 20)

		# EXTRA BUTTONS
		self.myEXbutton = self.tk.Button(self.frC, text='Quit', command=self.root.destroy)
		self.myEXbutton.grid(row = 0, column = 2)

		self.myEXbutton2 = self.tk.Button(self.frC, text="Broadcast Message", command=self.sayMessage)
		self.myEXbutton2.grid(row = 0, column = 4)

		self.clearButton = self.tk.Button(self.frC, text = 'Clear Text', command = self.clearText)
		self.clearButton.grid(row = 1, column = 4)

		# inputFields and Submits
		self.inputLabel = self.tk.Label(self.frC, text="Input")
		self.inputLabel.grid(row = 1, column = 0)

		self.inputField = self.tk.Entry(self.frC, width=20)
		self.inputField.grid(row = 1, column = 1)
		
		self.submitButton = self.tk.Button(self.frC, text='Submit', command = self.saveInput)
		self.submitButton.grid(row = 1, column = 2)

		# textfield
		self.text = self.tk.Text(self.frL, height = 20, width = 25)
		self.text.grid(row = 0, column = 0, padx = 120, pady = 20)

		self.printBreakfastButton = self.tk.Button(self.frC, text = 'Show', command = self.printBreakfasts)
		self.printBreakfastButton.grid(row = 0, column = 3, padx = 5, pady = 5) 

		# main loop
		self.root.mainloop()

	def printBreakfasts(self):
		for item in self.breakfastList:
			print(item)


	def sayMessage(self):
		print(self.message)

	def saveInput(self):
		# this gets content in inputField and calls deleteAllInput
		inputValue = self.inputField.get()
		# add input to breakfastList
		self.breakfastList.append(inputValue)
		# clear inputField
		self.inputField.delete(0, 'end')
		# show message and clear it
		self.text.insert(self.tk.END, 'ADDED ' + inputValue)
		# save all breakfasts to file
		file = 'anyfile.txt'
		file = open(file, 'w', encoding = 'utf-8')
		text = ''
		for item in self.breakfastList:
			text += item + '\n'
		text = text[:-1]
		file.write(text)



	def clearText(self):
		self.text.delete(1.0, "end-1c")