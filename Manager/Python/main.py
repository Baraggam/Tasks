from resource import Resource
from task import Task
from time_handler import TimeHandler
from time_handler import str_to_int
import yaml_handler


# Start the variables environment
def start(input_data):
	ram = input_data["ram"]
	begin = str_to_int(input_data["begin"])
	end = str_to_int(input_data["end"])
	resource = Resource(ram, begin, end)
	time_handler = TimeHandler(begin, end)
	return resource, time_handler


# With the data in hand, this function will return a dictionary with the results
def dict_Maker(input_data, resource, time_handler):
	results = {}
	for task in input_data["tasks"]:
		name = task["name"]
		begin = str_to_int(task["begin"])
		duration = str_to_int(task["duration"])
		results[name] = {'Begin': str(time_handler.get_available_begin(
			begin)), 'End': str(time_handler.get_available_end(duration))}
	return results


input_file_path = "data.yaml"
input_data = yaml_handler.load_yaml(input_file_path)
resource, time_handler = start(input_data)
results = dict_Maker(input_data, resource, time_handler)
yaml_handler.write_yaml(results, "results.yaml")
