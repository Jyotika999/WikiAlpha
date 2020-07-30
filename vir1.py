##coding wolfram api into our application


import wolframalpha
inp = input("Question: ")
app_id = "app-id"
client = wolframalpha.Client(app_id)

res = client.query(inp)
answer = next(res.results).text

print(answer)

