import httpx, json
from datetime import datetime
import pytz

data = httpx.get("https://api.wheretheiss.at/v1/satellites/25544")
iss = data.json()

pos = httpx.get(f"https://api.wheretheiss.at/v1/coordinates/{iss['latitude']},{iss['longitude']}")
region = pos.json()

dt = datetime.fromtimestamp(iss['timestamp'])
dt = dt.astimezone(pytz.timezone(region['timezone_id']))

info = {
    "latitude": round(iss['latitude'], 5),
    "longitude": round(iss['longitude'], 5),
    "altitude": round(iss['altitude'], 2),
    "velocity": round(iss['velocity'], 2),
    "visibility": iss['visibility'],
    "timezone_id": region['timezone_id'],
    "timestamp": dt.strftime("%Y-%m-%d %H:%M:%S"),
    "utc_offset": str(dt)[-6:],
    "country_code": None if region['country_code'] == '??' else region['country_code']
}

with open("iss_info.jsonl", "a") as f:
    f.write(json.dumps(info) + "\n")