import sys

# format: ('_major', '_minor', '_patch')
__version__ = "{{ cookiecutter.version }}"
watermark = dict(python=f"{sys.version_info.major}.{sys.version_info.minor}")
