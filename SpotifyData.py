from DragAndDropFile import DragAndDrop
from SelectionMenu import SelectionWindow
from Parser import parseAll, filterDate, parseArtist, parseSong, calcTotalTime, deleteUnknownArtists, splitByMonth
import sys, os
from PyQt5.QtWidgets import QApplication, QMainWindow
from Output import sortArtist, sortSongs


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

# the value of artistDict are objects of artistData
# which has members: msPlayed, mostPlayDate, mostPlayTime, currentDate, currentTime
artistDict = {}

if ui.aByMonth.isChecked():
    for month in aMonthlyData:
        month[1] = parseArtist(month[1])
else:
    artistDict = parseArtist(allData)


for i,j in artistDict.items():
    print(i,j)
    break

# the value of songDict is a linked list of songNodes
# songNode has members: timesPlayed, mostPlayDate, mostPlayTime, currentDate, currentCount, artistName
songList = []

if ui.sByMonth.isChecked():
    for month in sMonthlyData:
        month[1] = parseSong(month[1])
else:
    songList = parseSong(allData)

for month in songList:
    print(month)
    break

createPath = os.path.join(filePath, "_History.txt")
f = open(createPath, "w", encoding='utf8')
f.close()

"""
for i in data:
    if i["endTime"][0:4] == '2020':  # or i["endTime"][0:4] == '2019':
        th = th + int(i['msPlayed'])
        if i['artistName'] not in playHistoryDict2020.keys():
            playHistoryDict2020[i['artistName']] = i['msPlayed']
        if i['trackName'] not in mostPlaySong2020.keys():
            mostPlaySong2020[i['trackName']] = 1
        if int(i['msPlayed']) > 5000:
            mostPlaySong2020[i['trackName']] = mostPlaySong2020[i['trackName']] + 1
        playHistoryDict2020[i['artistName']] = playHistoryDict2020[i['artistName']] + i['msPlayed']

output1 = [(v, k) for k, v in playHistoryDict2020.items()]
output1.sort(reverse=True)
i = 1

file1 = open("history.txt", 'w', encoding='utf8')
file1.write("*************Most listened art*******************\n")
for v, k in output1:
    file1.write(str(i) + " " + str(k) + " " + str(v / 3600000) + " hours\n")
    if i >= 100:
        break
    i = i + 1

file1.write("\n*************Most played songs:************\n")
output2 = [(v, k) for k, v in mostPlaySong2020.items()]
output2.sort(reverse=True)
i = 1
for v, k in output2:
    if k == "Unknown Track":
        continue
    file1.write(str(i) + " " + str(k) + " " + str(v) + " times\n")
    if i >= 100:
        break
    i = i + 1

file1.write("\n***********totally hours listened: " + str(th / 3600000))
file1.close()
"""