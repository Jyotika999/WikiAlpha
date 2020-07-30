## building an example project with wikipedia api

import wikipedia

while True:
	inp = input("Question: ")
	print(wikipedia.summary(inp, sentences=2))
