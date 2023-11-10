import os
import msal
from office365.graph_client import GraphClient


class OutlookModule:
    def __init__(self, azure_authority_url, azure_app_client_id, azure_app_client_credential, tenant_name):
        self.azure_authority_url = azure_authority_url
        self.azure_app_client_id = azure_app_client_id
        self.azure_app_client_credential = azure_app_client_credential
        self.tenant_name = tenant_name

    def search_email(self, search_query):
        graph_client = GraphClient.with_token_interactive(self.tenant_name, self.azure_app_client_id)
        me = graph_client.me.get().execute_query()
        return me.search.query_messages(search_query).execute_query()

    def fetch_email(self, count, from_email):
        graph_client = GraphClient.with_token_interactive(self.tenant_name, self.azure_app_client_id)
        me = graph_client.me.get().execute_query()
        return me.messages.select(["subject", "body"]).top(count).get().execute_query_retry(max_retry=5, timeout_secs=1)

    def send_email(self, from_email, to_email, subject, body):
        graph_client = GraphClient.with_token_interactive(self.tenant_name, self.azure_app_client_id)
        me = graph_client.me.get().execute_query()
        me.send_mail(
            subject=subject,
            body=body,
            to_recipients=[to_email]
        ).execute_query_retry(max_retry=5, timeout_secs=1)