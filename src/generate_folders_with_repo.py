#!/usr/bin/env python3
##
## @Miou-zora Project, Mirror-Generator, 2023
## generate_folders_with_repo.py
## File description:
## Generate folders with repo and mirror repo in.
##

import subprocess

def generate_folders_with_repo(repo_ssh_link: str, user_name: str, repo_name: str, mirror_name: str):
    mirror_ssh_link = f"git@github.com:{user_name}/{mirror_name}.git"
    project_name = repo_ssh_link.split('-')[-2]
    actions = [(["mkdir", project_name], "Folder already exist: " + project_name),
               (["git", "clone", repo_ssh_link], "Can't clone repository: " + repo_ssh_link),
               (["mv", repo_name, project_name], "Can't move folder: " + repo_name),
               (["git", "clone", mirror_ssh_link], "Can't clone repository: " + mirror_ssh_link),
               (["mv", mirror_name, project_name], "Can't move folder: " + mirror_name)]
    for action in actions:
        if subprocess.run(action[0]).returncode == 1:
            raise Exception(action[1])
