from pathlib import Path

from setuptools import setup, find_packages

META_FILE = Path("src").absolute() / "app" / "__init__.py"
# testing requirements
EXTRAS_REQUIRES = {
    "tests": ["pytest", "pytest-mock", "coverage", "flake8"],
}

setup(
    name="app",
    version="1.0.0dev1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
    extras_require=EXTRAS_REQUIRES,
)
