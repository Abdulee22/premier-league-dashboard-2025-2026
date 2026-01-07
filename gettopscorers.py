import requests
import pandas as pd

#API key
API_KEY = "API key"  

# API endpoint for Premier League top scorers
url = "https://api.football-data.org/v4/competitions/PL/scorers"

#Headers with your API key
headers = {
    "X-Auth-Token": API_KEY
}   

# API call
response = requests.get(url, headers=headers)

# Check if it worked
if response.status_code == 200:
    data = response.json()
    print("Success! Data retrieved")
    
    # Extract top scorers data
    scorers = data['scorers']
    
    # Convert to a clean format
    scorers_data = []
    for scorer in scorers:
        scorers_data.append({
            'Penalties': scorer['penalties'] if 'penalties' in scorer else 0,
            'Player': scorer['player']['name'],
            'Team': scorer['team']['name'],
            'Goals': scorer['goals']
        })
    
    # Create DataFrame
    df = pd.DataFrame(scorers_data)
    
    # Save to CSV
    df.to_csv('premier_league_top_scorers.csv', index=False)
    print("\nData saved to premier_league_top_scorers.csv!")
    print("\nCurrent Premier League Top Scorers:")
    print(df.to_string(index=False))

else:
    print(f"Error: {response.status_code}")
    print(response.text)


