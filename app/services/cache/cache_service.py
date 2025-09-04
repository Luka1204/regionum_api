
from dogpile.cache import make_region

# Caché en memoria (puede cambiarse a Redis, Memcached, Disk, etc.)
region = make_region().configure(
    "dogpile.cache.memory",
    expiration_time=1000  # TTL en segundos
)