import os
import zipfile

# Function to unzip all files in the current directory
def unzip_files_in_directory(password):
    # Get the directory where the script is located
    script_directory = os.path.dirname(os.path.realpath(__file__))
    
    # List all files in the directory
    files = os.listdir(script_directory)
    
    # Filter for zip files
    zip_files = [file for file in files if file.endswith('.zip')]
    
    # Process each zip file
    for zip_file in zip_files:
        try:
            # Construct the full path to the zip file
            zip_file_path = os.path.join(script_directory, zip_file)
            
            # Open the zip file
            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                # Extract all the contents into the same directory
                zip_ref.extractall(script_directory, pwd=bytes(password, 'utf-8'))
                print(f"Extracted {zip_file} successfully.")
                
        except zipfile.BadZipFile:
            print(f"{zip_file} is not a zip file or is corrupted.")
        except RuntimeError as e:
            # Handle incorrect password
            if 'Bad password for file' in str(e):
                print(f"Incorrect password for {zip_file}.")
            else:
                raise

# Add this line where you want to unzip files in your script, for example, at the end
unzip_files_in_directory('PASSWORD')
