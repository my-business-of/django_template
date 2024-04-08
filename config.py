import argparse

params = {}
params_list = [
    {"name": "project_name", "help": "Project name for the Django app."},
    {"name": "secret_key", "help": "A secret key for this particular Django app."},
    {"name": "default_allowed_host", "help": "Hosts/domain names that are valid for this site.", "default": "*"},
    {"name": "debug", "help": "Debug allowed or not.", "default": True},
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


if __name__ == "__main__":
    get_params()
