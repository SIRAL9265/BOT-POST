import requests
import time
import os

# Ambil TOKEN dari GitHub Secrets agar aman
TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = "737344235199660123"

PESAN = """SELL AT FOODMALA <:Verified:1000267030550827128> 

Skill Spice 80 <:WL:880251447470596157> 

ARROZ CON POLLO 9 <:WL:880251447470596157> 

Always Restocked

REMEMBER <:Arrow:850540193626193941> FOODMALA"""

def kirim_pesan():
    url = f"https://discord.com/api/v9/channels/{CHANNEL_ID}/messages"
    payload = {"content": PESAN}
    header = {
        "authorization": TOKEN,
        "content-type": "application/json"
    }

    try:
        r = requests.post(url, json=payload, headers=header)
        status_now = time.strftime('%H:%M:%S')
        if r.status_code == 200:
            print(f"[{status_now}] BERHASIL: Pesan terkirim.")
        else:
            print(f"[{status_now}] GAGAL: Error {r.status_code}")
    except Exception as e:
        print(f"ERROR: {e}")

if __name__ == "__main__":
    kirim_pesan()
