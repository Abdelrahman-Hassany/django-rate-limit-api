from django.core.cache import cache

def sendmail_ratelimit(email):
    cache_key = f"attempts:{email}"
    attempts = cache.get(cache_key, 0)
    if attempts >= 5:
        return False
    cache.incr(cache_key)
    cache.expire(cache_key, 600)  
    return True