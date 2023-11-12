import os
import msal
import urllib
from office365.graph_client import GraphClient


class OutlookModule(object):
    _is_initialized = False

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(OutlookModule, cls).__new__(cls)
        return cls.instance

    def __init__(self, azure_authority_url, azure_app_client_id, azure_app_client_credential, tenant_name):
        if not self._is_initialized:
            self.azure_authority_url = azure_authority_url
            self.azure_app_client_id = azure_app_client_id
            self.azure_app_client_credential = azure_app_client_credential
            self.tenant_name = tenant_name
            self.graph_client = GraphClient.with_token_interactive(tenant_name, azure_app_client_id)
            self._is_initialized = True


    def search_email(self, search_query):
        result = self.graph_client.search.query_messages(search_query).execute_query()
        return result

    def fetch_email(self, count, from_email):
        me = self.graph_client.me.get().execute_query()
        return me.messages.select(["subject", "body"]).top(count).get().execute_query_retry(max_retry=5, timeout_secs=1)

    def fetch_email_by_subject(self, count, subject):
        me = self.graph_client.me.get().execute_query()
        return me.messages.get().filter(f"subject eq '{urllib.parse.quote_plus(subject)}'").select(["subject", "body"]).top(
            count).get().execute_query_retry(
            max_retry=5, timeout_secs=1)

    def send_email(self, to_email, subject, body):
        me = self.graph_client.me.get().execute_query()

        me.send_mail(
            subject=subject,
            body=body,
            to_recipients=[to_email]
        ).execute_query_retry(max_retry=5, timeout_secs=1)