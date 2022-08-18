
import os

class Color:
    primary = 0x3EE2B7
    transparent = 0x2F3136
    blurple_old = 0x7289DA
    blurple = 0x5865F2
    danger = 0xE92323
    warning = 0xE9B623
    success = 0x44E923

class Auth:
    discord_auth = {
        "debug":"OTc3NTQ2MzY5ODQ3OTI2Nzg0.GNX2Tz.IZJHwr2Gk1hC8akPGDMPW-K5w6M6S133N_CgKw",
        "release": "OTc3NTQ2MzY5ODQ3OTI2Nzg0.GNX2Tz.IZJHwr2Gk1hC8akPGDMPW-K5w6M6S133N_CgKw"
    }
    mongo_auth = "mongodb+srv://Mr4at9700:IlyaRomanov2005@cluster0.6krjiam.mongodb.net/?retryWrites=true&w=majority" # Вам надо зарегестрироваться на сайте mongodb.com и там создать кластер и получить строку для сайта, залью видеом, только куда - хз
    qiwi_auth = "eyJ2ZXJzaW9uIjoiUDJQIiwiZGF0YSI6eyJwYXlpbl9tZXJjaGFudF9zaXRlX3VpZCI6IjFlZmliZC0wMCIsInVzZXJfaWQiOiI3OTUzMDI0NzcxMSIsInNlY3JldCI6IjNmY2RkZTRlZTE2MmVkYjlmZWY0ZDNjMzMwNzBkY2MyMDcwOWJkNGVmYTE4ZDdmMGZmNDA0MzVkMWVhODA5Y2UifX0="

class Other:
    shard_count = 1
    slash = None
    premium_cost = 99
    invoice_lifetime = 360 # в минутах
    p2p = None
    uptime = 0