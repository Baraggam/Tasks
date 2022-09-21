import yaml


def load_from_line(file_path: str):
	with open(file_path) as stream:
		input_data = yaml.safe_load(stream)
	return input_data
