def timeToSec(time):
	sec = 0
	temp = time.split(":")
	sec += int(temp[0]) * 3600  # Seconds in 1 hour
	sec += int(temp[1]) * 60  # Seconds in 1 minute
	sec += int(temp[2])  # 1 second
	return int(sec)


def secToTime(sec):
	hour = int(sec / 3600)  # Hour
	min = int((sec - hour * 3600) / 60)  # Minute
	seconds = sec % 60  # Second
	temp = fill(hour) + ":" + fill(min) + ":" + fill(seconds)
	return temp


def fill(time):
	out = str(time)
	if len(out) < 2:
		out = "0" + out
	return out


def toString(current, resource):
	data = resource.setMoment(current.getBegin(), current.getTime())
	return ("Task " + current.getName() +
			" will start at " + secToTime(data[0]) +
			" on day " + str(data[1]) +
			" and will end at " + secToTime(data[2]) +
			" on day " + str(data[3]))
