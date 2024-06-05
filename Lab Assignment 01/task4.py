#task 4

def insertionSort(lineup):
  for i in range(1, len(lineup)):
    train, dest, time = lineup[i]
    hour = int(time.split(":")[0])

    j = i - 1
    ptrain, pdest, ptime = lineup[j][0], lineup[j][1], lineup[j][2]
    prevHour = int(ptime.split(":")[0])
    while j>=0 and (ptrain > train or (ptrain == train and prevHour < hour)):
      lineup[j+1] = lineup[j]

      j -= 1
      ptrain, pdest, ptime = lineup[j][0], lineup[j][1], lineup[j][2]
      prevHour = int(ptime.split(":")[0])
    lineup[j+1] = (train, dest, time)
  return lineup

input_data = open("input4.txt","r")
output_data = open("output4.txt","w")

line1 = int(input_data.readline())

lineup = []

for i in range(line1):
  info = input_data.readline().split(" ")
  name = info[0]
  district = info[-3]
  time = info[-1][:-1]
  lineup.append([name,district,time])

sortedSchedule = insertionSort(lineup)

for i in range(line1):
  print(f"{sortedSchedule[i][0]} will departure for {sortedSchedule[i][1]} at {sortedSchedule[i][2]}", file = output_data)
