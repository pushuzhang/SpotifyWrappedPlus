def sortArtist(artistDict):
    return dict(sorted(artistDict.items(), key=lambda item: item[1].msPlayed, reverse=True))


def sortSongs(songList):
    return sorted(songList, key=lambda item: item.timesPlayed, reverse=True)


def monthToString(month):
    monthStrings = {'01': 'January',
                    '02': 'February',
                    '03': 'March',
                    '04': 'April',
                    '05': 'May',
                    '06': 'June',
                    '07': 'July',
                    '08': 'August',
                    '09': 'September',
                    '10': 'October',
                    '11': 'November',
                    '12': 'December'
                    }
    return monthStrings[month[4:]] + ' ' + month[0:4]


def writeArtistData(aData, ui, f, sData):
    count = 0
    for name, data in aData.items():
        # increment the counter and top when the desired artists are meet
        if not ui.topSAll:
            count += 1
        print('name:', name, end=' ')
        print('msPlayed:', data.msPlayed, end=' ')
        if ui.aMPD.isChecked():
            print("MostPlayedDay On:", data.mostPlayDate, "you listened to ____ for", data.mostPlayTime, end=' ')
        if ui.aTopSongs.isChecked():
            j = 0
            for song in sData:
                if song.artistName == name:
                    print(song.songName)
                    j += 1
                if j == ui.topSFromA:
                    break
        print()
        if count == ui.topACount:
            break
    print()


def writeSongData(sData, ui, f):
    count = 0
    for song in sData:
        if not ui.topAAll:
            count += 1
        print('name:', song.songName, end=' ')
        print('timesPlayed: ', song.timesPlayed, end=' ')
        if ui.sMDL.isChecked():
            print("MostPlayedDay On:", song.mostPlayDate, "you listened to ____ for", song.mostPlayTime, end=' ')
        print()
        if count == ui.topSCount:
            break
    print()










