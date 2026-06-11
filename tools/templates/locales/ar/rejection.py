from string import Template


name = "rejection"

expected_variables = [
    "candidate_name",
    "job_title",
    "company_name",
    "recruiter_name",
]

rejection = Template("""
Subject: Update Regarding Your Application to $company_name – $job_title

Dear $candidate_name,

Thank you for your interest in $company_name and for taking the time to participate in our recruitment process for the $job_title position.

After careful consideration, we have decided to move forward with other candidates whose qualifications more closely match the current requirements of the role.

We genuinely appreciate your interest in joining our team and wish you every success in your professional journey.

Kind Regards,  
$recruiter_name  
$company_name
""")
