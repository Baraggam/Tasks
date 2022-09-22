import yaml_handler
import task
from resource import *
from time_handler import *
import main


def test_timers():
	begin = parse("56:00:54")
	end = parse("80:02:00")
	resource = Resource(1024 * 16, begin, end)
	th = Time_handler(resource)
	test_begin = th.get_begin(parse("81:00:00"))
	teste_end = th.get_end(parse("00:00:01"))
	assert test_begin == timedelta(
		hours=152, seconds=54) and teste_end == timedelta(hours=152, seconds=55)


def test_load_file():
	data = yaml_handler.load_yaml("data.yaml")
	assert data["ram"] == 10000
	assert data["inicio"] == "56:00:54"
	assert data["tasks"][0]["nome"] == "task1"
