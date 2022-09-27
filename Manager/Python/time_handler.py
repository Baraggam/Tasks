from datetime import timedelta


class TimeHandler:
	def __init__(self, begin, end) -> None:
		self._one_day = timedelta(hours=24)
		self._begin = begin
		self._end = end
		self._timer = begin  # Will hold the elapsed time
		self._available_time = self._end - self._begin
		# How often does the cycle restart (minimum 1 day)
		self._days_to_reset = self._end + self._one_day - \
			(self._end %
			 self._one_day)

	# Returns the available begin timer
	def get_available_begin(self, time):
		self._check_and_jump(time)
		return self._timer

	# Returns the available end timer
	def get_available_end(self, time):
		self._add(time)
		self._check_and_jump(self._timer)
		return self._timer

	# Add the time to the timer
	def _add(self, add: timedelta):
		i = 0  # How many iterations to complete
		while add > self._available_time:
			i += 1
			add -= self._available_time
		self._timer += add + (self._days_to_reset * i)

	# Will make the timer go to the right place between the available time
	def _check_and_jump(self, time: timedelta):
		if time > self._timer:  # Adjusting the begin
			self._timer = time
			# Adjusting if the timer is behind the begin
			if (self._timer % self._days_to_reset) < self._begin:
				self._timer += self._begin - \
					(self._timer % self._days_to_reset)
			# Adjusting if the timer is after the end
			elif (self._timer % self._days_to_reset) >= self._end:
				self._timer += (self._begin + self._days_to_reset) - \
					(self._timer % (self._begin + self._days_to_reset))
		elif (time % self._days_to_reset) > self._end:  # Adjusting the end
			# Time between the end and the start
			self._timer += self._days_to_reset - self._available_time


# Returns the amount in seconds in a "HH:MM:SS" string
def str_to_int(time: str):
	seconds = [3600, 60, 1]  # seconds in one [hour, minute, second]
	sec = sum([a * b for a, b in zip(seconds, map(int, time.split(':')))])
	return timedelta(seconds=sec)
