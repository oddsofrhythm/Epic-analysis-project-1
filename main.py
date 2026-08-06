# 1. IMPORT YOUR LIBRARIES
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 2. LOAD AND INSPECT THE DATA
# TODO: Load 'epic_clinic_data.csv' into a variable called df
# TODO: Print the first 5 rows using .head()

df= pd.read_csv ('epic_clinic_data.csv')
print(df.head())


# 3. CALCULATE A NEW COLUMN
# TODO: Create df['Total_Visit_mins'] by adding df['Wait_Time_mins'] and df['Exam_Time_mins']
# TODO: Print df[['Patient_ID', 'Total_Visit_mins']].head() to check your work

df['Total_Visit_mins'] = df['Wait_Time_mins'] + df['Exam_Time_mins']
print("step 3")
print(df[['Patient_ID', 'Total_Visit_mins']].head())


# 4. ANALYZE WITH GROUPBY
# TODO: Group by 'Department' and find the mean() of 'Satisfaction_Score'
print("\n-step 4") 
dept_satisfaction = df.groupby('Department')['Satisfaction_Score'].mean()
print(dept_satisfaction)

# 5. VISUALIZE 1: MATPLOTLIB BAR CHART
# TODO: Count visits per department using df['Department'].value_counts()
# TODO: Create a basic Matplotlib bar chart of those counts
# TODO: Add a title like "Patient Volume by Epic Department" and show the plot
plt.figure(figsize=(8, 5))
dept_counts = df['Department'].value_counts()
dept_counts.plot(kind='bar', color='skyblue')
plt.title("Patient Volume by Epic Department")
plt.xlabel("Department")
plt.ylabel("Number of Patients")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('department_volume.png')
plt.close()

# 6. VISUALIZE 2: SEABORN SCATTER PLOT
# TODO: Use sns.scatterplot() with x='Wait_Time_mins' and y='Satisfaction_Score'
# TODO: Add a title like "Impact of Wait Times on Patient Satisfaction" and show the plot
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='Wait_Time_mins', y='Satisfaction_Score', s=100, color='coral')
plt.title("Impact of Wait Times on Patient Satisfaction")
plt.tight_layout()
plt.savefig('wait_vs_satisfaction.png')
plt.close()