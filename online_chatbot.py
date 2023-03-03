from toolkit.queryGPT import query_davinci

start_of_prompt = """
you a re a friendly chatbot instantiated in a robotic barista.
be friendly with the guests, and try to strike up conversation if you can
all of your responses should be formatted as a json object exactly like this

{"reply": <a string with the response in plain text>}

you have the content of the last several interactions so you can get some context.
they will be formatted as a python style list of strings that identify who said what
"""


memory = []

while True:
    if len(memory) >= 10:
        memory.pop(0)  # remove the oldest query

    prompt = input("input your query: ")
    if prompt.upper() == "QUIT":
        break
    memory.append(f"the user said: {prompt}")  # add the new query to the list

    outgoing_prompt = f"{start_of_prompt} {str(memory)}"
    response = query_davinci(outgoing_prompt)
    print(response)
    memory.append(f"eunice said: {response}")
