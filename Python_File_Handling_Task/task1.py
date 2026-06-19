import os
import shutil

try:
    # Read data from input file
    with open("input.txt", "r") as file:
        data = file.read()

    print("File Content:")
    print(data)

    # Write data to output file
    with open("output.txt", "w") as file:
        file.write(data.upper())

    print("Data written to output.txt")

    # Rename output file
    os.rename("output.txt", "renamed_output.txt")
    print("File renamed successfully")

    # Move file to Backup folder
    shutil.move("renamed_output.txt", "Backup/renamed_output.txt")
    print("File moved to Backup folder")

except FileNotFoundError:
    print("Error: File not found")

except Exception as e:
    print("An error occurred:", e)