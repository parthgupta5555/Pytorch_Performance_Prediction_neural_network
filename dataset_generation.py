import numpy as np
import pandas as pd

np.random.seed(42)

n = 10000

experience = np.random.randint(0, 21, n)
training = np.random.randint(0, 51, n)
projects = np.random.randint(0, 31, n)
attendance = np.random.uniform(60, 100, n)

performance = (
    20
    + 1.8 * experience
    + 0.7 * training
    + 2.2 * projects
    + 0.25 * attendance
    + 8 * np.sin(training / 10)
    + 5 * np.log1p(projects)
    - 0.03 * (attendance - 90) ** 2
    + np.random.normal(0, 5, n)
)

performance = np.clip(performance, 0, 100)

df = pd.DataFrame({
    "Experience_Years": experience,
    "Training_Hours_Monthly": training,
    "Projects_Completed": projects,
    "Attendance_Percent": attendance.round(2),
    "Performance_Score": performance.round(2)
})

df.to_csv("employee_performance_dataset.csv", index=False)

print(df.head())
print("\nShape:", df.shape)