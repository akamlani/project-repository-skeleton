from pathlib import Path

from setuptools import find_namespace_packages, setup

# read description for long-form description
with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

# read requirements for core development installation
with open(Path("{{ cookiecutter.env_dep_path }}").joinpath("requirements.txt"), encoding="utf-8") as f:
    requirements = [line.strip() for line in f if len(line) > 1 and "#" not in line]

# read requirements for core development installation
# pip install packagename[ui]
# pip install -e ".[all]"
extra = {}
files = [*Path("{{ cookiecutter.env_dep_path }}").glob("**/requirements_*")]
etypes = [f.stem.split("_")[-1] for f in files]
for etype, filepath in zip(etypes, files):
    with open(filepath, encoding="utf-8") as f:
        extra[etype] = [line.strip() for line in f if len(line) > 1 and "#" not in line]
# repackage information
extra["all"] = [item for sublist in extra.values() for item in sublist]

### development mode, editable
# python setup.py develop
# pip    install -e .
setup(
    name="{{ cookiecutter.pkg_install_name }}",
    version="{{ cookiecutter.version }}",
    # author information
    author="{{ cookiecutter.full_name.replace('\"', '\\\"') }}",
    author_email="{{ cookiecutter.email }}",
    # descriptions
    description="{{ cookiecutter.project_description }}",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="{{ cookiecutter.license }}",
    keywords="{{ cookiecutter.project_keywords }}",
    classifiers=[
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
    ],
    # URIs
    url="https://github.com/{{ cookiecutter.username }}/{{ cookiecutter.repo_name }}",
    project_urls={
        "Bug Tracker": "https://github.com/{{ cookiecutter.username }}/{{ cookiecutter.repo_name }}/issues",
    },
    # what is packaged here
    python_requires=">=3.7",
    install_requires=requirements,
    packages=find_namespace_packages(include=["{{ cookiecutter.pkg_name }}.*"]),
    extras_require=extra,
    # testing packages
    test_suite="tests",
    tests_require=extra["test"],
    # include perspective data
    include_package_data=True,
    package_data={"{{ cookiecutter.pkg_name }}": ["*.txt", "*.rst", "*.md"]},
    zip_safe=False,
)
