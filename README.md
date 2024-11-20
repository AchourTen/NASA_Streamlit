# NASA Astronomy Picture of the Day (APOD) Viewer

## Overview
A Streamlit web application that allows users to explore NASA's Astronomy Picture of the Day (APOD) from June 16, 1995, to the present.

## Features
- Select any date from 1995 to 2020-05-04
- View high-definition images and videos
- Detailed explanations of astronomical images

## Prerequisites
- Python 3.7+
- Streamlit
- Requests library

## Installation

1. Clone the repository:
```bash
git clone https://github.com/AchourTen/NASA_Streamlit.git
cd NASA_Streamlit
```

2. Install required packages:
```bash
pip install streamlit requests
```

3. Get a NASA API Key
- Visit [NASA API Portal](https://api.nasa.gov)
- Sign up for a free API key

## Usage

Run the Streamlit app:
```bash
streamlit run NASA_Streamlit.py
```

### App Functionality
- Enter your NASA API key
- Select a date (between 1995-06-16 and 2020-05-04)
- Optional: Toggle high-definition image
- Click "Get INFO" to retrieve the astronomy image

## Rate Limits
- Personal API Key: 1,000 requests/hour

## Troubleshooting
- Ensure correct API key entry
- Check internet connection
- Verify date selection
- Use debug information for error details

## Contributing
1. Fork the repository
2. Create your feature branch
3. Commit changes
4. Push to the branch
5. Create a pull request


## Acknowledgments
- NASA's Astronomy Picture of the Day Team
- Streamlit
- Python Community
