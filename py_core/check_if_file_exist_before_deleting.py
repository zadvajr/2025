#Check if file exist before deleting
# To avoid getting an error, you might want to check if the file exists before you try to delete it:

# Example
# Check if file exists, then delete it:
import os

if os.path.exists('demofile2.txt'):
    os.remove('demofile2.txt')
else:
    print(f"File does not exist")
