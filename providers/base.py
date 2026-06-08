from abc import ABC, abstractmethod

class Provider(ABC):

    @abstractmethod
    def send_email(self, prompt: str) -> str:
        pass