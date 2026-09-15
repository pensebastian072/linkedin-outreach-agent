#!/usr/bin/env python3
"""
Setup Verification Script
========================

This script checks if your Professional LinkedIn AI system is properly configured.
"""

import os
import sys
import importlib
from datetime import datetime

def print_header():
    """Print the header"""
    print("="*60)
    print("🔍 PROFESSIONAL LINKEDIN AI - SETUP CHECK")
    print("="*60)
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()

def check_python_version():
    """Check Python version"""
    print("🐍 Python Version Check:")
    version = sys.version_info
    print(f"   Version: {version.major}.{version.minor}.{version.micro}")
    
    if version.major >= 3 and version.minor >= 8:
        print("   ✅ Python version is compatible")
        return True
    else:
        print("   ❌ Python 3.8+ required")
        return False

def check_required_packages():
    """Check if required packages are installed"""
    print("\n📦 Required Package Check:")
    
    packages = [
        ('anthropic', 'Claude API client'),
        ('pandas', 'Data analysis'),
        ('python-dotenv', 'Environment management'),
        ('numpy', 'Numerical computations'),
        ('matplotlib', 'Data visualization')
    ]
    
    all_good = True
    
    for package, description in packages:
        try:
            # Handle special cases
            if package == 'python-dotenv':
                importlib.import_module('dotenv')
            else:
                importlib.import_module(package)
            print(f"   ✅ {package:<15} - {description}")
        except ImportError:
            print(f"   ❌ {package:<15} - {description} (NOT INSTALLED)")
            all_good = False
    
    return all_good

def check_configuration():
    """Check configuration files"""
    print("\n⚙️ Configuration Check:")
    
    # Check .env file
    if os.path.exists('.env'):
        print("   ✅ .env file exists")
        
        with open('.env', 'r') as f:
            content = f.read()
            
        if 'ANTHROPIC_API_KEY=' in content:
            if 'your_anthropic_api_key_here' in content:
                print("   ⚠️ API key needs to be configured")
                return False
            else:
                print("   ✅ API key appears to be configured")
                return True
        else:
            print("   ❌ ANTHROPIC_API_KEY not found in .env")
            return False
    else:
        print("   ❌ .env file missing")
        print("   💡 Run: Copy-Item .env.example .env")
        return False

def check_core_files():
    """Check core system files"""
    print("\n📁 Core Files Check:")
    
    required_files = [
        ('professional_linkedin_ai.py', 'Main AI system'),
        ('analytics_dashboard.py', 'Analytics dashboard'),
        ('launch.py', 'System launcher'),
        ('requirements.txt', 'Dependencies list')
    ]
    
    all_good = True
    
    for file, description in required_files:
        if os.path.exists(file):
            size_kb = os.path.getsize(file) / 1024
            print(f"   ✅ {file:<25} - {description} ({size_kb:.1f} KB)")
        else:
            print(f"   ❌ {file:<25} - {description} (MISSING)")
            all_good = False
    
    return all_good

def test_api_connectivity():
    """Test basic API connectivity"""
    print("\n🌐 API Connectivity Test:")
    
    try:
        from dotenv import load_dotenv
        import anthropic
        
        load_dotenv()
        api_key = os.getenv('ANTHROPIC_API_KEY')
        
        if not api_key or api_key == 'your_anthropic_api_key_here':
            print("   ⚠️ API key not configured - skipping connectivity test")
            return False
        
        # Test basic API connection (without making a real call)
        client = anthropic.Anthropic(api_key=api_key)
        print("   ✅ Claude API client initialized successfully")
        print("   💡 API key format looks valid")
        
        return True
        
    except Exception as e:
        print(f"   ❌ API test failed: {str(e)}")
        return False

def test_system_functionality():
    """Test basic system functionality"""
    print("\n🧪 System Functionality Test:")
    
    try:
        # Import and initialize
        from professional_linkedin_ai import ProfessionalLinkedInAI
        
        ai = ProfessionalLinkedInAI()
        print("   ✅ ProfessionalLinkedInAI class loaded")
        
        # Check database setup
        if hasattr(ai, '_setup_professional_databases'):
            ai._setup_professional_databases()
            print("   ✅ Database setup completed")
        
        # Test analytics
        from analytics_dashboard import ProfessionalAnalytics
        analytics = ProfessionalAnalytics()
        print("   ✅ Analytics dashboard loaded")
        
        return True
        
    except Exception as e:
        print(f"   ❌ System test failed: {str(e)}")
        return False

def provide_recommendations():
    """Provide setup recommendations"""
    print("\n🎯 RECOMMENDATIONS:")
    print("-" * 30)
    
    if not os.path.exists('.env'):
        print("1. Copy .env.example to .env:")
        print("   Copy-Item .env.example .env")
        print()
    
    with open('.env', 'r') as f:
        if 'your_anthropic_api_key_here' in f.read():
            print("2. Get Claude API key:")
            print("   • Visit: https://console.anthropic.com")
            print("   • Sign up/login with Claude Pro account")
            print("   • Create API key in 'API Keys' section")
            print("   • Replace 'your_anthropic_api_key_here' in .env")
            print()
    
    print("3. Install missing packages:")
    print("   pip install -r requirements.txt")
    print()
    
    print("4. Test the system:")
    print("   python launch.py")

def main():
    """Main verification function"""
    print_header()
    
    checks = [
        ("Python Version", check_python_version),
        ("Required Packages", check_required_packages), 
        ("Configuration", check_configuration),
        ("Core Files", check_core_files),
        ("System Functionality", test_system_functionality)
    ]
    
    results = []
    
    for check_name, check_func in checks:
        try:
            result = check_func()
            results.append((check_name, result))
        except Exception as e:
            print(f"   ❌ {check_name} check failed: {str(e)}")
            results.append((check_name, False))
    
    # Summary
    print("\n" + "="*60)
    print("📊 SETUP VERIFICATION SUMMARY")
    print("="*60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    print(f"Checks Passed: {passed}/{total}")
    print()
    
    for check_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status:<8} {check_name}")
    
    if passed == total:
        print("\n🎉 CONGRATULATIONS!")
        print("Your Professional LinkedIn AI system is ready to use!")
        print("\nNext Steps:")
        print("1. Run: python launch.py")
        print("2. Start with Option 5 (Full Professional Demo)")
        print("3. Begin generating high-quality prospects!")
    else:
        print(f"\n⚠️ Setup incomplete ({passed}/{total} checks passed)")
        provide_recommendations()
    
    print("\n" + "="*60)

if __name__ == "__main__":
    main()
