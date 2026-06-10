# from schemes.email import SearchEmailsInput

# def build_gmail_query(filters: SearchEmailsInput) -> str:
#     query_parts = []

#     # Always scope to primary category
#     query_parts.append("category:primary")

#     # Label/folder — INBOX is the default
#     if filters.label and filters.label.upper() != "INBOX":
#         query_parts.append(f"in:{filters.label.lower()}")
#     else:
#         query_parts.append("in:inbox")

#     if filters.sender:
#         query_parts.append(f"from:{filters.sender}")
#     if filters.recipient:
#         query_parts.append(f"to:{filters.recipient}")
#     if filters.subject:
#         query_parts.append(f'subject:"{filters.subject}"')
#     if filters.keywords:
#         query_parts.append(filters.keywords)
#     if filters.start_date:
#         query_parts.append(f"after:{filters.start_date}")
#     if filters.end_date:
#         query_parts.append(f"before:{filters.end_date}")
#     if filters.unread_only:
#         query_parts.append("is:unread")
#     if filters.has_attachment:
#         query_parts.append("has:attachment")

#     return " ".join(query_parts)




from schemes.email import SearchEmailsInput

def build_gmail_query(filters: SearchEmailsInput) -> str:
    query_parts = []

    # Explicitly exclude promotions, social, updates, forums
    query_parts.append("-category:promotions")
    query_parts.append("-category:social")
    query_parts.append("-category:updates")
    query_parts.append("-category:forums")

    # Label/folder — INBOX is the default
    if filters.label and filters.label.upper() != "INBOX":
        query_parts.append(f"in:{filters.label.lower()}")
    else:
        query_parts.append("in:inbox")

    if filters.sender:
        query_parts.append(f"from:{filters.sender}")
    if filters.recipient:
        query_parts.append(f"to:{filters.recipient}")
    if filters.subject:
        query_parts.append(f'subject:"{filters.subject}"')
    if filters.keywords:
        query_parts.append(filters.keywords)
    if filters.start_date:
        query_parts.append(f"after:{filters.start_date}")
    if filters.end_date:
        query_parts.append(f"before:{filters.end_date}")
    if filters.unread_only:
        query_parts.append("is:unread")
    if filters.has_attachment:
        query_parts.append("has:attachment")

    return " ".join(query_parts)