import pandas as pd
import requests


def block_customers(params):
        csv_file = params['csv_file']
        api_url = params['api_url']
        provider_column = params['provider_column']

        df = pd.read_csv(csv_file)

        providers = df[provider_column].tolist()

        for provider in providers:
            response = requests.post(api_url, json={'provider_name': provider})  

            if response.status_code == 200:
                print(f'Successfully blocked {"Provider Name"}')
            else:
                print(f'Failed to block {"Provider Name"}. Status code: {response.status_code}')
