# git-overleaf-sync


This guide outlines the steps to integrate your Overleaf project with a GitHub repository. This integration allows you to collaborate on your LaTeX documents using Overleaf while also version-controlling your project on GitHub. This project more or less tries to bypass the (paid) Github integration as offered by Overleaf. 

## Prerequisites

- [Git](https://git-scm.com/) installed on your local machine.
- An Overleaf project that you want to connect to a GitHub repository.
- A GitHub repository where you want to store the version-controlled code.

## Setup Steps

### 1. Clone Overleaf Project

Clone your Overleaf project to your local machine using the following commands:

```bash
git clone <Overleaf_project_URL> <Overleaf_project_directory>
cd <Overleaf_project_directory>
```

### 2. Add GitHub Remote
Create a private repository on Github with `main` branch initialised.

Add your GitHub repository as a remote to your local Overleaf project:

```bash
git remote add <github_remote_name> <GitHub_repository_URL>
git fetch <github_remote_name>
```
### 3. Setup Local Branch
Create and switch to a local branch that will track the main branch of your GitHub repository:

```bash
git checkout -b <local_branch_name> <github_remote_name>/main
```
That's all for the manual git setup.

## Using git-overleaf-sync

### 1. Clone this repo
```bash
git clone git@github.com:sahiljhawar/git-overleaf-sync.git
```
and install `colorama` for colored terminal output
`pip install colorama`

### 2. Usage 

> [!WARNING]
> Only works with `python3`

```bash
python3 main.py --path <Overleaf_project_directory [fullpath]> --local <local_branch_name> --refresh <refresh time in seconds>
```
Use `<Overleaf_project_directory>` and `<local_branch_name>` as used during the intial setup
 
Code should be self explanatory.

> [!TIP]
> In principle this should work with Gitlab, Bitbucket and other Git based repository hosting services.
