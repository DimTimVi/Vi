import os
import subprocess

def git_add_commit_push(commit_message, branch):
    try:
        # Change to the directory of your repository
        os.chdir('C:/Users/Tim_G/OneDrive/Desktop/mysite/')
        
        # Add all changes
        add_command = ['git', 'add', '.']
        subprocess.run(add_command, check=True)
        
        # Commit changes with the provided message
        commit_command = ['git', 'commit', '-m', commit_message]
        subprocess.run(commit_command, check=True)
        
        # Push changes to the specified branch
        push_command = ['git', 'push', 'origin', branch]
        subprocess.run(push_command, check=True)
        
        print('Add, commit, and push successful.')
        
    except subprocess.CalledProcessError as e:
        print('An error occurred while adding, committing, and pushing.')
        print('Error output:', e.stderr)

# Use the function with your commit message and branch name
git_add_commit_push('Your commit message', 'master')
