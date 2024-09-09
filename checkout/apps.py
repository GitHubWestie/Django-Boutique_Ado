from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkout'

    # Ensures signal connection is ready at app startup
    def ready(self):
        import checkout.signals
