#!/usr/bin/env python3
##
## @Miou-zora Project, Mirror-Generator, 2023
## generate_mirror_workflow.py
## File description:
## Add CI/CD in mirror of `repo_name`.
##

import subprocess

def generate_mirror_workflow(binary_name: str, repo_ssh: str, repo_name:str, mirror_name: str):
    f = open("verif_mirror.yml", "r")
    mirror_file_data = f.read()
    f.close()
    mirror_file_data = mirror_file_data.replace("MIRROR_URL_MIRROR_GENERATOR", repo_ssh)
    mirror_file_data = mirror_file_data.replace("EXECUTABLE_MIRROR_GENERATOR", binary_name)
    actions = [(["mkdir", f"{binary_name}/{mirror_name}/.github"], "Folder already exist: " + f"{binary_name}/{mirror_name}/.github"),
               (["mkdir", f"{binary_name}/{mirror_name}/.github/workflows"], "Folder already exist: " + f"{binary_name}/{mirror_name}/.github/workflows")]
    for action in actions:
        if subprocess.run(action[0]).returncode == 1:
            raise Exception(action[1])
    mirror_file = open(f"{binary_name}/{mirror_name}/.github/workflows/verif_mirror.yml", "w")
    mirror_file.write(mirror_file_data)
    mirror_file.close()
