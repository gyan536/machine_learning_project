from setuptools import find_packages , setup
from typing import List
HYPEN_E_DOT='-e.'
def get_requirment(file_path:str)-> List[str]:
    """Get the requirements from a file.

    Args:
        file_path (string): The path to the file containing the requirements.

    Returns:
        List of strings representing each requirement in the given file.
    """
    requirements =[]
    with open(file_path) as file_obj:
        requirements=file_obj.readline()
        requirements=[req.replace('/n',' ')for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

        return requirements

setup(
    name="machine_learning_project",
    version='0.1',
    packages=find_packages(),
    install_requires=get_requirment('requirements.txt'),
    author="Gyan Prakash Gupta"
    author_email="gyanprakashgupta53@gmail.com"
)