# ============================================================
# build.ps1 - Builds Linux-compatible deployment ZIP
# Run from project root: .\build.ps1
# ============================================================

Write-Host ""
Write-Host "================================================" -ForegroundColor Cyan
Write-Host "   Serverless Image Pipeline - Build Script    " -ForegroundColor Cyan
Write-Host "================================================" -ForegroundColor Cyan
Write-Host ""

# Step 1: Clean old build
Write-Host "[STEP 1] Cleaning old build files..." -ForegroundColor Yellow
if (Test-Path "build") { Remove-Item -Recurse -Force "build" }
New-Item -ItemType Directory -Path "build" | Out-Null
Write-Host "[STEP 1] Done!" -ForegroundColor Green

# Step 2: Clear pip cache
Write-Host "[STEP 2] Clearing pip cache..." -ForegroundColor Yellow
pip cache purge
Write-Host "[STEP 2] Done!" -ForegroundColor Green

# Step 3: Install Linux-compatible Pillow
Write-Host "[STEP 3] Downloading Linux-compatible Pillow..." -ForegroundColor Yellow
pip install Pillow==10.4.0 `
    --only-binary=:all: `
    --platform manylinux2014_x86_64 `
    --python-version 3.12 `
    --no-deps `
    --no-cache-dir `
    -t ./build
Write-Host "[STEP 3] Done!" -ForegroundColor Green

# Step 4: Clean unnecessary files
Write-Host "[STEP 4] Cleaning unnecessary files..." -ForegroundColor Yellow
Get-ChildItem -Path "build" -Directory -Filter "*.dist-info" | Remove-Item -Recurse -Force
if (Test-Path "build/Pillow.libs") { Remove-Item -Recurse -Force "build/Pillow.libs" }
Write-Host "[STEP 4] Done!" -ForegroundColor Green

# Step 5: Copy Lambda function
Write-Host "[STEP 5] Copying Lambda function..." -ForegroundColor Yellow
Copy-Item "src/lambda_function.py" "build/lambda_function.py"
Write-Host "[STEP 5] Done!" -ForegroundColor Green

# Step 6: Create ZIP
Write-Host "[STEP 6] Creating deployment ZIP..." -ForegroundColor Yellow
if (Test-Path "deployment.zip") { Remove-Item "deployment.zip" }
Compress-Archive -Path build/* -DestinationPath deployment.zip
Write-Host "[STEP 6] Done!" -ForegroundColor Green

Write-Host ""
Write-Host "================================================" -ForegroundColor Cyan
Write-Host " BUILD SUCCESSFUL!" -ForegroundColor Green
Write-Host " Upload deployment.zip to AWS Lambda!" -ForegroundColor Green
Write-Host "================================================" -ForegroundColor Cyan
Write-Host ""
