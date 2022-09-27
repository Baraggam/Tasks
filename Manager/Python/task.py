from dataclasses import dataclass


@dataclass
class Task:
	_name: str
	_begin: int
	_duration: int
	_resource: int

	@property
	def name(self):
		return self._name

	@property
	def begin(self):
		return self._begin

	@property
	def duration(self):
		return self._duration

	@property
	def resource(self):
		return self._resource
