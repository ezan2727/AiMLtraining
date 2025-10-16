# import os
# import inspect

# print('current working directory:', os.getcwd())

# function = inspect.getmembers(os, inspect.isbuiltin)

# print('all functions in os module:')
# for n,function in function:
#     print(n)

# import os

# print('current working directory:', os.getcwd())

# function = inspect.getmembers(os, inspect.isbuiltin)

# print('all functions in os module:')
# for n,function in function:
#     print(n)

# import os
# cdir = os.getcwd()
# print(cdir)

# import os
# cdir = os.getcwd()
# folder_name=input("Enter the folder name to create: ")
# folder_path=os.path.join(cdir,folder_name)
# if(os.path.exists(folder_path)):
#     print("folder already exists")
# else:
#     os.makedirs(folder_path)
#     print(f'{folder_name} folder created at {folder_path}')
#     print("folder not exists")

#rename a folder
# import os
# cdir = os.getcwd()
# old_name = input("Enter the folder name to rename: ")
# new_name = input("Enter the new folder name: ")
# old_folder_path = os.path.join(cdir, old_name)
# new_folder_path = os.path.join(cdir, new_name)
# if os.path.exists(old_folder_path):
#     os.rename(old_folder_path, new_folder_path)
#     print(f'folder renamed from {old_name} to {new_name}')
# else:
#     print(f'{old_name} folder does not exist')


# import os

# # Ask user to input the full path of the old folder
# old_path = input("Enter the full path of the folder to rename: ")
# # Ask user to input the new folder name only (not full path)
# new_name = input("Enter the new folder name: ")

# # Check if the old folder exists
# if os.path.exists(old_path):
#     # Get the parent directory of the folder
#     parent_dir = os.path.dirname(old_path)
#     # Join parent directory with the new folder name
#     new_path = os.path.join(parent_dir, new_name)
    
#     # Rename the folder
#     os.rename(old_path, new_path)
#     print(f"Folder has been renamed successfully to '{new_path}'")
# else:
#     print("The specified folder does not exist.")

