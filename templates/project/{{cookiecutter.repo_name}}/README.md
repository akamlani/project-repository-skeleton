[![Testing {ci}](https://github.com/{{ cookiecutter.username }}/{{ cookiecutter.repo_name }}/actions/workflows/testing-ci.yml/badge.svg)](https://github.com/{{ cookiecutter.username }}/{{ cookiecutter.repo_name }}/actions/workflows/testing-ci.yml)


[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?hide_repo_select=true&ref=main&repo=492249131&machine=standardLinux32gb&location=EastUs)

# {{ cookiecutter.repo_name }}
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


Install Libraries, Documentation, and Dependencies
```sh
# installs the library in 'edit' mode for development into prior installed environment
# show be installed as: `{*-template}` in listing the packages (pip list | less ) as mentioned in setup.py
cd '{*-template}'
rm -r $(find . -name '*.egg-info')
pip uninstall <package_name>
pip install -e .
pip install -e ".[all]"
pip install -e ".[data]"
```
