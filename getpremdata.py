import requests
import pandas as pd

#API key
API_KEY = "the API key"  

# API endpoint for Premier League standings
url = "https://api.football-data.org/v4/competitions/PL/standings"

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
    
    # Extract standings data
    standings = data['standings'][0]['table']
    
    # Convert to a clean format
    teams_data = []
    for team in standings:
        teams_data.append({
            'Position': team['position'],
            'Team': team['team']['name'],
            'Played': team['playedGames'],
            'Won': team['won'],
            'Drawn': team['draw'],
            'Lost': team['lost'],
            'Points': team['points'],
            'Goals_For': team['goalsFor'],
            'Goals_Against': team['goalsAgainst'],
            'Goal_Difference': team['goalDifference']
        })
    
    # Create DataFrame
    df = pd.DataFrame(teams_data)
    
    # Save to CSV
    df.to_csv('premier_league_standings.csv', index=False)
    print("\nData saved to premier_league_standings.csv!")
    print("\nCurrent Premier League Standings:")
    print(df.to_string(index=False))
    
else:
    print(f"Error: {response.status_code}")
    print(response.text)