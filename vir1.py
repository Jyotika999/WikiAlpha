##coding wolfram api into our application


import wolframalpha
inp = input("Question: ")
app_id = "JXK66Y-GYUWJ325W8"
client = wolframalpha.Client(app_id)

res = client.query(inp)
answer = next(res.results).text

print(answer)

