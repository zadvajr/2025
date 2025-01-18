# Delete Folder
# To delete an entire folder, use the os.rmdir() method:

# Example
# Remove the folder "temp_folder_to_delete":
#Since we can only delete an empty folder, we need to delete the content first.
import os
os.remove("temp_folder_to_delete/empty_text_file.txt")
os.rmdir("temp_folder_to_delete")
