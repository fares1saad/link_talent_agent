from providers.serviceProviders.outlook import OutlookProvider
from providers.serviceProviders.gmail import GmailProvider

class ProviderFactory:
    @staticmethod
    def get_provider(provider_name: str):
        if provider_name == "outlook":
            return OutlookProvider()
        elif provider_name == "gmail":
            return GmailProvider()
        else:
            raise ValueError(f"Unknown provider: {provider_name}")
