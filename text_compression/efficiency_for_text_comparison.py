import matplotlib.pyplot as plt

t4 = "knjiga"
t1 = "nasumicna samo mala slova"
t2 = "nasumicna mala i velika slova"
t3 = "nasumicna slova i cifre"

e4 = 44.482036100805445
e1 = 40.454 
e2 = 27.998 
e3 = 25.436000000000003 

text_only_lower_case = t1
text_lower_case_and_upper_case = t2
text_letters_and_digits = t3

efficiency_book = e4
efficiency_only_lower_case = e1
efficiency_lower_case_and_upper_case = e2
efficiency_letters_and_digits = e3

text = [t4, t1, t2, t3]
efficiencies = [e4, e1, e2, e3]

plt.bar(text, efficiencies, label='Efikasnost kompresije', color='#FFAC1C', width=0.3)  # Use width to set the width of each bar

en4 = 0.9957120747823247
en1 = 0.9953549042905817
en2 = 0.9968225501731769
en3 = 0.9994102824087489

entropy_only_lower_case = en1
entropy_lower_case_and_upper_case = en2
entropy_letters_and_digits = en3

entropy = [en4, en1, en2, en3]

# Adjust the x positions for the second set of bars
#text_second_set = [x + 0.4 for x in text]

# Plotting a bar chart for the second set of values
plt.scatter(text, entropy, label='Entropija', color='#4CBB17', marker='o')

# Adding labels and title
plt.xlabel('Tekstualni fajlovi')
plt.ylabel('%')
plt.title('Efikasnost kompresije u zavisnosti od sadrzaja tekstualnih fajlova')

# Adding a legend to distinguish between sets
plt.legend()

# Display the plot
plt.show()
