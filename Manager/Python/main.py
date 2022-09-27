from resource import Resource
from task import Task
from time_handler import TimeHandler
from time_handler import str_to_int
import yaml_handler


# Start the resource and the time Handler environment
def initializer(input_data):
	ram = input_data["ram"]
	begin = str_to_int(input_data["begin"])
	end = str_to_int(input_data["end"])
	resource = Resource(ram, begin, end)
	time_handler = TimeHandler(begin, end)
	return resource, time_handler


# Create the task with the input data
def task_initializer(task_data):
	name = task_data["name"]
	begin = str_to_int(task_data["begin"])
	duration = str_to_int(task_data["duration"])
	resource = task_data["ram"]
	return Task(name, begin, duration, resource)


# With the data in hand, this function will return a dictionary with the results
def dict_Maker(input_data, resource, time_handler):
	results = {}
	for task_data in input_data["tasks"]:
		task = task_initializer(task_data)
		begin = str(time_handler.get_available_begin(task.begin))
		end = str(time_handler.get_available_end(task.duration))
		results[task.name] = {'Begin': begin, 'End': end}
	return results


input_file_path = "data.yaml"
input_data = yaml_handler.load_yaml(input_file_path)
resource, time_handler = initializer(input_data)
results = dict_Maker(input_data, resource, time_handler)
yaml_handler.write_yaml(results, "results.yaml")
