import importlib
import json


def load_config(config_file):
    with open(config_file, 'r') as file:
        return json.load(file)

def execute_task(config):
    task_name = config['task']
    params = config['params']

    task_module = importlib.import_module(f'tasks.{task_name}')
    task_function = getattr(task_module, task_name)
    task_function(params)

if __name__ == '__main__':
    config = load_config('config/example_config.json')
    execute_task(config)
