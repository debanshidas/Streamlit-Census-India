import streamlit as st
import pandas as pd
import seaborn as sns

# Set dark theme
st.set_page_config(page_title="Indian Population Dashboard", layout="wide", initial_sidebar_state="expanded")

# Set dark theme for matplotlib
plt.style.use('dark_background')
sns.set_style("darkgrid")


# Load the dataset
@st.cache_data
def load_data():
    data = pd.read_csv("census2011.csv")
    return data

data = load_data()

# Title of the dashboard
st.markdown("<h1 style='color: white;'>India Census 2011 Dashboard</h1>", unsafe_allow_html=True)


# Sidebar for filters
st.sidebar.markdown("<h2 style='color: white;'>Filters</h2>", unsafe_allow_html=True)


# Filter by State
states = data["State"].unique()
selected_state = st.sidebar.selectbox("Select State", ["All"] + list(states))

# Filter by District
if selected_state != "All":
    filtered_data = data[data["State"] == selected_state]
else:
    filtered_data = data

districts = filtered_data["District"].unique()
selected_district = st.sidebar.selectbox("Select District", ["All"] + list(districts))

if selected_district != "All":
    filtered_data = filtered_data[filtered_data["District"] == selected_district]

# Display filtered data
st.subheader("Filtered Data")
st.dataframe(filtered_data)

# Visualizations
st.subheader("Visualizations")

# Population Distribution
st.write("### Population Distribution")
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=filtered_data, x="District", y="Population", ax=ax)
plt.xticks(rotation=90)
st.pyplot(fig)

# Literacy Rate
st.write("### Literacy Rate")
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=filtered_data, x="District", y="Literacy", ax=ax)
plt.xticks(rotation=90)
st.pyplot(fig)

# Growth Rate
st.write("### Growth Rate")
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=filtered_data, x="District", y="Growth", ax=ax)
plt.xticks(rotation=90)
st.pyplot(fig)

# Sex Ratio
st.write("### Sex Ratio")
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=filtered_data, x="District", y="Sex-Ratio", ax=ax)
plt.xticks(rotation=90)
st.pyplot(fig)

# Download Option
st.subheader("Download Filtered Data")
if st.button("Download CSV"):
    csv = filtered_data.to_csv(index=False)
    st.download_button(
        label="Click to Download",
        data=csv,
        file_name="filtered_census_data.csv",
        mime="text/csv",
    )


