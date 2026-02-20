# 1. Create the destination folder if it doesn't exist
$targetDir = "raw md"
if (!(Test-Path $targetDir)) {
    New-Item -ItemType Directory -Path $targetDir
}

# 2. Get all markdown files in the current directory
$mdFiles = Get-ChildItem -Filter *.md

foreach ($file in $mdFiles) {
    # Define the output name (same name, .html extension)
    $outputFile = "$($file.BaseName).html"
    
    Write-Host "Converting: $($file.Name) ..."
    
    # 3. Run Pandoc
    # -s makes it a standalone HTML file with a header/footer
    pandoc "$($file.FullName)" -o "$outputFile"
    
    # 4. Move the original markdown file
    Move-Item -Path "$($file.FullName)" -Destination "$targetDir"
}

Write-Host "Success! Files moved to '$targetDir'." -ForegroundColor Green