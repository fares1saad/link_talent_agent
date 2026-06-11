from string import Template

name = "post_interview_feedback"

expected_variables = [
    "candidate_name",
    "job_title",
    "company_name",
    "recruiter_name",
]

post_interview_feedback = Template("""
Subject: Your Interview with $company_name – $job_title

Dear $candidate_name,

Thank you for taking the time to meet with our team regarding the $job_title position at $company_name. We appreciate the opportunity to learn more about your background.

After careful evaluation, we have decided to proceed with another candidate whose profile more closely aligns with our current business needs.

We sincerely appreciate the time and effort you invested throughout the interview process.

We wish you continued success in your career.

Best Regards,  
$recruiter_name  
$company_name
""")
