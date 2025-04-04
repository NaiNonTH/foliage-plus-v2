import os
import json
import shutil
import utils

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

        for block in blocks:
            if type(models) == str:
                models = structure[models]["models"]
                
            if type(models) == dict:
                if models is not None:
                    utils.write_model(models, block, template_name)
            elif type(models) == list:
                for model in models:
                    utils.write_model(model, block, template_name)

            if type(blockstate) == str:
                blockstate = structure[blockstate]["blockstate"]

            if blockstate is not None:
                utils.write_blockstate(blockstate, block, template=template_name, name=block)

    print("build success!")