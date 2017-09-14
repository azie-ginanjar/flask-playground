from setuptools import setup

setup(
    name='flask-playground',
    version='1.0',
    long_description=__doc__,
    packages=['app', 'app.api'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask'],
    entry_points={
        "console_scripts": ["flask-playground=app.__main__:run_cli"],
    },
)