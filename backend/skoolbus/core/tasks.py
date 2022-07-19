import logging
from huey.contrib.djhuey import db_task
from .models import (
    Transactions,
    SchoolProfile)
from .utils import TransactionStatus

logger = logging.getLogger.__name__


@db_task
def change_to_success(transaction, amount):
    school = SchoolProfile.objects.select_related('user').get(
        destination = transaction.destination.name
    )
    

@db_task()
def handle_webhook(payload: dict):
    logger.info(f"Handling webhook of event -> {payload['event']}")


    if payload['event'] == 'charge.success':
        transaction_ref = payload['data']['reference']
        try:
            transaction = Transactions.objects.select_related('user').get(

                paystack_reference = transaction_ref
            )
            transaction.transaction_status = TransactionStatus.SUCCESS
            transaction.save()
        except Transactions.DoesNotExist:
            logger.error(f'unable to find transactions')
        
    elif payload['event'] == 'transfer.TransactionStatus':
        try:
            transaction_ref = payload['data']['reference']
            amount = payload['data']['amount']
            transaction = Transactions.objects.select_related('user').get(

                paystack_reference = transaction_ref
            )

            transaction.transaction_status = TransactionStatus.SUCCESS
            transaction.amount = -amount
            transaction.save()


            change_to_success(transaction, amount)

        except Transactions.DoesNotExist:
            logger.error(f'unable to find transactions')


