import os
import pyperclip
import subprocess


def get_txt_files_in_dir(directory):
    # List all files in the directory
    files_in_dir = os.listdir(directory)

    # Filter for .txt files
    txt_files = [file for file in files_in_dir if file.endswith('.txt')]

    return txt_files


def create_jekyll_file(jekyll_site_dir, content, file_name):
    # Define the new file path and name
    new_file_dir = os.path.join(jekyll_site_dir, 'content')
    new_file_path = os.path.join(new_file_dir, file_name)

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

    print(f"New file '{file_name}' has been created and added to your Jekyll site.")


def main():
    # Specify the path to your Jekyll site directory
    jekyll_site_dir = r'C:\Users\Tim_G\OneDrive\Desktop\mysite'
    # Specify the directory where the .txt files are located
    txt_files_dir = r'C:\Users\Tim_G\OneDrive\Documents\text_files'

    # Get a list of .txt files in the directory
    txt_files = get_txt_files_in_dir(txt_files_dir)

    # If there are no .txt files, print a message and exit
    if not txt_files:
        print(f"No .txt files found in directory {txt_files_dir}")
        return

    # Print a list of the .txt files
    for i, file in enumerate(txt_files, start=1):
        print(f"{i}. {file}")

    # Prompt the user to choose a file or select all
    file_num = input("Enter the number of the file you want to copy (or 'all' to process all files): ")

    if file_num == 'all':
        # Process all files
        for chosen_file in txt_files:
            # Get the full path to the chosen file
            file_to_copy = os.path.join(txt_files_dir, chosen_file)

            # Read the content from the chosen file
            with open(file_to_copy, 'r') as file:
                content = file.read()

            # Use the file name of the .txt document as the file name for the resulting file
            file_name = os.path.splitext(chosen_file)[0] + '.md'

            create_jekyll_file(jekyll_site_dir, content, file_name)
    else:
        # Get the chosen file
        file_num = int(file_num) - 1

        # Verify the chosen file number
        if 0 <= file_num < len(txt_files):
            chosen_file = txt_files[file_num]

            # Get the full path to the chosen file
            file_to_copy = os.path.join(txt_files_dir, chosen_file)

            # Read the content from
