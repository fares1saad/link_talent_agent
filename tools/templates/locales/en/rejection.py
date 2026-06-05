from string import Template

name = "rejection"

expected_variables = [
    "candidate_name",
    "role",
    "company_name",
]

rejection = Template("""Hello $candidate_name,

Thank you for applying for the $role position at $company_name.

After careful consideration, we have decided not to move forward with your application at this time.

We truly appreciate your interest in $company_name and the time you invested in the application process.

We wish you the best of luck in your job search and future career.

Best regards,  
$company_name Hiring Team
""")