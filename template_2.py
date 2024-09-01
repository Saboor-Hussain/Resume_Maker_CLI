import tkinter as tk
from tkinter import font

# Define colors and fonts
PRIMARY_COLOR = "#13C29C"
SECONDARY_COLOR = "#FFFFFF"
HIGHLIGHT_COLOR = "#D6F9F0"
FONT = ("Helvetica", 12)
HEADER_FONT = ("Helvetica", 24, "bold")
SUBHEADER_FONT = ("Helvetica", 18, "bold")
SECTION_FONT = ("Helvetica", 14, "bold")
PADDING_X = 10
PADDING_Y = 5

def create_resume(user_data):
    name = user_data['personal_info']['name']
    email = user_data['personal_info']['email']
    phone = user_data['personal_info']['phone']
    website = user_data['personal_info']['website']
    job_title = user_data['personal_info']['job_title']
    summary_text = user_data.get('summary', '')
    experiences = user_data.get('experience', [])
    education = user_data['education']['education']
    school = user_data['education']['school']
    dates = user_data['education']['dates']
    skills = user_data['skills']
    languages = user_data['languages']

    root = tk.Tk()
    root.title("Resume Template")
    root.geometry("794x1123")
    root.resizable(False, True)
    root.configure(bg=SECONDARY_COLOR)

    canvas = tk.Canvas(root, bg=SECONDARY_COLOR)
    canvas.pack(side="left", fill="both", expand=True)

    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    frame = tk.Frame(canvas, bg=SECONDARY_COLOR)
    canvas.create_window((0, 0), window=frame, anchor="nw")

    add_personal_info(frame, name, email, phone, website, job_title)
    add_summary(frame, summary_text)
    add_experience(frame, experiences)
    add_education(frame, education, school, dates)
    add_skills(frame, skills)
    add_languages(frame, languages)

    root.mainloop()

def add_personal_info(frame, name, email, phone, website, job_title):
    header_frame = tk.Frame(frame, bg=PRIMARY_COLOR)
    header_frame.pack(fill="x", padx=PADDING_X, pady=10, expand=True)
    
    name_label = tk.Label(header_frame, text=name, font=HEADER_FONT, fg=SECONDARY_COLOR, bg=PRIMARY_COLOR)
    name_label.pack(pady=PADDING_Y, fill="x")
    
    job_title_label = tk.Label(header_frame, text=job_title, font=SUBHEADER_FONT, fg=SECONDARY_COLOR, bg=PRIMARY_COLOR)
    job_title_label.pack(pady=5, fill="x")
    
    contact_info_label = tk.Label(header_frame, text=f"{phone} | {email} | {website}", font=FONT, fg=SECONDARY_COLOR, bg=PRIMARY_COLOR)
    contact_info_label.pack(pady=10, fill="x")

def add_summary(frame, summary_text):
    summary_frame = tk.Frame(frame, bg=SECONDARY_COLOR)
    summary_frame.pack(fill="x", padx=PADDING_X, pady=6, expand=True)
    
    summary_title_label = tk.Label(summary_frame, text="Summary", font=SECTION_FONT, fg=PRIMARY_COLOR, bg=SECONDARY_COLOR, anchor="w")
    summary_title_label.pack(fill="x")
    
    summary_label = tk.Label(summary_frame, text=summary_text, font=FONT, wraplength=730, justify="left", bg=SECONDARY_COLOR)
    summary_label.pack(padx=20, pady=10, fill="x")

def add_experience(frame, experiences):
    experience_frame = tk.Frame(frame, bg=SECONDARY_COLOR)
    experience_frame.pack(fill="x", padx=PADDING_X, pady=4, expand=True)

    experience_title_label = tk.Label(experience_frame, text="Professional Experience", font=SECTION_FONT, fg=PRIMARY_COLOR, bg=SECONDARY_COLOR, anchor="w")
    experience_title_label.pack(fill="x")

    for experience in experiences:
        company = experience.get("company", "")
        position = experience.get("position", "")
        date = experience.get("date", "")
        responsibilities = experience.get("responsibilities", [])

        job_frame = tk.Frame(experience_frame, bg=HIGHLIGHT_COLOR)
        job_frame.pack(pady=10, fill="x", expand=True)

        job_title_label = tk.Label(job_frame, text=company, font=FONT, fg=PRIMARY_COLOR, bg=HIGHLIGHT_COLOR, anchor="w")
        job_title_label.pack(fill="x", padx=PADDING_X, pady=(PADDING_Y, 0), expand=True)

        job_position_date_label = tk.Label(job_frame, text=f"{position} ({date})", font=FONT, bg=HIGHLIGHT_COLOR, anchor="w")
        job_position_date_label.pack(fill="x", padx=PADDING_X, pady=(0, PADDING_Y), expand=True)

        for responsibility in responsibilities:
            responsibility_label = tk.Label(job_frame, text=f"• {responsibility}", font=FONT, wraplength=760, justify="left", bg=HIGHLIGHT_COLOR, anchor="w")
            responsibility_label.pack(fill="x", padx=PADDING_X, pady=(0, PADDING_Y), expand=True)

