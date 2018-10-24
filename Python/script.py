import sys
import functions

calendarEmail = sys.argv[1]
pingEndpoint = sys.argv[2]

earlyMeeting = functions.checkCalendar(calendarEmail)

if earlyMeeting:
    functions.pingPhone(pingEndpoint)
