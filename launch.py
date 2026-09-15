#!/usr/bin/env python3
"""
Professional LinkedIn AI System Launcher
========================================

This script provides an easy way to launch and interact with your Professional LinkedIn AI system.
"""

import os
import sys
from datetime import datetime

def check_setup():
    """Check if the system is properly set up"""
    print("🔍 Checking system setup...")
    
    # Check if .env file exists
    if not os.path.exists('.env'):
        print("❌ .env file not found!")
        print("Please copy .env.example to .env and configure your API keys.")
        return False
    
    # Check if API key is configured
    with open('.env', 'r') as f:
        env_content = f.read()
        if 'your_anthropic_api_key_here' in env_content:
            print("❌ API key not configured!")
            print("Please edit .env and add your Claude API key.")
            return False
    
    print("✅ System setup looks good!")
    return True

def show_menu():
    """Display the main menu"""
    print("\n" + "="*60)
    print("🚀 PROFESSIONAL LINKEDIN AI SYSTEM")
    print("="*60)
    print("1. Run Prospect Research Demo")
    print("2. Generate Executive Message Demo") 
    print("3. Create Industry Campaign Demo")
    print("4. View Analytics Dashboard")
    print("5. Run Full Professional Demo")
    print("6. Check System Status")
    print("0. Exit")
    print("="*60)

def run_prospect_research():
    """Run prospect research demo"""
    print("\n🔬 RUNNING PROSPECT RESEARCH DEMO...")
    print("-" * 40)
    
    try:
        from professional_linkedin_ai import ProfessionalLinkedInAI
        
        ai = ProfessionalLinkedInAI()
        research = ai.advanced_prospect_research(
            name="Sarah Johnson",
            company="TechCorp Industries",
            title="Chief Technology Officer", 
            industry="Manufacturing Technology"
        )
        
        if 'error' in research:
            print(f"❌ Error: {research['error']}")
        else:
            print("✅ Research completed successfully!")
            print(f"Prospect: {research['prospect_name']}")
            print(f"Company: {research['company']}")
            print(f"Confidence Score: {research['confidence_score']:.2f}")
            print(f"Opportunity Size: {research['opportunity_size']}")
            print("\nDetailed Analysis:")
            print("-" * 20)
            print(research['detailed_analysis'][:500] + "...")
            
    except Exception as e:
        print(f"❌ Error running prospect research: {str(e)}")

def run_message_generation():
    """Run message generation demo"""
    print("\n📝 RUNNING MESSAGE GENERATION DEMO...")
    print("-" * 40)
    
    try:
        from professional_linkedin_ai import ProfessionalLinkedInAI
        
        ai = ProfessionalLinkedInAI()
        
        # Create sample prospect data
        prospect_data = {
            'prospect_name': 'Sarah Johnson',
            'company': 'TechCorp Industries',
            'title': 'Chief Technology Officer',
            'detailed_analysis': 'Executive with 15+ years experience in manufacturing technology transformation...'
        }
        
        message = ai.generate_executive_message(prospect_data, "introduction")
        
        print("✅ Executive message generated!")
        print("\nGenerated Message:")
        print("-" * 20)
        print(message)
        
    except Exception as e:
        print(f"❌ Error generating message: {str(e)}")

def run_campaign_creation():
    """Run campaign creation demo"""
    print("\n🎯 RUNNING CAMPAIGN CREATION DEMO...")
    print("-" * 40)
    
    try:
        from professional_linkedin_ai import ProfessionalLinkedInAI
        
        ai = ProfessionalLinkedInAI()
        campaign = ai.create_industry_campaign(
            industry="Financial Services",
            target_titles=["CTO", "Chief Digital Officer", "VP Technology"],
            company_size="500-2000 employees"
        )
        
        if 'error' in campaign:
            print(f"❌ Error: {campaign['error']}")
        else:
            print("✅ Campaign created successfully!")
            print(f"Campaign ID: {campaign['id']}")
            print(f"Name: {campaign['name']}")
            print(f"Industry: {campaign['industry']}")
            print(f"Target Titles: {', '.join(campaign['target_titles'])}")
            print("\nCampaign Strategy:")
            print("-" * 20)
            print(campaign['strategy'][:500] + "...")
            
    except Exception as e:
        print(f"❌ Error creating campaign: {str(e)}")

def run_analytics():
    """Run analytics dashboard"""
    print("\n📊 RUNNING ANALYTICS DASHBOARD...")
    print("-" * 40)
    
    try:
        from analytics_dashboard import ProfessionalAnalytics
        
        analytics = ProfessionalAnalytics()
        report = analytics.generate_executive_report()
        print(report)
        
        # ROI Analysis
        roi_data = analytics.track_roi(30)
        if 'error' not in roi_data:
            print("\n💰 ROI ANALYSIS (Last 30 Days):")
            print("=" * 35)
            print(f"Total Investment: ${roi_data['total_investment']:,.2f}")
            print(f"Pipeline Created: ${roi_data['pipeline_created']:,}")
            print(f"ROI Ratio: {roi_data['roi_ratio']:.1f}x")
        
    except Exception as e:
        print(f"❌ Error running analytics: {str(e)}")

def run_full_demo():
    """Run the full professional demo"""
    print("\n🚀 RUNNING FULL PROFESSIONAL DEMO...")
    print("=" * 50)
    
    try:
        from professional_linkedin_ai import professional_demo
        professional_demo()
    except Exception as e:
        print(f"❌ Error running full demo: {str(e)}")

def check_status():
    """Check system status"""
    print("\n🔍 SYSTEM STATUS CHECK...")
    print("-" * 30)
    
    # Check files
    required_files = [
        'professional_linkedin_ai.py',
        'analytics_dashboard.py',
        'requirements.txt',
        '.env'
    ]
    
    for file in required_files:
        if os.path.exists(file):
            print(f"✅ {file}")
        else:
            print(f"❌ {file} (missing)")
    
    # Check databases
    database_files = [
        'professional_prospects.csv',
        'research_reports.json',
        'professional_campaigns.json',
        'campaign_analytics.json'
    ]
    
    print("\nDatabase Files:")
    for file in database_files:
        if os.path.exists(file):
            size = os.path.getsize(file)
            print(f"✅ {file} ({size} bytes)")
        else:
            print(f"⏳ {file} (will be created on first use)")
    
    # Check API connectivity
    print(f"\nLast Status Check: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

def main():
    """Main application loop"""
    print("🎯 Professional LinkedIn AI System")
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Check setup
    if not check_setup():
        return
    
    while True:
        try:
            show_menu()
            choice = input("\nSelect an option (0-6): ").strip()
            
            if choice == '0':
                print("👋 Goodbye! Happy networking!")
                break
            elif choice == '1':
                run_prospect_research()
            elif choice == '2':
                run_message_generation()
            elif choice == '3':
                run_campaign_creation()
            elif choice == '4':
                run_analytics()
            elif choice == '5':
                run_full_demo()
            elif choice == '6':
                check_status()
            else:
                print("❌ Invalid option. Please choose 0-6.")
                
            input("\nPress Enter to continue...")
            
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Unexpected error: {str(e)}")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()
