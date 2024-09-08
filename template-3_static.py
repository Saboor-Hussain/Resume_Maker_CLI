import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Resume Builder")
window.geometry("794x1123")
window.configure(bg='white')

# Create a left column frame with a custom color background
left_column = tk.Frame(window, bg='#063970', width=200, height=297)
left_column.pack(side='left', fill='y')

# Align the name to the left in the left column
name_label = tk.Label(left_column, text="Muhammad Haris", bg='#063970', fg='white', font=('Arial', 14, 'bold'))
name_label.pack(padx=5, pady=10, anchor='w')

# Add personal details to the left column
personal_details = {
    "Address": "123 Main St, City, Country",
    "Phone": "+1234567890",
    "Email": "harry@example.com"
}

for detail, value in personal_details.items():
    tk.Label(left_column, text=f"{detail}: {value}", bg='#063970', fg='white', anchor='w').pack(padx=5, pady=2, fill='x')

# Add social media accounts to the left column
social_media = {
    "LinkedIn": "linkedin.com/in/falak",
    "GitHub": "github.com/harry",
    "Twitter": "@harry_twitter",
    "Instagram": "@harry_insta"
}

for platform, handle in social_media.items():
    tk.Label(left_column, text=f"{platform}: {handle}", bg='#063970', fg='white', anchor='w').pack(padx=5, pady=2, fill='x')

# Add summary section to the left column
summary_title = tk.Label(left_column, text="Summary", bg='#063970', fg='white', font=('Arial', 14, 'bold', 'underline'), anchor='w')
summary_title.pack(padx=5, pady=(10, 2), fill='x')

summary_text = '''I am a skilled web developer with a passion for creating responsive and user-friendly web applications.
Proficient in front-end technologies such as HTML, CSS, and JavaScript, I leverage frameworks like React.js and backend tools like Node.js to build dynamic and efficient websites. 
With a strong foundation in database management and API integration, I ensure seamless data flow and enhanced user experiences.
My problem-solving abilities and attention to detail enable me to deliver scalable solutions that meet client objectives effectively.'''
summary_label = tk.Label(left_column, text=summary_text, bg='#063970', fg='white', anchor='w', justify='left', wraplength=190)
summary_label.pack(padx=5, pady=2, fill='x')

# Add interests section to the left column
interests_title = tk.Label(left_column, text="Interests", bg='#063970', fg='white', font=('Arial', 14, 'bold', 'underline'), anchor='w')
interests_title.pack(padx=5, pady=(10, 2), fill='x')

interests_text = '''• Coding\n• Reading\n• Traveling\n• Photography'''
interests_label = tk.Label(left_column, text=interests_text, bg='#063970', fg='white', anchor='w', justify='left', wraplength=190)
interests_label.pack(padx=5, pady=2, fill='x')

# Create a right column frame
right_column = tk.Frame(window, bg='white', width=420, height=297)
right_column.pack(side='right', fill='both', expand=True)

# Add horizontal lines as separators
separator1 = ttk.Separator(right_column, orient='horizontal')
separator1.pack(fill='x', padx=5, pady=(10, 5))

# Add professional skills section
skills_title = tk.Label(right_column, text="Professional Skills", bg='white', fg='black', font=('Arial', 12, 'bold', 'underline'), anchor='w')
skills_title.pack(padx=5, pady=(10, 2), fill='x')

skills_text = '''
I am proficient in several programming languages such as Python, Java, and C++, with hands-on experience in developing robust applications and implementing 
efficient algorithms. My expertise extends to web development, where I have worked extensively with HTML/CSS and JavaScript, utilizing frameworks like React.js 
and Django to create responsive and dynamic web solutions. Additionally, I have a strong foundation in database management, encompassing both SQL and NoSQL databases, 
where I excel in designing optimized schemas and ensuring data integrity through effective query execution. My problem-solving skills are well-honed, enabling me 
to tackle complex challenges with analytical precision and deliver innovative solutions that meet project requirements effectively.

Proficient in Python, Java, and C++
Experienced in HTML/CSS, JavaScript, React.js, and Django
Skilled in SQL and NoSQL database management
Strong problem-solving abilities'''
skills_label = tk.Label(right_column, text=skills_text, bg='white', fg='black', anchor='w', justify='left', wraplength=380)
skills_label.pack(padx=5, pady=2, fill='x')

# Add separator
separator2 = ttk.Separator(right_column, orient='horizontal')
separator2.pack(fill='x', padx=5, pady=(10, 5))

# Add languages section
languages_title = tk.Label(right_column, text="Languages", bg='white', fg='black', font=('Arial', 12, 'bold', 'underline'), anchor='w')
languages_title.pack(padx=5, pady=(10, 2), fill='x')

languages_text = "• Urdu: Native proficiency.\n  Ability to communicate fluently in spoken and written Urdu.\n\n• English: Professional working proficiency.\n  Fluent in English with excellent reading, writing,and communication skills.\n\n• Arabic: Basic proficiency.\n  Familiar with basic conversational Arabic and reading skills."
languages_label = tk.Label(right_column, text=languages_text, bg='white', fg='black', anchor='w', justify='left', wraplength=380)
languages_label.pack(padx=5, pady=2, fill='x')

# Add separator
separator3 = ttk.Separator(right_column, orient='horizontal')
separator3.pack(fill='x', padx=5, pady=(10, 5))

# Add education section
education_title = tk.Label(right_column, text="Education", bg='white', fg='black', font=('Arial', 12, 'bold', 'underline'), anchor='w')
education_title.pack(padx=5, pady=(10, 2), fill='x')

education_text = "• Degree: Bachelor of Science in Computer Science\n  University: UBIT\n  Year: 2024\n• Degree: High School Diploma\n  School: ABC High School\n  Year: 2020"
education_label = tk.Label(right_column, text=education_text, bg='white', fg='black', anchor='w', justify='left', wraplength=380)
education_label.pack(padx=5, pady=2, fill='x')

# Add separator
separator4 = ttk.Separator(right_column, orient='horizontal')
separator4.pack(fill='x', padx=5, pady=(10, 5))

# Add experience section
experience_title = tk.Label(right_column, text="Experience", bg='white', fg='black', font=('Arial', 12, 'bold', 'underline'), anchor='w')
experience_title.pack(padx=5, pady=(10, 2), fill='x')

experience_text = "• Job Title 1: Company Name\n  Duration: Jan 2021 - Present\n  Description: Responsibilities and achievements in this role.\n• Job Title 2: Company Name\n  Duration: Jan 2020 - Dec 2020\n  Description: Responsibilities and achievements in this role."
experience_label = tk.Label(right_column, text=experience_text, bg='white', fg='black', anchor='w', justify='left', wraplength=380)
experience_label.pack(padx=5, pady=2, fill='x')

window.resizable(False, False)

window.mainloop()
