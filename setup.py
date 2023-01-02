from setuptools import find_packages,setup  #find_packages convert our python code into packages [folder with name __init__.py will be consoder as packages
from typing import List

#WE are trying to run requirement.txt file line by line
REQUIREMENT_FILE_NAME = "requirements.txt"
HYPHEN_E_DOT = "-e ."

def get_requirements()->List[str]:  # the -> in this line represent thr=e type of the return
    with open (REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines() #it will return list requirements line by line

        """the requirement.txt file contains '\n' which is not a library name so we replace it with nothing"""
    requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]

    #we are removing -e. file beacause its not a library we just need libraries in requirement_list file
    if HYPHEN_E_DOT in requirement_list:
        requirement_list.remove(HYPHEN_E_DOT)
    return requirement_list


setup(
    name  = "sensor",
    version = "0.0.1",
    author = "praful",
    author_email = "pbhojane1609@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements(),#it is asking us which libraries we are requires formproject

)
