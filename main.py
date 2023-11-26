import os
import hashlib
import subprocess
import argparse
import time
from colorama import Fore, Style
import colorama


def get_parser():
    parser = argparse.ArgumentParser(description="Sync Overleaf with Github")

    parser.add_argument("--path", type=str, required=True, help="Path to the repo")

    parser.add_argument(
        "--local",
        type=str,
        required=True,
        help="Name of the local branch which was used during the initialisation",
    )

    parser.add_argument(
        "--refresh",
        type=float,
        default=10,
        help="Refresh time in seconds",
    )

    return parser


def hash_folder(folder_path):
    hash_value = hashlib.md5()

    for root, dirs, files in os.walk(folder_path):

        if ".git" in dirs:
            dirs.remove(".git")

        if "README.md" in files:
            files.remove("README.md")
        for file in sorted(files):
            file_path = os.path.join(root, file)
            with open(file_path, "rb") as f:
                content = f.read()
                hash_value.update(content)

    return hash_value.hexdigest()


def checkout_to_origin():
    result = subprocess.run(
        ["git", "checkout", "master"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True,
    )
    print(result.stdout.decode("utf-8"))


def pull_from_origin():
    result = subprocess.run(
        ["git", "pull", "origin", "master"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True,
    )

    print(result.stdout.decode("utf-8"))


def checkout_to_local(local_branch_name):
    result = subprocess.run(
        ["git", "checkout", local_branch_name],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True,
    )
    print(result.stdout.decode("utf-8"))


def merge_OL_to_GH():
    result = subprocess.run(
        ["git", "merge", "origin/master", "--allow-unrelated-histories"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True,
    )
    print(result.stdout.decode("utf-8"))


def push_to_GH():
    result = subprocess.run(
        ["git", "push", "github", "HEAD:main"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True,
    )

    print(result.stdout.decode("utf-8"))


parser = get_parser()
args = parser.parse_args()
repo_directory = args.path

colorama.init()
while True:
    old_hash = hash_folder(repo_directory)

    os.chdir(repo_directory)
    pull_from_origin()

    new_hash = hash_folder(repo_directory)

    if old_hash != new_hash:
        print(
            f"\n{Fore.RED}***********Changes found on Overleaf... Merging them to the"
            " Github repository***********"
        )

        checkout_to_local(args.local)
        merge_OL_to_GH()
        print(Style.RESET_ALL)
        push_to_GH()
        print(Fore.GREEN)
        checkout_to_origin()
        print(Style.RESET_ALL)

    else:
        print(f"{Fore.GREEN}No changes found...{Style.RESET_ALL}\n")

    time.sleep(args.refresh)
