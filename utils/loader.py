import yaml


def load_yaml(yaml_file):
    with open(yaml_file,"r") as f:
        content=f.read()
        json=yaml.load(content)
        return json