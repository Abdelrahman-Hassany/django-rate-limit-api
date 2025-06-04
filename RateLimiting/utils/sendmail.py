from django.core.mail import send_mail
from django.conf import settings
import logging
logger = logging.getLogger(__name__)

def send_test_mail(email):
    try:
        
        msg = """
        This is a test email
        """

        send_mail(
            "test end mail",
            msg,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,)
        return True
    except:
        logger.error("Failed to send test email", exc_info=True)
        return False