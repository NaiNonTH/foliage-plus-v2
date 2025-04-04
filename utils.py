import re
import json

def get_file_name(str: str):
    return str[:str.rindex(".")]

def render_name_and_template(model, block, **kwargs):
    raw_template = json.dumps(model["template"])        \
                       .replace("{", "{{")              \
                       .replace("}", "}}")

    template = re.sub(r"%(\w+)%", r"{\1}", raw_template)\
                 .format(**kwargs)
    
    raw_name = model.get("name", block)
    name = re.sub(r"%(\w+)%", r"{\1}", raw_name)            \
             .format(**kwargs)

    return name, template