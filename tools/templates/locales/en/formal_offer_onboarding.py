from string import Template


name = "formal_offer_onboarding"

expected_variables = [
    "candidate_name",
    "job_title",
    "company_name",
    "recruiter_name",
    "salary",
    "currency",
    "start_date",
    "work_location",
    "manager_name",
    "deadline_date",
]

formal_offer_onboarding = Template("""
Subject: Official Offer: Welcome to $company_name! – $job_title

Dear $candidate_name,

Congratulations! We are thrilled to formally offer you the position of $job_title with $company_name. We believe your expertise will be a fantastic addition to our team.

OFFER SUMMARY
Position: $job_title  
Base Salary: $salary $currency  
Start Date: $start_date  
Work Location: $work_location  
Reporting To: $manager_name  

REQUIRED DOCUMENTATION
To finalize your onboarding, please provide clear copies of the following documents:

• Proof of Identity: Valid Passport or National ID Card  
• Proof of Address: Recent utility bill or bank statement (last 3 months)  
• Qualifications: Copies of relevant degrees or certifications  
• Reference Details: Contact information for two professional references  

Please sign the attached offer letter and return it along with the documents listed above by $deadline_date.

We look forward to receiving your signed offer and welcoming you to the team.

Best Regards,  
$recruiter_name  
$company_name
""")
