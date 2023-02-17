import time
from rich import align
import random
from rich.progress import Progress
import os
import win32api

file_name = "executions.txt"

fd = os.open(file_name, os.O_CREAT | os.O_WRONLY | os.O_TRUNC, 0o600)
#fd stands for file descriptor
#0o600 specified file permission

os.close(fd)

def run_once(package):
    import subprocess
    import sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    
if not os.path.exists(file_name):
    #Run the function
    run_once("rich")
    run_once("progress")
    with open(file_name, "w") as f:
        f.write("")
        win32api.SetFileAttributes(file_name, win32api.FILE_ATTRIBUTE_HIDDEN)
        print(bool(win32api.GetFileAttributes(file_name) & win32api.FILE_ATTRIBUTE_HIDDEN))
     
else:
    #Do not run the funtion
    pass


def task1():
    with Progress() as progress:
        task = progress.add_task("[cyan]INITIALIZING PROGRAM PLEASE WAIT...",total=1000)
        
        while not progress.finished:
            progress.update(task, advance=7)
            time.sleep(0.02)
def task2():
    with Progress() as progress:
        task = progress.add_task("[green]FETCHING THE ALGORITHM...",total=1000)
        
        while not progress.finished:
            progress.update(task, advance=7)
            time.sleep(0.02)

def task3():
    with Progress() as progress:
        task = progress.add_task("[red]READING THE PROGRAM...",total=1000)
        
        while not progress.finished:
            progress.update(task, advance=7)
            time.sleep(0.02)

task_list = [task1, task2, task3]
chosen_task = random.choice(task_list)
chosen_task()