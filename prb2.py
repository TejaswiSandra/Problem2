import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load the dataset
@st.cache_data
def load_data():
    return pd.read_csv("university_student_dashboard_data.csv")

data = load_data()

# Dashboard title
st.title("University Student Dashboard")
st.markdown("""
This dashboard tracks student admissions, retention, and satisfaction over time.
""")

# Sidebar filters
st.sidebar.header("Filters")
selected_year = st.sidebar.selectbox("Select Year", data['Year'].unique())
selected_term = st.sidebar.selectbox("Select Term", data['Term'].unique())

# Filter data based on selections
filtered_data = data[(data['Year'] == selected_year) & (data['Term'] == selected_term)]

# Key Metrics
st.header("Key Metrics")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Applications", filtered_data['Applications'].sum())
with col2:
    st.metric("Total Admissions", filtered_data['Admitted'].sum())
with col3:
    st.metric("Total Enrollments", filtered_data['Enrolled'].sum())

# Retention Rate Trends
st.header("Retention Rate Trends Over Time")
retention_fig = px.line(data, x='Year', y='Retention Rate (%)', color='Term',
                        title="Retention Rate Over Time")
st.plotly_chart(retention_fig)

# Student Satisfaction Trends
st.header("Student Satisfaction Trends Over Time")
satisfaction_fig = px.line(data, x='Year', y='Student Satisfaction (%)', color='Term',
                           title="Student Satisfaction Over Time")
st.plotly_chart(satisfaction_fig)

# Enrollment Breakdown by Department
st.header("Enrollment Breakdown by Department")
enrollment_fig = px.bar(filtered_data, x='Term', y=['Engineering Enrolled', 'Business Enrolled', 'Arts Enrolled', 'Science Enrolled'],
                        title="Enrollment by Department")
st.plotly_chart(enrollment_fig)

# Comparison Between Spring and Fall Terms
st.header("Spring vs. Fall Term Comparison")
comparison_fig = go.Figure()
for term in data['Term'].unique():
    term_data = data[data['Term'] == term]
    comparison_fig.add_trace(go.Scatter(x=term_data['Year'], y=term_data['Enrolled'], mode='lines', name=term))
comparison_fig.update_layout(title="Enrollment Trends: Spring vs. Fall", xaxis_title="Year", yaxis_title="Enrollments")
st.plotly_chart(comparison_fig)

# Key Findings and Insights
st.header("Key Findings and Insights")
st.markdown("""
- **Retention Rates** have steadily increased over the years, with Fall terms consistently performing slightly better than Spring terms.
- **Student Satisfaction** has also shown a positive trend, indicating improved student experiences.
- **Engineering** remains the most popular department, followed by Business, Arts, and Science.
- **Fall terms** generally see higher enrollments compared to Spring terms.
""")
