from dataclasses import dataclass
from datetime import timedelta


@dataclass
class Resource:
	_amount: int = 1024 * 16  # Default value (in MB)
	_begin: timedelta = timedelta(seconds=0)  # Default value
	_end: timedelta = timedelta(hours=24)  # Default value

	@property
	def amount(self):
		return self._amount

	@property
	def begin(self):
		return self._begin

	@property
	def end(self):
		return self._end
