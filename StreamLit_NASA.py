import streamlit as st
import requests
from datetime import datetime, date

# Streamlit app title
st.title("NASA Astronomy Picture of the Day")

# Define date constraints
MIN_DATE = date(1995, 6, 16)  # APOD started on June 16, 1995
MAX_DATE = date.today()  # Current date

# Input fields for user to specify API key and date
api_key = st.text_input("Enter your NASA API Key:", "")

# Date input with min and max dates
date = st.date_input(
    "Select a Date:",
    value=MAX_DATE,
    min_value=MIN_DATE,
    max_value=MAX_DATE,
    help="Select a date between June 16, 1995 and today"
)

hd = st.checkbox("High Definition Image", value=True)

# Button to fetch data
if st.button("Get INFO"):
    if api_key:
        # Make the API request
        url = "https://api.nasa.gov/planetary/apod"
        params = {
            "api_key": api_key,
            "date": date.strftime("%Y-%m-%d"),
            "hd": hd,
        }
        
        try:
            response = requests.get(url, params=params)
            if response.status_code == 200:
                data = response.json()
                
                # Display the information
                st.subheader(f"Title: {data['title']}")
                st.write(f"Date: {data['date']}")
                st.write(f"Explanation: {data['explanation']}")
                
                # Handle different media types
                media_type = data.get('media_type', 'image')
                if media_type == 'image':
                    image_url = data['hdurl'] if hd and 'hdurl' in data else data['url']
                    st.image(image_url, caption=data['title'], use_column_width=True)
                elif media_type == 'video':
                    st.video(data['url'])
                    
            else:
                st.error(f"Error: {response.status_code}. Failed to retrieve data.")
                if response.status_code == 403:
                    st.warning("Please check if your API key is valid.")
                    
        except requests.exceptions.RequestException as e:
            st.error(f"Network error occurred: {str(e)}")
            
    else:
        st.warning("Please enter a valid NASA API key.")

st.markdown("""
---
### About this app
- This app fetches NASA's Astronomy Picture of the Day (APOD)
- Available dates: June 16, 1995 to present
- To get an API key, visit: [NASA API Portal](https://api.nasa.gov)
""")
