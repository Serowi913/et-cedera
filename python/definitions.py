import requests


def parse_for_definition(word):
    listx = str(requests.get(
        f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
        .content).split(
            '"definition":"')

    b = 0
    for i in listx:
        x = i.split('","')
        listx[b] = x[0]
        b += 1
    listx.pop(0)

    return listx

