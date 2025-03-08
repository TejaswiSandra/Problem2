import streamlit as st
import pandas as pd
import plotly.express as px



# Load the data
@st.cache_data
def load_data():
    return pd.read_csv('university_student_dashboard_data.csv')

df = load_data()

# Set up the Streamlit app
st.title('University Student Dashboard')

# Display the raw data
st.subheader('Raw Data')
st.write(df)

# Total applications, admissions, and enrollments per term
st.subheader('Total Applications, Admissions, and Enrollments per Term')
term_summary = df.groupby(['Year', 'Term']).agg({
    'Applications': 'sum',
    'Admitted': 'sum',
    'Enrolled': 'sum'
}).reset_index()
st.write(term_summary)

# Retention rate trends over time
st.subheader('Retention Rate Trends Over Time')
retention_fig = px.line(df, x='Year', y='Retention Rate (%)', color='Term', title='Retention Rate Over Time')
st.plotly_chart(retention_fig)

# Student satisfaction scores over the years
st.subheader('Student Satisfaction Scores Over the Years')
satisfaction_fig = px.line(df, x='Year', y='Student Satisfaction (%)', color='Term', title='Student Satisfaction Over Time')
st.plotly_chart(satisfaction_fig)

# Enrollment breakdown by department
st.subheader('Enrollment Breakdown by Department')
department_enrollment = df.melt(id_vars=['Year', 'Term'], value_vars=['Engineering Enrolled', 'Business Enrolled', 'Arts Enrolled', 'Science Enrolled'], 
                                var_name='Department', value_name='Enrolled')
department_fig = px.bar(department_enrollment, x='Year', y='Enrolled', color='Department', barmode='group', title='Enrollment by Department Over Time')
st.plotly_chart(department_fig)

# Comparison between Spring vs. Fall term trends
st.subheader('Spring vs. Fall Term Trends')
term_comparison = df.groupby('Term').agg({
    'Applications': 'mean',
    'Admitted': 'mean',
    'Enrolled': 'mean',
    'Retention Rate (%)': 'mean',
    'Student Satisfaction (%)': 'mean'
}).reset_index()
st.write(term_comparison)

# Compare trends between departments, retention rates, and satisfaction levels
st.subheader('Departmental Trends')
department_trends = df.melt(id_vars=['Year', 'Term'], value_vars=['Engineering Enrolled', 'Business Enrolled', 'Arts Enrolled', 'Science Enrolled', 'Retention Rate (%)', 'Student Satisfaction (%)'], 
                            var_name='Metric', value_name='Value')
trend_fig = px.line(department_trends, x='Year', y='Value', color='Metric', facet_col='Term', title='Departmental Trends Over Time')
st.plotly_chart(trend_fig)

# Key findings and actionable insights
st.subheader('Key Findings and Actionable Insights')
st.write("""
1. **Retention Rate**: The retention rate has been steadily increasing over the years, with a noticeable improvement in the Fall terms.
2. **Student Satisfaction**: Satisfaction scores have shown a consistent upward trend, indicating positive student experiences.
3. **Enrollment by Department**: Engineering and Business departments have seen the highest enrollment numbers, while Arts and Science have remained relatively stable.
4. **Spring vs. Fall**: Fall terms generally have higher retention and satisfaction rates compared to Spring terms.
""")
