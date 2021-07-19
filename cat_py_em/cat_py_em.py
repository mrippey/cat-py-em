from pathlib import Path 
from datetime import datetime
import click 


def check_file_time(filetime):
    """Function to retreive timestamp

    Args:
        filetime datetime

    Returns: 
        In conjunction with the below function, returns 
        last modified timestamp of a file.
    """
    dtime = datetime.utcfromtimestamp(filetime)
    return dtime.strftime("%d %b %Y")


def view_directory_contents(filepath):
    """Function to work with directory or file and 
    return appropriate information

    Args:
        filepath = pathlib.Path()

    Returns: 
       The contents of a file if a file is provided,
       or the contents of a directory when a directory
       is provided.
    """
    if Path(filepath).is_file():
        print(Path(filepath).read_text())
    
    elif Path(filepath).is_dir():
        print(f'Displaying directory path for: {filepath}\n')
        test = Path(filepath)
        
        for pth in test.iterdir():
            file_pth = pth.stat()
            dir_contents_info = f"[+] {pth.name:<25s}   Last Modified: {check_file_time(file_pth.st_birthtime):<12s}"
            click.echo(dir_contents_info)

    

@click.command()
@click.argument('filepath')
def main(filepath):
    """
    A small tool to build confidence and keep busy. This tool 
    was built to emulate just a few of the functionailities of the *nix cat 
    command. Provide a path containing a file or directory to lookup.\n
    Here are two examples:

    1. /etc/hosts/

    2. /tmp/example.txt

    This tool was built to continue strengthening my skills in Python. Code
    revisions and updates may/may not occur.
    """
    file_output = view_directory_contents(filepath)
   
    click.echo(file_output)
 

if __name__ == '__main__':
    main() 

