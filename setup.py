# This will make our ML application as Package and upload into Pypi, so that anybody can use it
from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return a list of requirements

    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
    return requirements

setup(
    name = "mlProject",
    version='0.0.1',
    author="Yashswi Jain",
    author_email="yashswijain@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)

# to find how many no. of packages --> We have to create one "src" folder 