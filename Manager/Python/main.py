from resource import *
from task import *
from time_handler import *
import yaml_handler


def to_string(name, begin, end):
	return "task " + name + " will start after \"" + begin + "\" and end after \"" + end + "\""


# With the data in hand, this function will return a dictionary with the results
def dict_Maker(input_data):
	ram = input_data["ram"]
	begin = parse(input_data["inicio"])
	end = parse(input_data["fim"])
	resource = Resource(ram, begin, end)
	th = Time_handler(resource)
	dict = {}
	for i in range(0, len(input_data["tasks"])):
		name = input_data["tasks"][i]["nome"]
		begin = parse(input_data["tasks"][i]["inicio"])
		duration = parse(input_data["tasks"][i]["duracao"])
		begin = th.get_begin(begin)
		end = th.get_end(duration)
		dict[str(i + 1) + "_" +	name] = {'Begin': str(begin), 'End': str(end)}
	return dict


input_file_path = "data.yaml"
input_data = yaml_handler.load_yaml(input_file_path)
yaml_handler.write_yaml(dict_Maker(input_data), "results.yaml")
