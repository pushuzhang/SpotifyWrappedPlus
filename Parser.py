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
    def __init__(self, msPlayed, mostPlayDate, mostPlayTime, currentDate, currentTime):
        self.msPlayed = msPlayed
        self.mostPlayDate = mostPlayDate
        self.mostPlayTime = mostPlayTime
        self.currentDate = currentDate
        self.currentTime = currentTime


# parse through all the data and pick out data that relate to Artist
def parseArtist(data):
    artistData = {}
    for song in data:
        curArtistName = song['artistName']
        ms = song['msPlayed']
        et = song['endTime']
        if curArtistName in artistData.keys():
            artistData[curArtistName].msPlayed += ms
            if removeTime(et) != artistData[curArtistName].currentDate:
                if artistData[curArtistName].mostPlayTime < artistData[curArtistName].currentTime:
                    artistData[curArtistName].mostPlayTime = artistData[curArtistName].currentTime
                    artistData[curArtistName].mostPlayDate = artistData[curArtistName].currentDate
                artistData[curArtistName].currentTime = ms
                artistData[curArtistName].currentDate = removeTime(et)
            else:
                artistData[curArtistName].currentTime += ms
        else:
            temp = ArtistValue(ms, removeTime(et), ms, removeTime(et), ms)
            artistData[curArtistName] = temp
    return artistData


# stores the information of a song
class SongNode:
    def __init__(self, timesPlayed=None, mostPlayDate=None, mostPlayTime=None,
                 currentDate=None, currentCount=None, artistName=None):
        self.timesPlayed = timesPlayed
        self.mostPlayDate = mostPlayDate
        self.mostPlayTime = mostPlayTime
        self.currentDate = currentDate
        self.currentCount = currentCount
        self.artistName = artistName
        self.nextNode = None


class SLink:
    def __init__(self):
        self.startNode = None


def parseSong(data):
    songData = {}
    for song in data:
        curArtistName = song['artistName']
        curSongName = song['trackName']
        et = song['endTime']
        if curSongName in songData.keys():
            if song['msPlayed'] > 5000:
                curNode = songData[curSongName].startNode
                while curNode is not None:
                    if curNode.artistName == curArtistName:
                        curNode.timesPlayed += 1
                        if removeTime(et) != curNode.currentDate:
                            if curNode.mostPlayTime < curNode.currentCount:
                                curNode.mostPlayTime = curNode.currentCount
                                curNode.mostPlayDate = curNode.currentDate
                            curNode.currentCount = 1
                            curNode.currentDate = removeTime(et)
                        else:
                            curNode.currentCount += 1
                        break
                    if curNode.nextNode is None:
                        temp = SongNode(1, removeTime(et), 1, removeTime(et), 1, curArtistName)
                        curNode.nextNode = temp
                        break
                    curNode = curNode.nextNode
        else:
            songData[curSongName] = SLink()
            temp = SongNode(1, removeTime(et), 1, removeTime(et), 1, curArtistName)
            songData[curSongName].startNode = temp
    return songData


# calc the total time the user listened to Spotify
def calcTotalTime(data):
    msTotal = 0
    for song in data:
        msTotal += song['msPlayed']
    return msTotal


# delete all the Unknown Artists in the listening history
def deleteUnknownArtists(data):
    return [song for song in data if song['artistName'] is not 'Unknown Artist']

