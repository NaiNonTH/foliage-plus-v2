import re
import json

def get_file_name(str: str):
    return str[:str.rindex(".")]

def write_model(model, block_name, template):
    model_name, model_template = render_name_and_template(model, template=template, name=block_name)

    with open(f"pack/assets/minecraft/models/block/f_{model_name}.json", "w") as writer:
        writer.write(model_template)

def write_blockstate(blockstate, block_name, **kwargs):
    raw_template = json.dumps(blockstate)               \
                       .replace("{", "{{")              \
                       .replace("}", "}}")

    template = re.sub(r"%(\w+)%", r"{\1}", raw_template)\
                 .format(**kwargs)
    
    with open(f"pack/assets/minecraft/blockstates/{block_name}.json", "w") as writer:
        writer.write(template)

def render_name_and_template(model, **kwargs):
    raw_template = json.dumps(model["template"])        \
                       .replace("{", "{{")              \
                       .replace("}", "}}")

    template = re.sub(r"%(\w+)%", r"{\1}", raw_template)\
                 .format(**kwargs)
    
    raw_name = model.get("name", kwargs["name"])
    name = re.sub(r"%(\w+)%", r"{\1}", raw_name)            \
             .format(**kwargs)

    return name, template