import os
import re
import argparse

params = {}
params_list = [
    {"name": "project_name", "help": "Project name for the Django app."},
    {"name": "secret_key", "help": "A secret key for this particular Django app."},
    {"name": "default_allowed_host", "help": "Hosts/domain names that are valid for this site.", "default": "*"},
    {"name": "debug", "help": "Debug allowed or not.", "default": True},
    {"name": "db_name", "help": "Database Name.", "default": "db_name"},
    {"name": "db_user", "help": "Database User.", "default": "db_user"},
    {"name": "db_password", "help": "Database Password.", "default": "db_password"},
    {"name": "db_host", "help": "Database Host.", "default": "db_host"},
    {"name": "db_port", "help": "Database Port.", "default": "db_port"},
]


def get_params():
    parser = argparse.ArgumentParser(description='Template config args parser.')

    for param in params_list:
        parser.add_argument('--' + param["name"], help=param["help"], default=param.get("default"))

    args = parser.parse_args()

    for param in params_list:
        value = getattr(args, param["name"])
        if value is None and param.get("default") is None:
            raise ValueError(f"Value or default not provided for parameter '{param['name']}'.")
        else:
            params[param["name"]] = value


def create_env_file():
    with open('.env', 'w') as f:
        for key, value in params.items():
            f.write(f'{key.upper()}={value}' + '\n')


def replace_words_in_file(filename: str, replacements: dict):
    with open(filename, 'r') as f:
        content = f.read()

    for old_word, new_word in replacements.items():
        content = re.sub(re.escape(old_word), new_word, content)

    with open(filename, 'w') as f:
        f.write(content)


if __name__ == "__main__":
    get_params()
    create_env_file()
    keys = {
        "{PROJECT_NAME}": params["project_name"]
    }

    default_project_name = 'django_template'
    # Walk through the directory tree rooted at default_project_name folder
    for root, dirs, files in os.walk(default_project_name):
        # Exclude the __pycache__ directory
        if '__pycache__' in dirs:
            dirs.remove('__pycache__')
        # Append absolute paths of all files to the list
        for file in files:
            file_path = os.path.join(root, file)
            replace_words_in_file(file_path, keys)

    os.rename(default_project_name, params["project_name"])
