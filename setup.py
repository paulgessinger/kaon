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
        "flask",
        "peewee",
        "coloredlogs",
    ],
    tests_require=tests_require,
    extras_require={"dev": dev_requires, "test": tests_require},
    packages=find_packages("src"),
    package_dir={"": "src"},
)
