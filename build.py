import os
import json
import shutil
import utils

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

    template_files = os.listdir("templates/models")

    with open("structure.json", "r") as file:
        structure = json.load(file)

    for template in template_files:
        template_name = utils.get_file_name(template)
        local_structure = structure[template_name]

        if "all" in local_structure:
            model_structure = structure[local_structure["all"]]
        else:
            model_structure = local_structure

        blocks = local_structure.get("blocks", [])

        model = model_structure.get("model", None)
        blockstate = model_structure.get("blockstate", None)

        for block in blocks:
            if type(model) == str:
                model = structure[model]["model"]
                
            if model is not None:
                model_template = Template(json.dumps(model["template"])).substitute(template=template_name, name=block)
                model_name = Template(model.get("name", block)).substitute(template=template_name, name=block)

            if type(blockstate) == str:
                blockstate = structure[blockstate]["blockstate"]
            elif blockstate is not None:
                blockstate_template = Template(json.dumps(blockstate))

            if model is not None:
                with open(f"pack/assets/minecraft/models/block/f_{model_name}.json", "w") as writer:
                    writer.write(model_template)

            if blockstate is not None:
                block_blockstate_template = blockstate_template.substitute(template=template_name, name=block)

                with open(f"pack/assets/minecraft/blockstates/{block}.json", "w") as writer:
                    writer.write(block_blockstate_template)

    print("build success!")