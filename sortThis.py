import os
import shutil
import datetime

with open('SortReport.txt', '+a') as f:
  directory = os.listdir(os.getcwd())
  print("Running Sort This Script\n", file=f)
  start = datetime.datetime.now()
  print(f"Started: {start}\n", file=f)

  try:

    def print_contents():
      """ Print directory contents """

      file_names = []
      for entry in os.listdir():
        file_names.append(entry)

      print(file_names, file=f)
      return file_names

    def create_sort_dir():
      """ Create the 'Sort This' directory"""
      ignore = ['Sort This', 'desktop.ini', 'SortReport.txt', 'readFileNames.py']
      file_names = []
      contents = os.listdir(os.getcwd());

      if 'Sort This' in contents:
        current_directory = os.getcwd()
        print(f'Sort This folder already exists\n', file=f)
        print(f'{current_directory} includes these files and directories:\n', file=f)
        print(f'{contents}\n', file=f)      
      else:
        print('Creating the \'Sort This\' directory\n', file=f)
        os.mkdir('Sort This')
      
      for entry in contents:        
        if entry in ignore:
          continue
        else:
          file_names.append(entry)

      print('Returning files and folders in the current directory for sorting:\n', file=f)  
      return file_names

    def add_files_to_dir(file_names, directory):
      """ Add files by name to the supplied directory """
      if file_names == []:
        print("No files or folders to sort...\n", file=f)
        return
      
      current_directory = os.getcwd()
      
      # ensure the supplied files are in this directory
      for entry in file_names:
        if entry not in os.listdir(os.getcwd()):
          print(f'Error: Could not find this file in the current directory: {entry}\n', file=f)
          return
      
      # ensure destination directory is a child of current directory
      if directory not in os.listdir(os.getcwd()):
        print(f'Error: Directory {directory} not found\n', file=f)
        print(f'Destination directory: {directory}\n', file=f)
        print(f'Current directory: {os.listdir(os.getcwd())}\n', file=f)
        return
      
      for entry in file_names:
        source_path = os.path.join(current_directory, entry)
        destination_path = os.path.join(current_directory, directory, entry)

        if os.path.isfile(source_path):
          shutil.move(source_path, destination_path)
          print(f"Moved File: {entry} to {destination_path}\n", file=f)
        
        if os.path.isdir(source_path):
          os.makedirs(destination_path, exist_ok=True)
          shutil.move(source_path, destination_path)
          print(f"Moved Folder: {entry} to {destination_path}\n", file=f)
    
    remaining = create_sort_dir()
    add_files_to_dir(remaining, "Sort This")

  except Exception as err:
    print(f"Something went wrong: {err}\n", file=f)
    
  finally:
    print("Cancelling Sort This Script\n", file=f)
    end = datetime.datetime.now()
    dif = end - start
    dif_in_seconds = dif.total_seconds()
    print(f"Cancelled: {end}\n", file=f)
    print(f"Time Ellapsed in seconds: {dif_in_seconds}\n\n\n", file=f)