[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?hide_repo_select=true&ref=main&repo=492249131&machine=standardLinux32gb&location=EastUs)

# Project Repository Skeleton
Template for executing domain or use case specific projects


## Installation
Configure Project from Skeleton
After configuring the cookiecutter.json file in `templates/project`, execute the following scripts
```sh
> cd templates
> make setup
# in the root folder after the project has been created
> cd ..
> ./cookiecutter.sh
# this will create a directory with all files within that will serve as the Repo directory for a new project
# note the following depends on having a repo with a git directory
> make setup
# this will not install the dependencies and you can further install this package now as noted below
```
