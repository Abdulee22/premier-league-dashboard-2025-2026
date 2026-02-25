# premier-league-dashboard-2025-2026


An interactive Power BI dashboard providing real-time analysis of the Premier League 2025/26 season, including league standings and top scorers statistics.

![Dashboard Preview](dashboard_screenshot.png)

## 🎯 Project Overview

This project demonstrates end-to-end data analytics skills by extracting live Premier League data via API, processing it with Python, and creating interactive visualizations in Power BI.

## 🛠️ Technologies Used

- **Python** - Data extraction and processing
  - `requests` - API calls
  - `pandas` - Data manipulation
- **Power BI Desktop** - Dashboard creation and visualization
- **Football-Data.org API** - Live Premier League data source

## 📊 Features

- **League Standings Table** - Current positions, points, wins, draws, losses, goals, and goal difference
- **Top Scorers Visualization** - Bar chart showing leading goal scorers
- **Top Scorers Table** - Detailed statistics including goals, assists, and penalties
- **Live Data** - Pulls current season data from Football-Data.org API

## 🚀 How to Run

### Prerequisites
- Python 3.x installed
- Power BI Desktop installed
- Football-Data.org API key (free tier available at football-data.org)

### Steps
1. Clone this repository
2. Install required Python packages:
```bash
   pip install requests pandas
```
3. Add your API key to the Python scripts
4. Run the data extraction scripts:
```bash
   python getpremdata.py
   python get_top_scorers.py
```
5. Open the Power BI file and refresh data sources

## 📁 Project Structure
```
premier-league-dashboard/
│
├── getpremdata.py              # Extracts league standings
├── get_top_scorers.py          # Extracts top scorers data
├── premier_league_standings.csv # Output data file
├── premier_league_top_scorers.csv # Output data file
└── README.md                   # Project documentation
```

## 📈 Skills Demonstrated

- API integration and data extraction
- Data cleaning and transformation with pandas
- Data visualization and dashboard design
- Business intelligence reporting
- Python programming

## 👤 Author

**Abdulhakim Mohamed**

Aspiring Data Analyst | Python • Power BI • API Integration

## 📝 License

This project is open source and available for educational purposes.
