from abc import ABC, abstractmethod

class Provider(ABC):

    @abstractmethod
    def send_email(self, email: str , body: str, subject: str ) -> str:
        pass
    @abstractmethod
    def add_draft(self, email: str,body: str,subject: str) -> bool:
        pass
    @abstractmethod
    def search_emails(self, criteria: dict) -> list:
        pass
    @abstractmethod
    def read_email(self, email_id: str) -> dict:
        pass
    @abstractmethod
    def read_thread(self, thread_id: str) -> dict:
        pass
    # def fetch_inbox_with_filter(self, email_id: str) -> dict:
    #     pass
    # def fetch_sent_emails(self, email_id: str) -> dict:
    #     pass
    # def fetch_drafts(self, email_id: str) -> dict:
    #     pass    
    # def delete_email(self, email_id: str) -> bool:
    #     pass

