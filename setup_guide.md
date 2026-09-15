# Professional LinkedIn AI Setup Guide

## 🚀 Quick Start Instructions

### Step 1: Get Your Claude API Key

1. **Go to [console.anthropic.com](https://console.anthropic.com)**
2. **Sign up with your existing Claude Pro account**
3. **Navigate to "API Keys" section**
4. **Create a new API key**
5. **Copy the key - you'll need it in Step 3**

### Step 2: Install Dependencies

Open PowerShell and run:

```powershell
# Navigate to project directory
cd "C:\Users\<your-user>\OneDrive\Documents\GitHub\linked-in-ai-agent"

# Install Python packages
pip install -r requirements.txt
```

### Step 3: Configure Your Environment

1. **Copy the example environment file:**
```powershell
Copy-Item .env.example .env
```

2. **Edit the `.env` file with your information:**
   - Open `.env` in VS Code or any text editor
   - Replace `your_anthropic_api_key_here` with your actual Claude API key
   - Update your business information (company name, expertise, etc.)

### Step 4: Run Your Professional System

```powershell
# Run the main system
python professional_linkedin_ai.py

# Run analytics dashboard
python analytics_dashboard.py
```

## ✅ Verification

If everything is set up correctly, you should see:
- ✅ Professional LinkedIn AI System Ready!
- ✅ Advanced prospect research capabilities
- ✅ Executive-level message generation
- ✅ Industry campaign strategy creation

## 🎯 Expected Results

### Month 1:
- **Research**: 200+ high-quality prospect profiles
- **Outreach**: 100+ personalized executive messages
- **Meetings**: 15-25 qualified prospect conversations
- **Pipeline**: $500K-1M in potential consulting opportunities

### Cost Estimates:
- **Claude Haiku**: $15-25/month for 200-500 prospects
- **Claude Sonnet**: $25-40/month for 100-200 prospects (premium quality)

## 🔧 Troubleshooting

**API Key Issues:**
- Ensure your Claude API key is correctly set in `.env`
- Check that you have billing enabled on your Anthropic account

**Import Errors:**
- Run `pip install -r requirements.txt` again
- Make sure you're using Python 3.8 or higher

**File Not Found:**
- Ensure you're running commands from the project directory
- Check that all files were created properly

## 📊 Using the System

### Research a Prospect:
```python
from professional_linkedin_ai import ProfessionalLinkedInAI

ai = ProfessionalLinkedInAI()
research = ai.advanced_prospect_research(
    name="John Smith",
    company="Tech Corp",
    title="CTO",
    industry="Manufacturing"
)
```

### Generate Executive Message:
```python
message = ai.generate_executive_message(research, "introduction")
print(message)
```

### Create Industry Campaign:
```python
campaign = ai.create_industry_campaign(
    industry="Healthcare",
    target_titles=["CTO", "VP Technology", "Chief Digital Officer"]
)
```

## 🎯 Ready to Launch!

Your professional LinkedIn AI system is now configured and ready to help you:
- Generate high-quality prospect research
- Create personalized executive messages
- Build systematic outreach campaigns
- Track performance and optimize results

Start with a small test campaign to verify everything works, then scale up your outreach activities!
