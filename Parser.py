import os, json


def parseAll(filePath):
    data = []
    for i in os.listdir(filePath):
        if i.startswith('StreamingHistory') and i.endswith('.json'):
            with open(os.path.join(filePath, i), 'r', encoding='utf8') as f:
                data = data + json.load(f)
    return data




# def removeUnknowSongs(data):
#     for songs in data:
#         if songs.artistName == 'Unknown Artist'