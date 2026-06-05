from string import Template

name = "acceptance"

expected_variables = [
    "candidate_name",
    "role",
    "company_name",
]

acceptance = Template("""Hello $candidate_name,

We are pleased to inform you that you have been selected for the $role position at $company_name.

After reviewing your application and interview performance, we were impressed with your skills and background.

We are excited to move forward with you and will share the next steps shortly.

Welcome to $company_name — we look forward to having you on the team!

Best regards,  
$company_name Hiring Team
""")