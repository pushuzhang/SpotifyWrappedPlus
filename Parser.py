import os, json


# parse through all the json files and read all to the same dictionary
def parseAll(filePath):
    data = []
    for i in os.listdir(filePath):
        if i.startswith('StreamingHistory') and i.endswith('.json'):
            with open(os.path.join(filePath, i), 'r', encoding='utf8') as f:
                data = data + json.load(f)
    return data


# remove all song history outside of set time frame
def filterDate(data, start, end):
    for song in data:
        tempDate = removeTime(song['endTime']).split('-')
        if dateWithin(tempDate, start, end):
            continue
        data = [song for song in data if not dateWithin(tempDate, start, end)]
    return data


# check if the date is within the range of start and end
def dateWithin(date, start, end):
    startYear, startMonth, startDay = tuple(int(s) for s in start)
    endYear, endMonth, endDay = tuple(int(e) for e in end)
    if startYear <= int(date[0]) <= endYear:
        if startMonth <= int(date[1]) <= endMonth:
            if startDay <= int(date[2]) <= endDay:
                return True
    return False


# remove the time from a date
def removeTime(date):
    return date.split()[0]


# stores the information of a artist
class ArtistValue:
    def __init__(self, minutesPlayed, mostPlayDate, mostPlayTime, currentDate, currentTime):
        self.minutesPlayed = minutesPlayed
        self.mostPlayDate = mostPlayDate
        self.mostPlayTime = mostPlayTime
        self.currentDate = currentDate
        self.currentTime = currentTime


# parse through all the data and pick out data that relate to Artist
def parseArtist(data):
    # key = artistName : value = object of artist
    artistData = {}
    for song in data:
        if song.artistName in artistData.keys():
            artistData[song.artistName].minutesPlayed += song.msPlayed
            if removeTime(song.endTime) != artistData[song.artistName].currentDate:
                if artistData[song.artistName].mostPlayTime < artistData[song.artistName].currentTime:
                    artistData[song.artistName].mostPlayTime = artistData[song.artistName].currentTime
                    artistData[song.artistName].mostPlayDate = artistData[song.artistName].currentDate
                artistData[song.artistName].currentTime = song.msPlayed
                artistData[song.artistName].currentDate = removeTime(song.endTime)
            else:
                artistData[song.artistName].currentTime += song.msPlayed
        else:
            temp = ArtistValue(song.msPlayed, removeTime(song.endTime), song.msPlayed, removeTime(song.endTime), song.msPlayed)
            artistData[song.artistName] = temp








# def removeUnknowSongs(data):
#     for songs in data:
#         if songs.artistName == 'Unknown Artist'
