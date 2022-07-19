from django.conf import settings
import requests
from django.db import transaction



class Paystack:
    headers = {'authorization': f'Bearer {settings.PAYSTACK_SECRET_KEY}'}

    def create_transfer_recipient(self, payload):
        try:
            response = requests.post(

                f'{settings.PAYSTACK_URL}/transferrecipient',
                data = payload,
                headers = self.headers
            )

            if response.status_code == 201:
                response = response.json()
                return response['data']['recipient_code']

        except requests.RequestException as err:
            print(err)
            return None

    @transaction.atomic
    def initialize_transaction(self, payload):
        try:
            response = requests.post(

                f'{settings.PAYSTACK_URL}/transaction/initialize',
                data = payload,
                headers = self.headers
            )
            

            if response.status_code == 200:
                response = response.json()

                
                return (
                    response['data']['authorization_url'],
                    response['data']['reference']
                )
        except requests.RequestException as err:
            print(err)
            return None
        



    @transaction.atomic
    def initialize_transfer(self, payload):
        try:

            response = requests.post(

                f'{settings.PAYSTACK_URL}/transfer',
                data = payload,
                headers = self.headers
            )

            if response.status_code == 200:
                response = response.json()

                return response['data']['reference']
        except requests.RequestException as err:
            print(err)
            return None




paystack = Paystack()

