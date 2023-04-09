import subprocess
import difflib

# Read the content of the old requirements.txt file
with open("requirements.txt", "r") as f:
    old_requirements = f.readlines()

# Loop through each package and get the latest version from PyPI
updated_requirements = []
for req in old_requirements:
    package_name = req.split("==")[0]
    curr_version = req.strip().split("==")[1]
    out = subprocess.run(["pip", "install", f"{package_name}=="], capture_output=True, text=True)
    latest_version = out.stdout.strip().split("Collecting ")[1].split(" (from")[0]
    if curr_version != latest_version:
        # If the installed version doesn't match the latest version, update it
        updated_requirements.append(f"{package_name}=={latest_version}\n")
    else:
        updated_requirements.append(req)

# Write the updated requirements to a new requirements.txt file
with open("requirements_updated.txt", "w") as f:
    f.writelines(updated_requirements)

# Find the differences between the old and updated requirements files
with open("requirements.txt", "r") as f1, open("requirements_updated.txt", "r") as f2:
    differ = difflib.HtmlDiff()
    diff = differ.make_file(f1.readlines(), f2.readlines())

# Print the differences in HTML format
with open("diff.html", "w") as f:
    f.write(diff)
