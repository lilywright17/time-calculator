def add_time(start, duration, day_of_week=False):
  
#split the start time into hours, minutes, AM or PM
  start_tuple = start.partition(":")
  start_minutes_tuple = start_tuple[2].partition(" ")
  start_hours = int(start_tuple[0])
  start_minutes = int(start_minutes_tuple[0])
  am_pm = start_minutes_tuple[2]
  am_pm_flip = {"AM":"PM", "PM":"AM"}
#split the duration into hours and minutes
  duration_tuple = duration.partition(":")
  duration_hours = int(duration_tuple[0])
  duration_minutes = int(duration_tuple[2])

  #create a days of the week index for use later, lower case because we'll lower the day inputted
  days_of_week_index = {"monday": 0, "tuesday": 1, "wednesday": 2, "thursday": 3, "friday": 4, "saturday": 5, "sunday": 6}
#corresponding array so we can change new day back to a string
  days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
  
  #add the duration minutes to the start time minutes
#if we go over 59 we add an hour to the start time and start again at 00
  end_minutes = start_minutes + duration_minutes
  if (end_minutes >= 60):
    start_hours += 1
    end_minutes = end_minutes % 60
  
  end_hours = (start_hours + duration_hours) % 12

  amount_of_days = int(duration_hours/24)

  #we always want the minutes to be 2 digits
  if (end_minutes > 9):
    end_minutes = end_minutes
  else:
    end_minutes = "0" + str(end_minutes)
  #if end hours = 0 then this is actually 12am or pm
  if (end_hours == 0):
    end_hours = 12
  else:
    end_hours = end_hours

  if am_pm == "PM" and start_hours + (duration_hours % 12) >= 12:
    amount_of_days +=1
  #the total hours divided by 12 and rounded down to the nearest number provides the amount of times we switch from AM to PM
  amount_am_pm_flips = ((start_hours + duration_hours)/12)//1
  
  if (amount_am_pm_flips % 2 == 0):
    end_am_pm = am_pm
  else:
    end_am_pm = am_pm_flip[am_pm]

  return_time = str(end_hours) + ":" + str(end_minutes) + " " + str(end_am_pm)
  
  if(day_of_week):
    day_of_week = day_of_week.lower()
    index = int((days_of_week_index[day_of_week]) + amount_of_days) % 7
    new_day = days_of_week[index]
    return_time += ", " + new_day
  
  #work out how many days later it is
  if amount_of_days == 1:
    return_time += " " + "(next day)"
  if amount_of_days > 1:
    return_time += " " + "(" + str(amount_of_days) + " days later)"
  
  return return_time

print(add_time("9:15 PM", "5:30"))

   #"6:18 AM (20 days later)"