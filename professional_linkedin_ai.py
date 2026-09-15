import os
import anthropic
from datetime import datetime, timedelta
import json
import pandas as pd
from typing import List, Dict, Any, Optional
import time
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class ProfessionalLinkedInAI:
    """Professional LinkedIn AI system optimized for Claude"""
    
    def __init__(self):
        self.client = anthropic.Anthropic(
            api_key=os.getenv('ANTHROPIC_API_KEY')
        )
        self.model = os.getenv('CLAUDE_MODEL', 'claude-3-haiku-20240307')
        self.max_tokens = int(os.getenv('CLAUDE_MAX_TOKENS', '4000'))
        self.temperature = float(os.getenv('CLAUDE_TEMPERATURE', '0.7'))
        
        # Professional settings
        self.company_name = os.getenv('COMPANY_NAME', 'Your Consulting Firm')
        self.your_name = os.getenv('YOUR_NAME', 'Your Name')
        self.expertise = os.getenv('YOUR_EXPERTISE', 'business transformation')
        
        # Initialize databases
        self._setup_professional_databases()
    
    def _setup_professional_databases(self):
        """Set up professional-grade data management"""
        self.prospects_db = "professional_prospects.csv"
        self.research_db = "research_reports.json"
        self.campaigns_db = "professional_campaigns.json"
        self.analytics_db = "campaign_analytics.json"
        
        # Create databases if they don't exist
        self._ensure_databases_exist()
    
    def advanced_prospect_research(self, name: str, company: str, title: str, 
                                 industry: str = "") -> Dict[str, Any]:
        """Professional-grade prospect research using Claude"""
        
        prompt = f"""
        As a senior business development researcher for a management consulting firm, conduct comprehensive research on this LinkedIn prospect:

        Prospect Details:
        - Name: {name}
        - Title: {title} 
        - Company: {company}
        - Industry: {industry}

        Provide a structured analysis covering:

        1. EXECUTIVE SUMMARY
        - Key findings about this prospect's potential fit
        - Recommended outreach approach and timing
        - Estimated opportunity size and likelihood

        2. PROFESSIONAL BACKGROUND
        - Career trajectory and key achievements
        - Areas of expertise and responsibility
        - Decision-making authority and influence

        3. COMPANY INTELLIGENCE
        - Business model and revenue streams
        - Recent developments, challenges, and opportunities
        - Market position and competitive landscape
        - Technology stack and digital maturity

        4. PAIN POINT ANALYSIS
        - Likely operational challenges they face
        - Industry-specific pressure points
        - Potential consulting needs and budget availability
        - Timing factors (fiscal year, project cycles)

        5. OUTREACH STRATEGY
        - Optimal messaging angle and value proposition
        - Relevant case studies or credibility markers to mention
        - Best channels and timing for initial contact
        - Follow-up sequence recommendations

        6. RISK ASSESSMENT
        - Factors that might impact deal probability
        - Competitive threats or existing relationships
        - Budget and timing constraints

        Focus on actionable insights that enable personalized, value-driven outreach. Be specific about consulting opportunities and quantify potential impact where possible.
        """
        
        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=self.max_tokens,
                temperature=self.temperature,
                messages=[{"role": "user", "content": prompt}]
            )
            
            research_result = {
                'prospect_name': name,
                'company': company,
                'title': title,
                'industry': industry,
                'research_date': datetime.now().isoformat(),
                'detailed_analysis': response.content[0].text,
                'confidence_score': self._calculate_confidence_score(response.content[0].text),
                'opportunity_size': self._estimate_opportunity_size(title, company, industry),
                'next_actions': self._extract_next_actions(response.content[0].text)
            }
            
            # Save to research database
            self._save_research_report(research_result)
            
            return research_result
            
        except Exception as e:
            return {'error': f"Research failed: {str(e)}"}
    
    def generate_executive_message(self, prospect_data: Dict[str, Any], 
                                 message_type: str = "introduction") -> str:
        """Generate executive-level LinkedIn messages using Claude"""
        
        prospect_name = prospect_data.get('prospect_name', 'there')
        company = prospect_data.get('company', '')
        title = prospect_data.get('title', '')
        research = prospect_data.get('detailed_analysis', '')
        
        prompt = f"""
        As an expert in executive communications and B2B consulting sales, craft a highly personalized LinkedIn message for this prospect:

        Prospect: {prospect_name}
        Title: {title}
        Company: {company}

        Research Intelligence:
        {research[:1500]}  # Truncate for token management

        Your Firm: {self.company_name}
        Your Expertise: {self.expertise}
        Your Name: {self.your_name}

        Message Requirements:
        1. EXECUTIVE TONE: Professional, peer-to-peer communication appropriate for {title} level
        2. PERSONALIZATION: Reference specific business context, not generic industry speak
        3. VALUE FIRST: Lead with insight or perspective, not a sales pitch
        4. CREDIBILITY: Subtly establish expertise without name-dropping
        5. SOFT CTA: Request a brief conversation, not a sales meeting
        6. LENGTH: 120-180 words maximum

        Message Types:
        - introduction: First-time outreach with connection request
        - follow_up: Follow-up to previous message or interaction
        - referral: Warm introduction through mutual connection
        - content_response: Response to their LinkedIn post/content

        Current Message Type: {message_type}

        Craft a message that feels authentic, provides immediate value, and positions you as a peer rather than a vendor. The goal is to start a genuine business conversation, not make a sale.

        Format as a complete LinkedIn message ready to send.
        """
        
        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=self.max_tokens,
                temperature=self.temperature,
                messages=[{"role": "user", "content": prompt}]
            )
            
            return response.content[0].text
            
        except Exception as e:
            return f"Message generation failed: {str(e)}"
    
    def create_industry_campaign(self, industry: str, target_titles: List[str], 
                               company_size: str = "100-1000 employees") -> Dict[str, Any]:
        """Create comprehensive industry-focused outreach campaign"""
        
        prompt = f"""
        As a strategic consultant specializing in business development, design a comprehensive LinkedIn outreach campaign:

        Campaign Parameters:
        - Target Industry: {industry}
        - Target Titles: {', '.join(target_titles)}
        - Company Size: {company_size}
        - Consulting Firm: {self.company_name}
        - Expertise: {self.expertise}

        Create a detailed campaign strategy including:

        1. CAMPAIGN OVERVIEW
        - Campaign name and objectives
        - Target audience definition and qualification criteria
        - Value proposition and messaging theme
        - Expected timeline and milestones

        2. MARKET ANALYSIS
        - Industry trends and challenges affecting target audience
        - Specific pain points by role/title
        - Competitive landscape and positioning opportunities
        - Seasonal factors and optimal timing

        3. MESSAGING STRATEGY
        - Core value propositions for each target title
        - Industry-specific credibility markers
        - Relevant case studies and success stories to reference
        - Content themes that resonate with this audience

        4. OUTREACH SEQUENCE
        - Initial connection request approach
        - Follow-up message strategy (2-3 touches)
        - Content sharing and value-add touchpoints
        - Meeting request and qualification process

        5. SUCCESS METRICS
        - Connection acceptance rate targets
        - Response rate benchmarks
        - Meeting conversion goals
        - Pipeline value projections

        6. IMPLEMENTATION PLAN
        - Daily and weekly activity targets
        - Tools and resources needed
        - Quality assurance checkpoints
        - Optimization and iteration process

        Focus on scalable, systematic approaches that maintain personalization and deliver consistent results.
        """
        
        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=self.max_tokens,
                temperature=self.temperature,
                messages=[{"role": "user", "content": prompt}]
            )
            
            campaign = {
                'id': f"campaign_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
                'name': f"{industry} Executive Outreach",
                'industry': industry,
                'target_titles': target_titles,
                'company_size': company_size,
                'strategy': response.content[0].text,
                'created_date': datetime.now().isoformat(),
                'status': 'active',
                'prospects_targeted': 0,
                'messages_sent': 0,
                'responses_received': 0,
                'meetings_scheduled': 0
            }
            
            # Save campaign
            self._save_campaign(campaign)
            
            return campaign
            
        except Exception as e:
            return {'error': f"Campaign creation failed: {str(e)}"}
    
    def analyze_message_performance(self, campaign_id: str) -> Dict[str, Any]:
        """Analyze message performance and provide optimization recommendations"""
        
        # Load campaign data
        campaign_data = self._load_campaign(campaign_id)
        if not campaign_data:
            return {'error': 'Campaign not found'}
        
        prompt = f"""
        As a data-driven marketing consultant, analyze this LinkedIn outreach campaign performance:

        Campaign: {campaign_data.get('name', 'Unknown')}
        Industry: {campaign_data.get('industry', 'Various')}
        
        Performance Data:
        - Prospects Targeted: {campaign_data.get('prospects_targeted', 0)}
        - Messages Sent: {campaign_data.get('messages_sent', 0)}
        - Responses Received: {campaign_data.get('responses_received', 0)}
        - Meetings Scheduled: {campaign_data.get('meetings_scheduled', 0)}
        
        Response Rate: {(campaign_data.get('responses_received', 0) / max(campaign_data.get('messages_sent', 1), 1) * 100):.1f}%
        Meeting Conversion: {(campaign_data.get('meetings_scheduled', 0) / max(campaign_data.get('responses_received', 1), 1) * 100):.1f}%

        Provide analysis and recommendations covering:

        1. PERFORMANCE ASSESSMENT
        - How do these metrics compare to industry benchmarks?
        - What are the strongest and weakest performance areas?
        - Overall campaign effectiveness rating (1-10)

        2. MESSAGE OPTIMIZATION
        - Likely reasons for current response rates
        - Specific improvements for subject lines and opening messages
        - A/B testing recommendations for key message elements

        3. TARGETING REFINEMENT
        - Adjustments to prospect qualification criteria
        - Industry or role-specific modifications needed
        - Timing and frequency optimization suggestions

        4. STRATEGIC RECOMMENDATIONS
        - Short-term tactical improvements (next 2 weeks)
        - Medium-term strategic adjustments (next month)
        - Long-term campaign evolution (next quarter)

        5. FORECASTING
        - Projected performance with recommended changes
        - Resource allocation for maximum ROI
        - Pipeline and revenue impact estimates

        Be specific and actionable with all recommendations.
        """
        
        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=self.max_tokens,
                temperature=self.temperature,
                messages=[{"role": "user", "content": prompt}]
            )
            
            analysis = {
                'campaign_id': campaign_id,
                'analysis_date': datetime.now().isoformat(),
                'performance_analysis': response.content[0].text,
                'current_metrics': {
                    'response_rate': campaign_data.get('responses_received', 0) / max(campaign_data.get('messages_sent', 1), 1) * 100,
                    'meeting_rate': campaign_data.get('meetings_scheduled', 0) / max(campaign_data.get('responses_received', 1), 1) * 100
                },
                'recommendations_priority': 'high' if campaign_data.get('responses_received', 0) / max(campaign_data.get('messages_sent', 1), 1) < 0.15 else 'medium'
            }
            
            return analysis
            
        except Exception as e:
            return {'error': f"Analysis failed: {str(e)}"}

    def _calculate_confidence_score(self, research_text: str) -> float:
        """Calculate confidence score based on research depth"""
        indicators = ['specific', 'recent', 'data', 'confirmed', 'verified', 'source']
        score = sum(1 for indicator in indicators if indicator in research_text.lower())
        return min(score / len(indicators), 1.0)
    
    def _estimate_opportunity_size(self, title: str, company: str, industry: str) -> str:
        """Estimate potential opportunity size"""
        title_lower = title.lower()
        if any(term in title_lower for term in ['ceo', 'president', 'founder']):
            return "Large ($100K-500K+)"
        elif any(term in title_lower for term in ['vp', 'director', 'head']):
            return "Medium ($50K-150K)"
        else:
            return "Small ($25K-75K)"
    
    def _extract_next_actions(self, research_text: str) -> List[str]:
        """Extract next actions from research"""
        # Simple extraction - could be enhanced with more sophisticated NLP
        actions = []
        if 'outreach' in research_text.lower():
            actions.append('Send personalized connection request')
        if 'follow up' in research_text.lower():
            actions.append('Schedule follow-up in 1 week')
        if 'case study' in research_text.lower():
            actions.append('Prepare relevant case study')
        return actions or ['Review research and plan outreach']
    
    def _save_research_report(self, research_data: Dict[str, Any]):
        """Save research report to database"""
        try:
            if os.path.exists(self.research_db):
                with open(self.research_db, 'r') as f:
                    reports = json.load(f)
            else:
                reports = {'reports': []}
            
            reports['reports'].append(research_data)
            
            with open(self.research_db, 'w') as f:
                json.dump(reports, f, indent=2)
        except Exception as e:
            print(f"Error saving research report: {e}")
    
    def _save_campaign(self, campaign_data: Dict[str, Any]):
        """Save campaign to database"""
        try:
            if os.path.exists(self.campaigns_db):
                with open(self.campaigns_db, 'r') as f:
                    campaigns = json.load(f)
            else:
                campaigns = {'campaigns': []}
            
            campaigns['campaigns'].append(campaign_data)
            
            with open(self.campaigns_db, 'w') as f:
                json.dump(campaigns, f, indent=2)
        except Exception as e:
            print(f"Error saving campaign: {e}")
    
    def _load_campaign(self, campaign_id: str) -> Optional[Dict[str, Any]]:
        """Load campaign from database"""
        try:
            if not os.path.exists(self.campaigns_db):
                return None
            
            with open(self.campaigns_db, 'r') as f:
                campaigns = json.load(f)
            
            for campaign in campaigns.get('campaigns', []):
                if campaign.get('id') == campaign_id:
                    return campaign
            
            return None
        except Exception as e:
            print(f"Error loading campaign: {e}")
            return None
    
    def _ensure_databases_exist(self):
        """Ensure all databases exist"""
        # Create CSV for prospects
        if not os.path.exists(self.prospects_db):
            df = pd.DataFrame(columns=[
                'name', 'title', 'company', 'industry', 'linkedin_url',
                'research_score', 'opportunity_size', 'last_contact',
                'status', 'notes', 'campaign_id'
            ])
            df.to_csv(self.prospects_db, index=False)
        
        # Create JSON files
        for db_file in [self.research_db, self.campaigns_db, self.analytics_db]:
            if not os.path.exists(db_file):
                with open(db_file, 'w') as f:
                    json.dump({}, f)

