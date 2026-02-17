# pyai Build Script
# ====================
# PowerShell script for building and packaging PyAI
# For Windows / Microsoft environments

param(
    [Parameter()]
    [ValidateSet("build", "install", "test", "clean", "docs", "publish", "zip", "all")]
    [string]$Command = "all"
)

$ErrorActionPreference = "Stop"
$ProjectRoot = $PSScriptRoot
$DistDir = Join-Path $ProjectRoot "dist"
$BuildDir = Join-Path $ProjectRoot "build"

function Write-Header {
    param([string]$Message)
    Write-Host "`n========================================" -ForegroundColor Cyan
    Write-Host "  $Message" -ForegroundColor Cyan
    Write-Host "========================================`n" -ForegroundColor Cyan
}

function Clean-Build {
    Write-Header "Cleaning Build Artifacts"
    
    $dirsToRemove = @("dist", "build", "*.egg-info", "__pycache__")
    
    foreach ($dir in $dirsToRemove) {
        $paths = Get-ChildItem -Path $ProjectRoot -Recurse -Directory -Filter $dir -ErrorAction SilentlyContinue
        foreach ($path in $paths) {
            Write-Host "Removing: $($path.FullName)"
            Remove-Item -Path $path.FullName -Recurse -Force
        }
    }
    
    # Remove .pyc files
    Get-ChildItem -Path $ProjectRoot -Recurse -Filter "*.pyc" | Remove-Item -Force
    
    Write-Host "Clean complete!" -ForegroundColor Green
}

function Build-Package {
    Write-Header "Building PyAI Package"
    
    # Ensure build tools are available
    Write-Host "Installing build tools..."
    python -m pip install --upgrade pip build wheel hatchling --quiet
    
    # Build the package
    Write-Host "Building distribution packages..."
    python -m build
    
    Write-Host "Build complete!" -ForegroundColor Green
    Write-Host "Packages created in: $DistDir"
    Get-ChildItem -Path $DistDir
}

function Install-Package {
    Write-Header "Installing PyAI Locally"
    
    # Install in development mode with all dependencies
    python -m pip install -e ".[all,dev]"
    
    Write-Host "Installation complete!" -ForegroundColor Green
}

function Run-Tests {
    Write-Header "Running Tests"
    
    # Run pytest
    python -m pytest tests/ -v --cov=PyAI --cov-report=term-missing
    
    Write-Host "Tests complete!" -ForegroundColor Green
}

function Build-Docs {
    Write-Header "Building Documentation"
    
    # Create docs output directory
    $DocsOutput = Join-Path $ProjectRoot "docs\_build"
    New-Item -ItemType Directory -Path $DocsOutput -Force | Out-Null
    
    # Copy all markdown files
    $DocsFiles = Get-ChildItem -Path (Join-Path $ProjectRoot "docs") -Filter "*.md"
    foreach ($file in $DocsFiles) {
        Copy-Item -Path $file.FullName -Destination $DocsOutput
    }
    
    # Copy README files from modules
    $ModuleReadmes = Get-ChildItem -Path (Join-Path $ProjectRoot "pyai") -Recurse -Filter "README.md"
    foreach ($file in $ModuleReadmes) {
        $relativePath = $file.Directory.Name
        Copy-Item -Path $file.FullName -Destination (Join-Path $DocsOutput "$relativePath-README.md")
    }
    
    Write-Host "Documentation built in: $DocsOutput" -ForegroundColor Green
}

function Create-ZipDistribution {
    Write-Header "Creating ZIP Distribution"
    
    $ZipDir = Join-Path $DistDir "PyAI-release"
    New-Item -ItemType Directory -Path $ZipDir -Force | Out-Null
    
    # Copy source files
    $ItemsToCopy = @(
        "pyai",
        "examples",
        "docs",
        "README.md",
        "LICENSE",
        "pyproject.toml",
        "setup.py",
        "MANIFEST.in"
    )
    
    foreach ($item in $ItemsToCopy) {
        $sourcePath = Join-Path $ProjectRoot $item
        if (Test-Path $sourcePath) {
            $destPath = Join-Path $ZipDir $item
            if (Test-Path $sourcePath -PathType Container) {
                Copy-Item -Path $sourcePath -Destination $destPath -Recurse
            } else {
                Copy-Item -Path $sourcePath -Destination $destPath
            }
        }
    }
    
    # Remove __pycache__ from copied files
    Get-ChildItem -Path $ZipDir -Recurse -Directory -Filter "__pycache__" | Remove-Item -Recurse -Force
    
    # Create the zip file
    $version = (python -c "import pyai; print(pyai.__version__)" 2>$null) -or "0.2.0"
    $ZipFile = Join-Path $DistDir "PyAI-$version-release.zip"
    
    Compress-Archive -Path "$ZipDir\*" -DestinationPath $ZipFile -Force
    
    # Clean up temporary directory
    Remove-Item -Path $ZipDir -Recurse -Force
    
    Write-Host "ZIP distribution created: $ZipFile" -ForegroundColor Green
}

function Publish-Package {
    Write-Header "Publishing to PyPI"
    
    Write-Host "WARNING: This will publish to PyPI!" -ForegroundColor Yellow
    $confirm = Read-Host "Are you sure? (yes/no)"
    
    if ($confirm -eq "yes") {
        python -m pip install --upgrade twine --quiet
        python -m twine upload dist/*
        Write-Host "Published to PyPI!" -ForegroundColor Green
    } else {
        Write-Host "Publication cancelled." -ForegroundColor Yellow
    }
}

# Main execution
switch ($Command) {
    "clean" { Clean-Build }
    "build" { Build-Package }
    "install" { Install-Package }
    "test" { Run-Tests }
    "docs" { Build-Docs }
    "zip" { Create-ZipDistribution }
    "publish" { Publish-Package }
    "all" {
        Clean-Build
        Build-Package
        Create-ZipDistribution
        Write-Header "All Tasks Complete!"
        Write-Host "Distribution packages available in: $DistDir" -ForegroundColor Green
    }
}
