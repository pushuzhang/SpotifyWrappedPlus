# sorting Artist data base on the time listened
def sortArtist(artistDict):
    return dict(sorted(artistDict.items(), key=lambda item: item[1].msPlayed, reverse=True))


# sorting Song data base on the times listened
def sortSongs(songList):
    return sorted(songList, key=lambda item: item.timesPlayed, reverse=True)


# covert month format from ex. 200101 to January 2001
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


# covert millisecond to hours + minutes
def msToHour(ms):
    hours = int(ms / (1000 * 60 * 60))
    minutes = (ms / (1000 * 60)) % 60
    return '%d hours, %d minutes' % (hours, minutes)


# write the artist data to file base on user customization
def writeArtistData(aData, ui, f, sData):
    count = 0
    for name, data in aData.items():
        # increment the counter and top when the desired artists are meet
        if not ui.topSAll:
            count += 1
        f.write(name[:25].ljust(25) + '| ')
        f.write(msToHour(data.msPlayed).ljust(21) + '| ')
        if ui.aMPD.isChecked():
            f.write(('You listened to ' + name[:15] + ' the most on: ' + data.mostPlayDate +
                     ' for ' + msToHour(data.mostPlayTime)).ljust(85) + '| ')
        if ui.aTopSongs.isChecked():
            j = 0
            for song in sData:
                if song.artistName == name:
                    j += 1
                    f.write(str(j) + '. ' + song.songName[:20] + ' ')
                if j == ui.topSFromA:
                    break
        f.write('\n')
        if count == ui.topACount:
            break
    f.write('\n')


# write the Song data base on use customization
def writeSongData(sData, ui, f):
    count = 0
    for song in sData:
        if not ui.topAAll:
            count += 1
        f.write(song.songName[:25].ljust(25) + '| ')
        f.write(str(song.timesPlayed).ljust(4) + 'times | ')
        if ui.sMDL.isChecked():
            f.write('You listened to ' + song.songName[:15] + ' the most on: ' + song.mostPlayDate +
                    ' for ' + str(song.mostPlayTime) + ' times')
        f.write('\n')
        if count == ui.topSCount:
            break
    f.write('\n')
