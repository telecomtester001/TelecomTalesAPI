import subprocess
import os

# Navigate to the parent directory where run.py is located
parent_dir = os.path.join(os.path.dirname(__file__), '..', '..')
os.chdir(parent_dir)

# Set the FLASK_APP environment variable
os.environ['FLASK_APP'] = 'run.py'

# List of commands to execute
commands = [
    'flask db init',
    'flask db migrate -m "Initial migration."',
    'flask db upgrade'
]

# Execute each command
for command in commands:
    process = subprocess.Popen(command, shell=True)
    process.wait()
    if process.returncode != 0:
        print(f"Command '{command}' failed with exit code {process.returncode}")
        break
else:
    print("Database initialization complete.")