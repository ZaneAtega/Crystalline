import os

# Get the current folder
current_folder = os.getcwd()

# Iterate through all files in the current folder
for filename in os.listdir(current_folder):
    # Only process .webp files
    if filename.endswith('.webp'):
        # Split the filename by spaces
        parts = filename.split(' ')

        # Split the first part by underscores and get the last part (the number)
        number_part = parts[0]
        number = number_part.split('_')[-1]  # Get the last part after the underscore

        # Remove the first digit of the number
        new_number = number[1:]

        # Construct the new filename
        new_filename = f"{new_number}.webp"

        # Rename the file
        old_path = os.path.join(current_folder, filename)
        new_path = os.path.join(current_folder, new_filename)
        os.rename(old_path, new_path)

        print(f"Renamed: {filename} -> {new_filename}")

print("Renaming complete.")
