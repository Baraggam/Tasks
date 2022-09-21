from dataclasses import dataclass


@dataclass
class Task:
	__name: str
	__begin: int
	__time: int
	__resource: int

	def getName(self):
		return self.__name

	def getBegin(self):
		return self.__begin

	def getTime(self):
		return self.__time

	def getResource(self):
		return self.__resource
