import os
import json
import shutil
import utils
import re

from string import Template

if __name__ == "__main__":
    try:
        shutil.rmtree("pack")
    except FileNotFoundError:
        pass

    os.makedirs("pack")
    os.makedirs("pack/assets/minecraft/models/block")
    os.makedirs("pack/assets/minecraft/blockstates")

    shutil.copytree("templates/models", "pack/assets/minecraft/models/templates")
    shutil.copyfile("templates/pack.mcmeta", "pack/pack.mcmeta")

    with open("structure.json", "r") as file:
        structure = json.load(file)

    templates = structure.keys()

    for template_name in templates:
        local_structure = structure[template_name]

        if "all" in local_structure:
            model_structure = structure[local_structure["all"]]
        else:
            model_structure = local_structure

        blocks = local_structure.get("blocks", [])

        models = model_structure.get("models", None)
        blockstate = model_structure.get("blockstate", None)

        print(blocks)

        for block in blocks:
            if type(models) == str:
                models = structure[models]["models"]

            if type(models) == dict:
                if models is not None:
                    model_name, model_template = utils.render_name_and_template(models, template=template_name, name=block, block=block)

                    with open(f"pack/assets/minecraft/models/block/f_{model_name}.json", "w") as writer:
                        writer.write(model_template)

            elif type(models) == list:
                for model in models:
                    model_name, model_template = utils.render_name_and_template(model, template=template_name, name=block, block=block)

                    with open(f"pack/assets/minecraft/models/block/f_{model_name}.json", "w") as writer:
                        writer.write(model_template)

            if type(blockstate) == str:
                blockstate = structure[blockstate]["blockstate"]

            if blockstate is not None:
                blockstate_template = Template(json.dumps(blockstate))
                block_blockstate_template = blockstate_template.substitute(template=template_name, name=block)

                with open(f"pack/assets/minecraft/blockstates/{block}.json", "w") as writer:
                    writer.write(block_blockstate_template)

    print("build success!")