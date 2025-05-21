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

- **🔌 Lightning Charger** – Leading the pack. It's clear that people are amazed by the lighting of the charger.
- **⚡ USB-C Charging Cable** – Affordable, essential, and always in demand. Over **3,500 units** sold.
- **🔋 AAA Batteries (4-pack)** – Who knew batteries would be this competitive?

### 📉 Lowest Performers

- **🚿 LG Washing Machine** and **🔥 LG Dryer** struggled to make an impact — big ticket items, but low traction.
- Could it be the price? Or are customers shopping elsewhere for home appliances? Either way, these two missed the mark.           

### 🤯 Surprise Twist

- **iPhones and MacBooks?** Not the top sellers! While still valuable, they’re outpaced by everyday essentials.

### 💡 What This Tells Us

- Sometimes, it’s the small stuff that makes a big impact. Low-cost, high-usage products dominate the charts — and drive consistent sales.
""")
st.divider()


