from resource import *
from datetime import timedelta


class Time_handler:
	def __init__(self, resource) -> None:
		self.__one_day = timedelta(hours=24)
		self.__begin = resource.getBegin()
		self.__end = resource.getEnd()
		self.__timer = resource.getBegin()  # Will hold the elapsed time
		self.__available_time = self.__end - self.__begin
		# How often does the cycle restart (minimum 1 day)
		self.__days_to_reset = self.__end + self.__one_day - \
			(self.__end %
			 self.__one_day)

	# Returns the available begin timer
	def get_begin(self, time):
		self.__check_and_jump(time)
		return self.__timer

	# Returns the available end timer
	def get_end(self, time):
		self.__add(time)
		self.__check_and_jump(self.__timer)
		return self.__timer

	# Add the time to the timer
	def __add(self, add: timedelta):
		i = 0  # How many iterations to complete
		while add > self.__available_time:
			i += 1
			add -= self.__available_time
		self.__timer += add + (self.__days_to_reset * i)

	# Will make the timer go to the right place between the available time
	def __check_and_jump(self, time: timedelta):
		if time > self.__timer:  # Adjusting the begin
			self.__timer = time
			# Adjusting if the  timer is behind the begin
			if (self.__timer % self.__days_to_reset) < self.__begin:
				self.__timer += self.__begin - \
					(self.__timer % self.__days_to_reset)
			# Adjusting if the  timer is after the end
			elif (self.__timer % self.__days_to_reset) >= self.__end:
				self.__timer += (self.__begin + self.__days_to_reset) - \
					(self.__timer % (self.__begin + self.__days_to_reset))
		elif (time % self.__days_to_reset) > self.__end:  # Adjusting the end
			# Time between the end and the start
			self.__timer += self.__days_to_reset - self.__available_time


# Returns the amount in seconds in a "HH:MM:SS" string
def parse(time: str):
	seconds = [3600, 60, 1]  # seconds in one [hour, minute, second]
	sec = sum([a * b for a, b in zip(seconds, map(int, time.split(':')))])
	return timedelta(seconds=sec)
