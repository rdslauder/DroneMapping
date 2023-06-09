import os

#Rename images with user inputting the batch number for a prefix, insert "#" between batch number and image number

def batchRename():

    # Get script directory
    script_directory = os.path.dirname(os.path.realpath(__file__))

    # Set the path to the directory containing the files to be renamed
    folder_path = os.path.join(script_directory)

    # Prompt the user to input a prefix
    prefix = input("Enter the batch number: ")

    # Set the starting index
    start_index = 1

    # Loop through each file in the directory
    for i, filename in enumerate(os.listdir(folder_path)):
        # Check if the file is an image
        if os.path.splitext(filename)[1].lower() in ['.jpg', '.jpeg', '.png', '.bmp', '.gif']:
            # Set the new filename
            new_filename = prefix + '#' + str(start_index) + '.jpg'

            # Set the paths to the source and destination files
            source_path = os.path.join(folder_path, filename)
            destination_path = os.path.join(folder_path, new_filename)

            # Rename the file
            os.rename(source_path, destination_path)

            # Increment the index
            start_index += 1
