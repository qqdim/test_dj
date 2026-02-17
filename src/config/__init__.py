
from .celery import app as celery_app

__all__ = ('celery_app',)
# celery_app = Celery("orders_service")