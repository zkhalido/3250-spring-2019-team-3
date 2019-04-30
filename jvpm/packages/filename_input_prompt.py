"""Module that will prompt for file info."""
class FileNameInputPrompt:
    """Class to prompt fro info."""
    def input_prompt():
        """Method that implements the prompt."""
        name = str(input("What file do you want to run: "))
        extension = ".class"
        directory = "jvpm/javafiles/"
        new_name = directory + name + extension
        return new_name
