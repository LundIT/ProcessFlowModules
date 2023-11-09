import os
import msal


class OutlookModule:
    def __init__(self, azure_authority_url, azure_app_client_id, azure_app_client_credential):
        self.azure_authority_url = azure_authority_url
        self.azure_app_client_id = azure_app_client_id
        self.azure_app_client_credential = azure_app_client_credential

    def acquire_token(self):
        """
        Acquire token via MSAL
        """
        authority_url = self.azure_authority_url
        app = msal.ConfidentialClientApplication(
            authority=authority_url,
            client_id=self.azure_app_client_id,
            client_credential=self.azure_app_client_credential
        )
        token = app.acquire_token_for_client(scopes=["https://graph.microsoft.com/.default"])
        return token

    def search_email(self, search_query):
        graph_client = GraphClient(self.acquire_token)
        return graph_client.search.query_messages(search_query).execute_query()

    def fetch_email(self, count, from_email):
        graph_client = GraphClient(self.acquire_token)
        user = graph_client.users.get().filter(
            f"userPrincipalName eq '{from_email}'").execute_query()
        return user[0].messages.select(["subject", "body"]).top(count).get().execute_query_retry(max_retry=5, timeout_secs=1)

    def send_email(self, from_email, to_email, subject, body):
        graph_client = GraphClient(self.acquire_token)
        user = GraphClient(self.acquire_token).users.get().filter(
            f"userPrincipalName eq '{from_email}'").execute_query()
        user[0].send_mail(
            subject=subject,
            body=body,
            to_recipients=[to_email]
        ).execute_query_retry(max_retry=5, timeout_secs=1)