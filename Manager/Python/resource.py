from dataclasses import dataclass


@dataclass
class Resource:
	# Amount of the RAM in the system (im MB)
	# Begin and End is the delimiters of the available time (in seconds)
	# Elapsed time since the time 0 of the program (in seconds)
	__amount: int
	__begin: int
	__end: int
	__elapsedTime: int

	def getAmount(self):
		return self.__amount

	def getBegin(self):
		return self.__begin

	def getEnd(self):
		return self.__end

	def getElapsedTime(self):
		return self.__elapsedTime

	# Returns the  amount of time that the resource was active (in seconds)
	# 86400 is the seconds in one day
	def __getUsage(self):
		x = int(self.__elapsedTime / 86400) * self.__getTimePerDay()
		if (self.__elapsedTime % 86400 >= self.__end):
			x += self.__getTimePerDay()
		else:
			x += (self.__elapsedTime % 86400) - self.__begin
		return int(x)

	# Returns the available time per day
	def __getTimePerDay(self):
		return int(self.__end - self.__begin)

	# Returns the non available time per day
	def __getRestPerDay(self):
		return int(86400 - self.__getTimePerDay())

	# Returns the available second of the day
	# The end variable controls how the number will return
	# If it ends at the end mark, will show the end time and not the begin time

	def __getSecDay(self, end):
		x = int(self.__begin + self.__getUsage()) % self.__getTimePerDay()
		if end and x % self.__getTimePerDay() == 0:
			x = self.getEnd()
		return x

	# Returns the day of a available second
	# The end variable controls how the number will return
	# If it ends at the end mark, will show the current day and not the next one

	def __getDay(self, end):
		usage = self.__getUsage()
		x = int(usage / self.__getTimePerDay())
		if end and usage % self.__getTimePerDay() == 0:
			x -= 1
		return x

	# Add the seconds to the variable and returns the begin and the end of the task
	# out[0] - The second of the start
	# out[1] - The day of the start
	# out[2] - The second of the end
	# out[3] - The day of the end
	def setMoment(self, begin, time):
		out = [0] * 4
		if begin <= self.__elapsedTime:
			x = self.__getSecDay(False)
			out[0] = x
			out[1] = self.__getDay(False)
			if x + time > self.__getTimePerDay():
				self.__elapsedTime += time + \
					int((time / self.__getTimePerDay()) * self.__getRestPerDay())
			else:
				self.__elapsedTime += time
			out[2] = self.__getSecDay(True)
			out[3] = self.__getDay(True)
		else:
			self.__elapsedTime = begin
			newBegin = int(self.__elapsedTime % 86400)
			if newBegin <= self.__end:
				out = self.setMoment(newBegin, time)
			else:
				self.__elapsedTime += 86400 - newBegin
				out = self.setMoment(newBegin, time)
		return out
