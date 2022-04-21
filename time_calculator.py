def add_time(start, duration, dayofWeek=None):
  currHour = int(start.split(':')[0])
  currMin = int(start.split(':')[1].split()[0])
  time = start.split()[1]
  deltaHours = int(duration.split(':')[0])
  deltaMin = int(duration.split(':')[1])
  newHour = currHour
  newMin = currMin
  daysLater = 0
  daysOfWeek = ['blank', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
  if (dayofWeek != None):
      dayofWeek = dayofWeek.upper()
      dayIndex = 0
      for day in daysOfWeek:
         if (dayofWeek == day.upper()):
            dayIndex = daysOfWeek.index(day)

  newMin = newMin + deltaMin
  if (newMin > 60):
    newHour = newHour + 1
    newMin = newMin - 60
  if (newMin < 10):
    newMin = "0" + str(newMin)
  newHour = newHour + deltaHours
  while (newHour > 24):
    daysLater = daysLater + 1
    newHour = newHour - 24
  if (newHour > 12):
    newHour = newHour - 12
    if (time == 'PM'):
      time = 'AM'
      daysLater = daysLater + 1
    else:
      time = 'PM'
  if (newHour == 12):
    if (time == 'PM'):
      time = 'AM'
      daysLater = daysLater + 1
    else:
      time = 'PM'
  daysLaterT = daysLater
  while (daysLaterT > 6):
      daysLaterT = daysLaterT - 7
  new_time = str(newHour) + ":" + str(newMin) + " " + time
  if (dayofWeek != None):
        print("dAY INDEX: " + str(daysLaterT+dayIndex))
        new_time = new_time + ", " + daysOfWeek[daysLaterT+dayIndex]
  if (daysLater > 0):
    if (daysLater == 1):
        new_time = new_time + " (next day)"
    else:
        new_time = new_time + " (" + str(daysLater) + " days later)"  
  return new_time