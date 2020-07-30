# combining wolframalpha with wikipedia

import wikipedia
import wolframalpha

while True:
	inp = input("Question: ")

	try:
		#try block will constitute the wolframalpha
		app_id = "JXK66Y-GYUWJ325W8"
		client = wolframalpha.Client(app_id)
		res = client.query(inp)
		ans = next(res.results).text
		print (ans)

	except:
		# if wolframalpha block does not hold up well, then wikipedia block will get executed
		print(wikipedia.summary(inp))



