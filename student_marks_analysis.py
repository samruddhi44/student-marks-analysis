
import pandas as pd
import matplotlib.pyplot as plt

# Load marks from CSV
data = pd.read_csv("marks.csv")

# Display basic statistics
print("Summary Statistics:")
print(data.describe())

# Plot marks
plt.figure(figsize=(10,6))
plt.plot(data['Name'], data['Marks'], marker='o', color='teal')
plt.title('Student Marks Analysis')
plt.xlabel('Student Name')
plt.ylabel('Marks')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
