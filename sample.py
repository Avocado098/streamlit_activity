import streamlit as st

import pandas as pd
import numpy as np

from sqlalchemy import create_engine, inspect
from sqlalchemy import text

warehouse = "postgresql://airyll_user:iKiLhVkL0nHuRn2BFTsGWdmM4vEQI7Ls@dpg-d0k5tbruibrs73983cs0-a.singapore-postgres.render.com/airyll"
engine = create_engine(warehouse,  client_encoding='utf8')
connection = engine.connect()

@st.cache_data
def load_data():
    query_ext = """
        SELECT "Product", count(*) AS count
        FROM sales_data
        GROUP BY "Product";
    """
    result = connection.execute(text(query_ext))
    return pd.DataFrame(result.mappings().all())

df = load_data()



st.title("Sales Dashboard")
st.subheader("Most bought product")
st.bar_chart(df.set_index('Product'))

st.subheader("🔥 Product Spotlight")
st.markdown(":orange[Here’s what everyone’s adding to their carts lately — the most bought products from our sales data!]")
st.divider()

st.markdown("""
### 🚨 Top Performers

- **🔌 USB-C Charging Cable** – Leading the pack! Over **130,000 units** sold. Affordable, essential, and always in demand.
- **⚡ Lightning Charger** – Another power player with equally strong numbers. Apple users clearly love their fast charge!
- **🔋 AAA Batteries (4-pack)** – Powering up the leaderboard. Who knew batteries would be this competitive?

### 🎧 Popular Picks

- **🎶 Apple AirPods Headphones** and **Wired Headphones** are racking up sales. Music lovers unite – wireless or not!
- **📺 Flat Screen TVs** and **SoundSport Speakers** also made it to the top tier.

### 🤯 Surprise Twist

- **iPhones and MacBooks?** Not the top sellers! While still valuable, they’re outpaced by everyday essentials.

### 💡 What This Tells Us

- Sometimes, it’s the small stuff that makes a big impact. Low-cost, high-usage products dominate the charts — and drive consistent sales.
""")
st.divider()


