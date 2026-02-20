#!/bin/bash

# Define the target directory for original files
TARGET_DIR="raw md"

# Create the directory if it doesn't already exist
mkdir -p "$TARGET_DIR"

# Loop through all markdown files in the current folder
for file in *.md; do
    # Check if any markdown files actually exist to avoid errors
    [ -e "$file" ] || continue

    # Extract the filename without the extension
    filename="${file%.*}"

    echo "Converting: $file ..."

    # Convert MD to HTML using Pandoc
    pandoc "$file" -o "${filename}.html"

    # Move the original markdown file to the "raw md" folder
    mv "$file" "$TARGET_DIR/"
done

echo "Done! Your HTML files are ready and originals are tucked away in '$TARGET_DIR'."