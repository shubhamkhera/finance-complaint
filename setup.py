from setuptools import setup, find_packages
from typing import List

#Declaring variables for setup functions
PROJECT_NAME = "finance-complaint"
VERSION = "0.0.1"
AUTHOR = "Shubham Khera"
DESCRIPTION = "This is a sample for industry ready solution"
REQUIREMENT_FILE_NAME = "requirements.txt"

HYPHEN_E_DOT = "-e ."

def get_requirements_list(filepath: str) -> List[str]:
    """
    Description: This function is going to return the list of requirements
    mention in the requirements.txt file
    return This functio to return a list of requirements which contains the name of 
    libraries mentioned in the requirements.txt file
    """
    requirement_list = []
    with open(filepath) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace("\n","") for requirement_name in requirement_list]
        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
    return requirement_list
    
setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=get_requirements_list('requirements.txt')
)