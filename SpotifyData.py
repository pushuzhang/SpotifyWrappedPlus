from DragAndDropFile import DragAndDrop
from SelectionMenu import SelectionWindow
from Parser import parseAll, filterDate, parseArtist, parseSong, calcTotalTime, deleteUnknownArtists, splitByMonth
import sys, os
from PyQt5.QtWidgets import QApplication, QMainWindow
from Output import sortArtist, sortSongs, monthToString, writeArtistData, writeSongData

# Main
inputApp = QApplication(sys.argv)
win1 = DragAndDrop()
win1.show()
inputApp.exec_()

if not win1.hasData:
    print("No filePath found, Exiting")
    sys.exit()

selectionApp = QApplication(sys.argv)
win2 = QMainWindow()
ui = SelectionWindow()
ui.setupUi(win2)
win2.show()
selectionApp.exec_()

# reading all streaming history files from the given directory
filePath = win1.filePath
allData = parseAll(filePath)

# filter the date base on the time frame set
if ui.setTime.isChecked():
    allData = filterDate(allData, ui.startTime.date().getDate(), ui.endTime.date().getDate())

# calculating the total listening time
totalTime = calcTotalTime(allData)

# remove all the unknown artists
allData = deleteUnknownArtists(allData)

# if the user request by monthly data
aMonthlyData = []
sMonthlyData = []
if ui.aByMonth.isChecked() or ui.sByMonth.isChecked():
    aMonthlyData = splitByMonth(allData)
    sMonthlyData = splitByMonth(allData)

# creating dictionary for artists and songs

# artistDict is a dictionary
# the key of artistDict are name of the artists
# the value of artistDict are objects of artistData
# which has members: msPlayed, mostPlayDate, mostPlayTime, currentDate, currentTime

# when reading by monthly
# monthly artist data is a list of tuples
# each tuple consists of the month of the data and a artistDict
artistDict = {}

# reading data by month / not by month then sort it
if ui.topA.isChecked():
    if ui.aByMonth.isChecked():
        for month in aMonthlyData:
            tempArtist = parseArtist(month[1])
            month[1] = sortArtist(tempArtist)
        for month in sMonthlyData:
            tempSong = parseSong(month[1])
            month[1] = sortSongs(tempSong)
    else:
        tempArtist = parseArtist(allData)
        artistDict = sortArtist(tempArtist)

# the value of songDict is a linked list of songNodes
# songNode has members: timesPlayed, mostPlayDate, mostPlayTime, currentDate, currentCount, artistName
songList = []

if ui.sByMonth.isChecked():
    for month in sMonthlyData:
        tempSong = parseSong(month[1])
        month[1] = sortSongs(tempSong)
else:
    tempSong = parseSong(allData)
    songList = sortSongs(tempSong)

# creating a history file with the the user's input data folder
createPath = os.path.join(filePath, "_History.txt")
f = open(createPath, "w", encoding='utf8')

if ui.topA.isChecked():
    if ui.aByMonth.isChecked():
        for aMonth, sMonth in zip(aMonthlyData, sMonthlyData):
            print(monthToString(aMonth[0]))
            writeArtistData(aMonth[1], ui, f, sMonth[1])
    else:
        writeArtistData(artistDict, ui, f, songList)

if ui.sByMonth.isChecked():
    for month in sMonthlyData:
        print(monthToString(month[0]))
        writeSongData(month[1], ui, f)
else:
    writeSongData(songList, ui, f)
f.close()
