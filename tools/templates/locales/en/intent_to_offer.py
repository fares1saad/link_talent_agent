from string import Template

# =========================================================
# 01. INTENT TO OFFER (PRE-OFFER)
# =========================================================

name = "intent_to_offer"

expected_variables = [
    "candidate_name",
    "job_title",
    "company_name",
    "recruiter_name",
    "expected_start_date",
    "current_address",
    "planned_holidays",
]

intent_to_offer = Template("""
Subject: Exciting News! Update regarding your application – $job_title

Dear $candidate_name,

Following our recent interviews, the team was incredibly impressed with your skills and the value you could bring to $company_name. We are delighted to inform you that we would like to proceed with an offer for the $job_title position.

Before we finalize and send the formal offer package, we would like to confirm a few details to ensure everything is accurate:

• Confirm your expected start date  
• Confirm your current residential address for the contract  
• Any planned holidays in the next 3–6 months  

Please reply to this email with the above information at your earliest convenience. Once received, we will prepare and send your official offer letter and onboarding package.

We look forward to having you join our team!

Best Regards,  
$recruiter_name  
$company_name
""")
