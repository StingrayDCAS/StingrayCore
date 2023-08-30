import openai
from sanitize import sanitize as san
from byond2json import hub2dict as h2d

def extract_server_from_status(status: str):
    response = openai.Completion.create(
        model="davinci:ft-herma-2023-08-30-18-50-26",
        prompt=((san(status))[:40]+" ->")
    )
    return response['choices'][0]['text'].strip().split("\n")[0].split(")")[0]

# testing
worlds = h2d()["worlds"]

for i in range(0,len(worlds)):
    if len(worlds[i]["players"]) > 10:
        print(extract_server_from_status(worlds[i]["status"]))
        