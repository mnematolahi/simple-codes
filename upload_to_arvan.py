import os

# Define your ArvanCloud credentials
arvan_username = "your_arvan_username"
arvan_password = "your_arvan_password"

# Define the URL of the file to be downloaded
file_url = "https://fsdfsdfsdfsdfsdf.com"

# Define the local file path where the downloaded file will be saved
local_file_path = "file_to_upload.zip"

# Download the file from the given URL
os.system(f"curl -L -o {local_file_path} {file_url}")

# Upload the file to your ArvanCloud storage using the Arvan CLI tool
os.system(f"arvan storage upload --path /remote/path/ --local-path {local_file_path} --username {arvan_username} --password {arvan_password}")

# Remove the local file after uploading
os.remove(local_file_path)

print("File uploaded successfully!")
