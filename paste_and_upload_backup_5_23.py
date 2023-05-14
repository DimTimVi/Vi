import os
import pyperclip
import subprocess


def get_txt_files_in_dir(directory):
    # List all files in the directory
    files_in_dir = os.listdir(directory)

    # Filter for .txt files
    txt_files = [file for file in files_in_dir if file.endswith('.txt')]

    return txt_files


def create_jekyll_file(jekyll_site_dir, content):
    # Prompt for the name of the new file
    new_file_name = input("Enter the name of the new file (without the extension):\n") + '.md'

    # Define the new file path and name
    new_file_dir = os.path.join(jekyll_site_dir, 'content')
    new_file_path = os.path.join(new_file_dir, new_file_name)

    # Create the necessary directories if they don't exist
    os.makedirs(new_file_dir, exist_ok=True)

    # Create the new file and write the content
    with open(new_file_path, 'w') as file:
        file.write(content)

    # Commit and push the changes to GitHub
    git_add_cmd = ['git', 'add', new_file_path]
    git_commit_cmd = ['git', 'commit', '-m', 'Add new file']
    git_push_cmd = ['git', 'push', 'origin', 'master']

    subprocess.run(git_add_cmd, cwd=jekyll_site_dir)
    subprocess.run(git_commit_cmd, cwd=jekyll_site_dir)
    subprocess.run(git_push_cmd, cwd=jekyll_site_dir)

    print(f"New file '{new_file_name}' has been created and added to your Jekyll site.")


def main():
    # Specify the path to your Jekyll site directory
    jekyll_site_dir = r'C:\Users\Tim_G\OneDrive\Desktop\mysite'
    # Specify the directory where the .txt files are located
    txt_files_dir = os.path.join(jekyll_site_dir, 'content')

    # Get a list of .txt files in the directory
    txt_files = get_txt_files_in_dir(txt_files_dir)

    # If there are no .txt files, print a message and exit
    if not txt_files:
        print(f"No .txt files found in directory {txt_files_dir}")
        return

    # Print a list of the .txt files
    for i, file in enumerate(txt_files, start=1):
        print(f"{i}. {file}")

    # Prompt the user to choose a file
    file_num = int(input("Enter the number of the file you want to copy:\n")) - 1

    # Get the chosen file
    chosen_file = txt_files[file_num]

    # Get the full path to the chosen file
    file_to_copy = os.path.join(txt_files_dir, chosen_file)

    # Read the content from the chosen file
    with open(file_to_copy, 'r') as file:
        content = file.read()

    create_jekyll_file(jekyll_site_dir, content)


if __name__ == '__main__':
    main()
