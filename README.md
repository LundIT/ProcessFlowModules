# Lund PDF Master

A Python library for converting office files to PDF using the iLovePDF API.

## Install the package

```python
pip install ProcessFlowModules
```

## Usage

Here's a basic example of how to use OpenAIModule:

```python
from process_flow_modules.OpenAIModule import OpenAIModule

openai_client = OpenAIModule("api_type", "api_base", "api_version", "engine", "organization")
openai_client.create_gpt_model(messages="prompt")
```

Here's a basic example of how to use OutlookModule:

```python
from process_flow_modules.OutlookModule import OutlookModule

outlook_client = OutlookModule("azure_authority_url", "azure_app_client_id", "azure_app_client_credential")
outlook_client.search_email(search_query=search_query)
```

This project is licensed under the terms of the MIT license
