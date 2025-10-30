import os

# Get the current directory
directory = os.getcwd()

# Loop through all files and subdirectories in the current directory
for root, dirs, files in os.walk(directory):
    for file in files:
        # Check if the file has no extension
        if '.' not in file:
            # Create the new file name by adding .webp extension
            old_path = os.path.join(root, file)
            new_path = os.path.join(root, file + '.webp')
            
            # Rename the file
            os.rename(old_path, new_path)
            print(f"Renamed {old_path} to {new_path}")
