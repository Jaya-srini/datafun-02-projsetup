''' start a data analytics project '''
import pathlib


def create_project_directory(directory_name: str):
    """ 
    Creates a project sub-directory.
    :param directory_name: Name to be created, e.g. "test"
    """
    pathlib.Path(directory_name).mkdir(exist_ok=True)

def main(): 
    '''Scaffold a project'''
    create_project_directory(directory_name ='test') #name the parameter
    create_project_directory(directory_name ='docs') #name the parameter


# Add module block at the bottom
if __name__ == '__main__':
    main()