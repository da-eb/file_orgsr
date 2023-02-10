import os
import shutil

def organise_files(src_dir, dst_dir):
    # Get all files in the source directory
    files = os.listdir(src_dir)

    # Create a dictionary to map file extensions to destination directories
    file_types = {
        '.txt': 'text_files',
        '.jpg': 'image_files',
        '.mp3': 'audio_files',
        '.pdf': 'pdf_files',
        '.docx': 'word_files'
    }

    # Loop through each file in the source directory
    for file in files:
        # Get the file extension
        file_extension = os.path.splitext(file)[1].lower()

        # Check if the file extension is in the file_types dictionary
        if file_extension in file_types:
            # Get the destination directory for the file type
            dst_subdir = os.path.join(dst_dir, file_types[file_extension])

            # If the destination directory does not exist, create it
            if not os.path.exists(dst_subdir):
                os.makedirs(dst_subdir)

            # Move the file to the destination directory
            src_file = os.path.join(src_dir, file)
            dst_file = os.path.join(dst_subdir, file)
            shutil.move(src_file, dst_file)

# Example usage
src_dir = '/path/to/source/directory'
dst_dir = '/path/to/destination/directory'
organise_files(src_dir, dst_dir)
