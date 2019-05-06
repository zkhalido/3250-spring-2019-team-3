"""Module that will prompt for file info."""
# pylint: disable=E0211,R0903
# ****************************************************************************************
class FileNameInputPrompt:
    """Class to prompt for info."""
    def input_prompt():
        """Method that implements a file prompt."""
        name = str(input("What file do you want to run: "))
        extension = ".class"
        directory = "jvpm/javafiles/"
        new_name = directory + name + extension
        return new_name
# ****************************************************************************************
