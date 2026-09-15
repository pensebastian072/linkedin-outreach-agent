# Professional LinkedIn AI Setup Script
# =====================================

Write-Host "🚀 Setting up Professional LinkedIn AI System..." -ForegroundColor Green
Write-Host "=================================================" -ForegroundColor Green

# Check if Python is installed
Write-Host "`n🔍 Checking Python installation..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✅ $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Python not found! Please install Python 3.8+ first." -ForegroundColor Red
    Write-Host "Download from: https://www.python.org/downloads/" -ForegroundColor Yellow
    exit 1
}

# Check if pip is available
Write-Host "`n🔍 Checking pip installation..." -ForegroundColor Yellow
try {
    $pipVersion = pip --version 2>&1
    Write-Host "✅ $pipVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ pip not found!" -ForegroundColor Red
    exit 1
}

# Install Python packages
Write-Host "`n📦 Installing Python packages..." -ForegroundColor Yellow
Write-Host "This may take a few minutes..." -ForegroundColor Gray

try {
    pip install -r requirements.txt
    Write-Host "✅ All packages installed successfully!" -ForegroundColor Green
} catch {
    Write-Host "❌ Error installing packages. Please run manually:" -ForegroundColor Red
    Write-Host "pip install -r requirements.txt" -ForegroundColor Yellow
}

# Create .env file if it doesn't exist
Write-Host "`n⚙️ Setting up configuration..." -ForegroundColor Yellow

if (Test-Path ".env") {
    Write-Host "✅ .env file already exists" -ForegroundColor Green
} else {
    Copy-Item ".env.example" ".env"
    Write-Host "✅ Created .env file from template" -ForegroundColor Green
    Write-Host "⚠️ IMPORTANT: Edit .env file with your Claude API key!" -ForegroundColor Red
}

# Create directories
Write-Host "`n📁 Setting up directories..." -ForegroundColor Yellow
$directories = @("data", "exports", "backups")
foreach ($dir in $directories) {
    if (!(Test-Path $dir)) {
        New-Item -ItemType Directory -Path $dir -Force | Out-Null
        Write-Host "✅ Created $dir directory" -ForegroundColor Green
    }
}

Write-Host "`n🎯 Setup Complete!" -ForegroundColor Green
Write-Host "==================" -ForegroundColor Green

Write-Host "`nNext Steps:" -ForegroundColor Yellow
Write-Host "1. Get your Claude API key from https://console.anthropic.com" -ForegroundColor White
Write-Host "2. Edit the .env file and add your API key" -ForegroundColor White
Write-Host "3. Run: python launch.py" -ForegroundColor White

Write-Host "`n📊 Expected Monthly Costs:" -ForegroundColor Cyan
Write-Host "• Claude Haiku: $15-25 (200-500 prospects)" -ForegroundColor White
Write-Host "• Claude Sonnet: $25-40 (100-200 prospects, premium quality)" -ForegroundColor White

Write-Host "`n🎯 Expected Results (Month 1):" -ForegroundColor Cyan
Write-Host "• 200+ high-quality prospect profiles" -ForegroundColor White
Write-Host "• 100+ personalized executive messages" -ForegroundColor White
Write-Host "• 15-25 qualified prospect conversations" -ForegroundColor White
Write-Host "• $500K-1M potential consulting pipeline" -ForegroundColor White

Write-Host "`nReady to launch? Run:" -ForegroundColor Green
Write-Host "python launch.py" -ForegroundColor Yellow

# Pause to let user read the information
Write-Host "`nPress any key to continue..." -ForegroundColor Gray
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
