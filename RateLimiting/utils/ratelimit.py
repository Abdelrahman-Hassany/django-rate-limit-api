from django.core.cache import cache

def sendmail_ratelimit(email):
    cache_key = f"attempts:{email}"
    if not cache.add(cache_key, 1, timeout=600):  
        attempts = cache.incr(cache_key)
        if attempts > 5:
            return False
    return True

    