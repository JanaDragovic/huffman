import matplotlib.pyplot as plt

import matplotlib.pyplot as plt

# 

t1 = 1
t2 = 2
t3 = 3

e1 = 1
e2 = 2
e3 = 3

text_only_lower_case = t1
text_lower_case_and_upper_case = t2
text_letters_and_digits = t3

efficiency_only_lower_case = e1
efficiency_lower_case_and_upper_case = e2
efficiency_letters_and_digits = e3



text = [t1, t2, t3]
efficiencies = [e1,e2,e3]


plt.scatter(text, efficiencies, label='Set 1', color='blue', marker='o')

en1 = 1
en2 = 2
en3 = 3

entropy_only_lower_case = en1
entropy_lower_case_and_upper_case = en2
entropy_letters_and_digits = en3


entropy = [en1,en2,en3]

# Plotting a scatter plot for the first set of values


# Adding a scatter plot for the second set of values
plt.scatter(text, y_values_set2, label='Set 2', color='red', marker='x')

# Adding labels and title
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.title('Scatter Plot with Two Sets of Values')

# Adding a legend to distinguish between sets
plt.legend()

# Display the plot
plt.show()
