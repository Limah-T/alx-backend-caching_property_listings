# properties/utils.py
from django.core.cache import cache
from django_redis import get_redis_connection
from .models import Property

def get_all_properties():
    queryset = cache.get('all_properties')
    if not queryset:
        queryset = Property.objects.all()
        cache.set('all_properties', queryset, 3600)  # 1 hour
    return queryset


def get_redis_cache_metrics():
    """
    Retrieve Redis keyspace hit/miss metrics.
    Returns a dictionary with hits, misses, and hit ratio.
    """
    conn = get_redis_connection("default")
    info = conn.info("stats")

    hits = info.get("keyspace_hits", 0)
    misses = info.get("keyspace_misses", 0)
    total = hits + misses

    hit_ratio = (hits / total) if total > 0 else 0.0

    metrics = {
        "hits": hits,
        "misses": misses,
        "hit_ratio": round(hit_ratio, 2),  # ratio in percentage terms 0.00 - 1.00
    }

    # Optional: log for visibility
    import logging
    logger = logging.getLogger(__name__)
    logger.info(f"Redis Cache Metrics: {metrics}")

    return metrics