# Example Usage
def professional_demo():
    """Demonstrate professional features"""
    
    print("🚀 Initializing Professional LinkedIn AI with Claude...")
    ai = ProfessionalLinkedInAI()
    
    # Example 1: Advanced Prospect Research
    print("\n" + "="*60)
    print("ADVANCED PROSPECT RESEARCH")
    print("="*60)
    
    research = ai.advanced_prospect_research(
        name="Sarah Johnson",
        company="TechCorp Industries", 
        title="Chief Technology Officer",
        industry="Manufacturing Technology"
    )
    
    print("Professional Research Results:")
    print(research.get('detailed_analysis', 'Research failed'))
    
    # Example 2: Executive Message Generation
    print("\n" + "="*60)
    print("EXECUTIVE MESSAGE GENERATION")
    print("="*60)
    
    message = ai.generate_executive_message(research, "introduction")
    print("Generated Executive Message:")
    print(message)
    
    # Example 3: Industry Campaign Creation
    print("\n" + "="*60)
    print("INDUSTRY CAMPAIGN STRATEGY")
    print("="*60)
    
    campaign = ai.create_industry_campaign(
        industry="Financial Services",
        target_titles=["CTO", "Chief Digital Officer", "VP Technology", "Head of Innovation"],
        company_size="500-5000 employees"
    )
    
    if 'error' not in campaign:
        print(f"Campaign Created: {campaign['name']}")
        print("Campaign Strategy:")
        print(campaign.get('strategy', 'Strategy not generated'))
    
    print("\n🎯 Professional LinkedIn AI System Ready!")
    print("Your system includes:")
    print("✅ Advanced prospect research with confidence scoring")
    print("✅ Executive-level message generation")
    print("✅ Industry campaign strategy creation") 
    print("✅ Performance analytics and optimization")
    print("✅ Professional databases and tracking")

if __name__ == "__main__":
    professional_demo()
