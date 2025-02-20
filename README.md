# ISS Data Collection

Automated collection of real-time data from the International Space Station (ISS) using GitHub Actions. The system fetches ISS location data daily at **12:00 UTC** and stores it in a structured **JSONL (JSON Lines) format**. 

**Data Source**: [Where The ISS At?](https://wheretheiss.at)  
**Automation**: Powered by [GitHub Actions](https://github.com/features/actions)  

## Workflow  

1. **Scheduled Data Collection**:  
   - Runs daily at **12:00 UTC** using GitHub Actions.  
   - Fetches real-time ISS data from the [Where The ISS At? API](https://api.wheretheiss.at/v1/satellites/25544).  

2. **Data Storage**:  
   - The collected data is stored in **`iss_info.jsonl`**.  
   - Each entry is stored as a separate line in **JSONL format** for efficient processing.  

## Data Format

Each line in `iss_info.jsonl` represents a snapshot of the ISS's position and related metadata:

```json
{
    "latitude": 43.30165,
    "longitude": 145.40868,
    "altitude": 419.6,
    "velocity": 27594.72,
    "visibility": "eclipsed",
    "timezone_id": "Asia/Tokyo",
    "timestamp": "2025-02-20 03:44:07",
    "utc_offset": "+09:00",
    "country_code": "JP"
}
```

Reference for Timezone info: [Wikipedia](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)

## Attribution

This project was inspired by [iss-location](https://github.com/sanand0/iss-location), created by my professor, **S Anand**.  

A big thanks to:  
- **[Where The ISS At?](https://wheretheiss.at)** for providing the ISS tracking API  
- **GitHub Actions** for seamless automation