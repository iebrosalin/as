import yaml

def read_yaml(path: str) -> dict:
    with open(path,  encoding='utf-8') as fh:
        data_template = yaml.safe_load(fh)
    return data_template