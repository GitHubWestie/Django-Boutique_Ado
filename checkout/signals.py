from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


from .models import OrderLineItem

@receiver(post_save, sender=OrderLineItem)
def updateOnSave(sender, instance, created, **kwargs):
    # Sender = The model sending an object (In this case OrderLineItem)
    # Instance = The actual instance/object sent from the model
    # Created = Boolean value which states if order is new or existing
    # **kwargs = Any keyword arguments
    """ Update order total on lineitem update/create """
    instance.order.update_total()


@receiver(post_delete, sender=OrderLineItem)
def updateOnSave(sender, instance, **kwargs):
    # Sender = The model sending an object (In this case OrderLineItem)
    # Instance = The actual instance/object sent from the model
    # **kwargs = Any keyword arguments
    """ Update order total on lineitem delete """
    instance.order.update_total()