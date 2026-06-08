from providers.base import Provider


class OutlookProvider(Provider):
    def send_email(self, prompt: str) -> str:
        # Implement the logic to send an email using Outlook API
        return f"Email sent with content: {prompt}"
