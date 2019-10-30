from setuptools import setup, find_packages  # type: ignore

dev_requires = ["black"]
tests_require = ["pytest", "coverage", "pytest-cov", "mypy", "flake8", "tox"]
setup(
    name="kaon",
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
    description="",
    url="http://github.com/paulgessinger/kaon",
    author="Paul Gessinger",
    author_email="hello@paulgessinger.com",
    license="MIT",
    install_requires=[
        #"flask",
        "click",
        "peewee",
        "coloredlogs",
        "schema",
        "PyYAML"
    ],
    tests_require=tests_require,
    extras_require={"dev": dev_requires, "test": tests_require},
    entry_points={"console_scripts": ["kaon=kaon.cli:main"]},
    packages=find_packages("src"),
    package_dir={"": "src"},
)
