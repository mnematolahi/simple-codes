#!/bin/bash

# Set the username, token, and repository URLs
USERNAME=mnematolahi
TOKEN=dfgdfgdfgfd
EXTERNAL_REPO_URL=https://github.com/external/repo.git

# Extract the name of the external repository
EXTERNAL_REPO_NAME=$(basename $EXTERNAL_REPO_URL .git)

# Set the URL for the new repository
YOUR_REPO_URL=https://github.com/$USERNAME/$EXTERNAL_REPO_NAME.git

echo "Creating new repository..."
# Create the new repository with authentication
curl -u $USERNAME:$TOKEN https://api.github.com/user/repos -d '{"name":"'$EXTERNAL_REPO_NAME'"}'

echo "Cloning external repository..."
# Clone the external repository to a temporary directory
TEMP_DIR=$(mktemp -d)
git clone $EXTERNAL_REPO_URL $TEMP_DIR

echo "Creating copy branch..."
# Navigate to the external repository and create a new branch
cd $TEMP_DIR
git checkout -b copy

echo "Removing external origin..."
# Remove the Git remote to the external repository
git remote remove origin

echo "Copying contents to your own repository..."
# Add the contents of the external repository to your own repository
cd ..
git clone $YOUR_REPO_URL
cd $EXTERNAL_REPO_NAME
cp -R $TEMP_DIR/* .

echo "Committing changes..."
# Commit the changes
git add .
git commit -m "Copy contents of external repository"
git branch -M copy

echo "Pushing changes..."
# Push the changes with authentication
git push --set-upstream https://$USERNAME:$TOKEN@github.com/$USERNAME/$EXTERNAL_REPO_NAME.git copy

# Clean up the temporary directory
rm -rf $TEMP_DIR
