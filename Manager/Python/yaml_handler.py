import yaml


def load_yaml(file_path: str):
	with open(file_path) as stream:
		input_data = yaml.safe_load(stream)
	return input_data


def write_yaml(results, file_path: str):
	with open(file_path, 'w') as file:
		yaml.dump(results, file)
