from dataclasses import dataclass
from datetime import timedelta


@dataclass
class Resource:
	__amount: int = 1024 * 16  # Default value (in MB)
	__begin: timedelta = timedelta(seconds=0)  # Default value
	__end: timedelta = timedelta(hours=24)  # Default value

	def getAmount(self):
		return self.__amount

	def getBegin(self):
		return self.__begin

	def getEnd(self):
		return self.__end
