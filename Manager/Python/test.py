from datetime import timedelta
from resource import Resource
from task import Task
from time_handler import TimeHandler
from time_handler import str_to_int
import yaml_handler
import main


def test_timers():
	begin = str_to_int("480:05:00")
	end = str_to_int("482:05:00")
	resource = Resource(1024 * 16, begin, end)
	time_handler = TimeHandler(begin, end)
	test_begin = time_handler.get_available_begin(str_to_int("483:00:00"))
	teste_end = time_handler.get_available_end(str_to_int("00:10:00"))
	assert test_begin == timedelta(
		hours=984, minutes=5) and teste_end == timedelta(hours=984, minutes=15)


def test_load_file():
	data = yaml_handler.load_yaml("data.yaml")
	assert data["ram"] == 10000
	assert data["begin"] == "56:00:54"
	assert data["tasks"][0]["name"] == "task_1"
