# combining wolframalpha with wikipedia

import wikipedia
import wolframalpha

while True:
	inp = input("Question: ")

	try:
		#try block will constitute the wolframalpha
		app_id = "app -id"
		client = wolframalpha.Client(app_id)
		res = client.query(inp)
		ans = next(res.results).text
		print (ans)

	except:
		# if wolframalpha block does not hold up well, then wikipedia block will get executed
		print(wikipedia.summary(inp))