def add_education(frame, education, school, dates):
    education_frame = tk.Frame(frame, bg=SECONDARY_COLOR)
    education_frame.pack(fill="x", padx=PADDING_X, pady=10, expand=True)
    
    education_title_label = tk.Label(education_frame, text="Education", font=SECTION_FONT, fg=PRIMARY_COLOR, bg=SECONDARY_COLOR, anchor="w")
    education_title_label.pack(fill="x")

    degree_frame = tk.Frame(education_frame, bg=HIGHLIGHT_COLOR)
    degree_frame.pack(pady=10, fill="x", expand=True)

    degree_label = tk.Label(degree_frame, text=f"Degree: {education}", font=FONT, fg=PRIMARY_COLOR, bg=HIGHLIGHT_COLOR, anchor="w")
    degree_label.pack(fill="x", padx=PADDING_X, pady=PADDING_Y, expand=True)
    
    school_label = tk.Label(degree_frame, text=f"School: {school}", font=FONT, bg=HIGHLIGHT_COLOR, anchor="w")
    school_label.pack(fill="x", padx=PADDING_X, pady=PADDING_Y, expand=True)
    
    dates_label = tk.Label(degree_frame, text=f"Dates: {dates}", font=FONT, bg=HIGHLIGHT_COLOR, anchor="w")
    dates_label.pack(fill="x", padx=PADDING_X, pady=PADDING_Y, expand=True)

def add_skills(frame, skills):
    skills_frame = tk.Frame(frame, bg=SECONDARY_COLOR)
    skills_frame.pack(fill="x", padx=PADDING_X, pady=10, expand=True)
    
    skills_title_label = tk.Label(skills_frame, text="Skills", font=SECTION_FONT, fg=PRIMARY_COLOR, bg=SECONDARY_COLOR, anchor="w")
    skills_title_label.pack(fill="x")
    
    skills_text = "\n".join(f"• {skill}" for skill in skills)
    skills_label = tk.Label(skills_frame, text=skills_text, font=FONT, justify="left", bg=SECONDARY_COLOR, anchor="w")
    skills_label.pack(fill="x", padx=PADDING_X, pady=PADDING_Y, expand=True)

def add_languages(frame, languages):
    languages_frame = tk.Frame(frame, bg=SECONDARY_COLOR)
    languages_frame.pack(fill="x", padx=PADDING_X, pady=10, expand=True)
    
    languages_title_label = tk.Label(languages_frame, text="Languages", font=SECTION_FONT, fg=PRIMARY_COLOR, bg=SECONDARY_COLOR, anchor="w")
    languages_title_label.pack(fill="x")
    
    languages_text = "\n".join(f"• {language}" for language in languages)
    languages_label = tk.Label(languages_frame, text=languages_text, font=FONT, justify="left", bg=SECONDARY_COLOR, anchor="w")
    languages_label.pack(fill="x", padx=PADDING_X, pady=PADDING_Y, expand=True)

# data for testing
# user_data = {
#     'personal_info': {
#         'name': 'John Doe',
#         'email': 'johndoe@example.com',
#         'phone': '123-456-7890',
#         'website': 'www.johndoe.com',
#         'job_title': 'Software Developer'
#     },
#     'summary': 'An experienced software developer with a strong background in Python and JavaScript. An experienced software developer with a strong background in Python and JavaScript. An experienced software developer with a strong background in Python and JavaScript. An experienced software developer with a strong background in Python and JavaScript.',
#     'experience': [
#         {
#             'company': 'ABC Corp',
#             'position': 'Senior Developer',
#             'date': '2018 - Present',
#             'responsibilities': [
#                 'Led the development of a major application.',
#                 'Mentored junior developers.'
#             ]
#         },
#         {
#             'company': 'XYZ Ltd',
#             'position': 'Software Engineer',
#             'date': '2015 - 2018',
#             'responsibilities': [
#                 'Developed several web applications.',
#                 'Worked with cross-functional teams to design and implement features.'
#             ]
#         }
#     ],
#     'education': {
#         'education': 'Bachelor of Science in Computer Science',
#         'school': 'ABC University',
#         'dates': '2011 - 2015'
#     },
#     'skills': ['Python', 'JavaScript', 'SQL', 'Django', 'React'],
#     'languages': ['English', 'Spanish', 'French']
# }

# create_resume(user_data)
