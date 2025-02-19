#!/usr/bin/env python3
##
## @Miou-zora Project, Mirror-Generator, 2023
## main.py
## File description:
## Main file for mirror generator.
## Generate mirror, create folder for project and clone Epitech repository and Mirror repository.
##

from github import Github
from sys import argv
import json
from src.add_to_collaborators import *
from src.argument_manager import *
from src.push_mirror import *
from src.generate_mirror_workflow import *
from src.generate_folders_with_repo import *
from src.generate_mirror import *

def main():
    args = argumentManager()
    repo_info = args.sshKey[0].split(":")[1].split("/")
    json_file = json.load(open("data.json"))
    github_identifier: Github = Github(json_file["token"])
    orga_name = repo_info[0]
    repo_name = ".".join(repo_info[1].split(".")[:-1])
    mirror_name = (args.mirror_name[0] if (args.mirror_name != None) else f"{repo_name}-mirror")
    commit = (args.commit[0] if (args.commit != None) else "CI/CD push")
    generate_mirror(orga_name, repo_name, github_identifier, mirror_name)
    generate_folders_with_repo(args.sshKey[0], github_identifier.get_user().login, repo_name, mirror_name)
    generate_mirror_workflow(args.sshKey[0].split('-')[-2], args.sshKey[0], repo_name, mirror_name)
    add_collaborators(args.friend, mirror_name, github_identifier)
    push_mirror(mirror_name, args.sshKey[0].split('-')[-2], commit)

if __name__ == '__main__':
    main()
