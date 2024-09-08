import tkinter as tk
from tkinter import font

# Define colors and fonts
PRIMARY_COLOR = "#13C29C"
SECONDARY_COLOR = "#FFFFFF"
HIGHLIGHT_COLOR = "#D6F9F0"
FONT = ("Helvetica", 12)
HEADER_FONT = ("Helvetica", 22, "bold")
SUBHEADER_FONT = ("Helvetica", 18, "bold")
SECTION_FONT = ("Helvetica", 14, "bold")

def create_resume_template():
    # Create the main window
    root = tk.Tk()
    root.title("Resume Template")
    root.geometry("794x1123")
    root.resizable(False, True)

    # Set background color
    root.configure(bg=SECONDARY_COLOR)

    # Create a canvas for scrolling
    canvas = tk.Canvas(root, bg=SECONDARY_COLOR)
    canvas.pack(side="left", fill="both", expand=True)

    # Add a scrollbar
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    # Configure the canvas to work with the scrollbar
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Create a frame inside the canvas
    frame = tk.Frame(canvas, bg=SECONDARY_COLOR)
    canvas.create_window((0, 0), window=frame, anchor="nw")

    # Create a frame for the header
    header_frame = tk.Frame(frame, bg=PRIMARY_COLOR)
    header_frame.pack(fill="x", padx=20, pady=10)

    # Add the name label to the header
    name_label = tk.Label(header_frame, text="MUHAMMAD AHMED", font=HEADER_FONT, fg=SECONDARY_COLOR, bg=PRIMARY_COLOR)
    name_label.pack(pady=2)

    # Add the job title label to the header
    job_title_label = tk.Label(header_frame, text="WEB DEVELOPER", font=SUBHEADER_FONT, fg=SECONDARY_COLOR, bg=PRIMARY_COLOR)
    job_title_label.pack(pady=2)

    # Add contact information to the header
    contact_info_label = tk.Label(header_frame, text="+1 3445566 | harry@mail.com | 172 street gulshan e iqbal, karachi sindh", 
                                  font=FONT, fg=SECONDARY_COLOR, bg=PRIMARY_COLOR)
    contact_info_label.pack(pady=10)

    # Create a frame for the summary section
    summary_frame = tk.Frame(frame, bg=SECONDARY_COLOR)
    summary_frame.pack(fill="x", padx=20, pady=6)

    # Add summary title
    summary_title_label = tk.Label(summary_frame, text="Summary", font=SECTION_FONT, fg=PRIMARY_COLOR, bg=SECONDARY_COLOR, anchor="w")
    summary_title_label.pack(fill="x")

    # Add summary text
    summary_text = """Passionate web developer with over 5 years of experience in designing and developing user-friendly websites and applications. Proficient in HTML, CSS, JavaScript, and modern frameworks like React and Angular. Adept at collaborating with cross-functional teams to deliver high-quality digital solutions. Seeking to leverage expertise in front-end development to contribute to a dynamic team focused on innovative web projects."""
    summary_label = tk.Label(summary_frame, text=summary_text, font=FONT, wraplength=700, justify="left", bg=SECONDARY_COLOR)
    summary_label.pack(pady=10)

    # Create a frame for the professional experience section
    experience_frame = tk.Frame(frame, bg=SECONDARY_COLOR)
    experience_frame.pack(fill="x", padx=20, pady=4)

    # Add professional experience title
    experience_title_label = tk.Label(experience_frame, text="Professional Experience", font=SECTION_FONT, fg=PRIMARY_COLOR, bg=SECONDARY_COLOR, anchor="w")
    experience_title_label.pack(fill="x")

    # Create a frame for each job listing
    job1_frame = tk.Frame(experience_frame, bg=HIGHLIGHT_COLOR)
    job1_frame.pack(pady=10, fill="x")

    # Add job title and company
    job1_title_label = tk.Label(job1_frame, text="Company - Company City, Company State", font=FONT, fg=PRIMARY_COLOR, bg=HIGHLIGHT_COLOR, anchor="w")
    job1_title_label.pack(fill="x", padx=10, pady=5)

    # Add job dates
    job1_dates_label = tk.Label(job1_frame, text="Position (Jun 2022 - Current)", font=FONT, bg=HIGHLIGHT_COLOR, anchor="w")
    job1_dates_label.pack(fill="x", padx=10, pady=5)

    # Add job responsibilities and accomplishments
    job1_responsibilities_label = tk.Label(job1_frame, text="• List your most recent (current) role first.\n"
                                                          "• Include your key duties and some accomplishment(s) in 3-4 bullet points.\n"
                                                          "• Use \"keywords\" appearing in the job ad to describe your duties.\n"
                                                          "• Write in present tense if you are still employed.", font=FONT, justify="left", bg=HIGHLIGHT_COLOR, anchor="w")
    job1_responsibilities_label.pack(fill="x", padx=10, pady=5)

    # Create a frame for the second job listing
    job2_frame = tk.Frame(experience_frame, bg=HIGHLIGHT_COLOR)
    job2_frame.pack(pady=10, fill="x")

    # Add job title and company
    job2_title_label = tk.Label(job2_frame, text="Company - Company City, Company State", font=FONT, fg=PRIMARY_COLOR, bg=HIGHLIGHT_COLOR, anchor="w")
    job2_title_label.pack(fill="x", padx=10, pady=5)

    # Add job dates
    job2_dates_label = tk.Label(job2_frame, text="Position (Feb 2018 - May 2022)", font=FONT, bg=HIGHLIGHT_COLOR, anchor="w")
    job2_dates_label.pack(fill="x", padx=10, pady=5)

    # Add job responsibilities and accomplishments
    job2_responsibilities_label = tk.Label(job2_frame, text="• Write in the past tense to describe your main line of work.\n"
                                                          "• Use strong verbs to communicate your duties and responsibilities with impact.\n"
                                                          "• Include a quantifiable accomplishment.", font=FONT, justify="left", bg=HIGHLIGHT_COLOR, anchor="w")
    job2_responsibilities_label.pack(fill="x", padx=10, pady=5)

    # Create a frame for the education section
    education_frame = tk.Frame(frame, bg=SECONDARY_COLOR)
    education_frame.pack(fill="x", padx=20, pady=10)

    # Add education title
    education_title_label = tk.Label(education_frame, text="Education", font=SECTION_FONT, fg=PRIMARY_COLOR, bg=SECONDARY_COLOR, anchor="w")
    education_title_label.pack(fill="x")

    # Create a frame for the degree information
    degree_frame = tk.Frame(education_frame, bg=HIGHLIGHT_COLOR)
    degree_frame.pack(pady=10, fill="x")

    # Add degree and field
    degree_label = tk.Label(degree_frame, text="Degree: BACHELOR IN SCIENCE COMPUTER SCIENCE (BSCS) FROM (UNIVERSITY OF KARACHI)\n (UBIT)", font=FONT, fg=PRIMARY_COLOR, bg=HIGHLIGHT_COLOR, anchor="w")
    degree_label.pack(fill="x", padx=10, pady=5)

    # Add school name and location
    school_label = tk.Label(degree_frame, text="SM PUBLIC ACADEMY (CAMPUS 7)  | GULSHAN E IQBAL (KARACHI And SINDH)", font=FONT, bg=HIGHLIGHT_COLOR, anchor="w")
    school_label.pack(fill="x", padx=10, pady=5)

    # Add graduation date
    graduation_label = tk.Label(degree_frame, text="Graduation Date (2024-2028)", font=FONT, bg=HIGHLIGHT_COLOR, anchor="w")
    graduation_label.pack(fill="x", padx=10, pady=5)

    # Create a frame for the skills section
    skills_frame = tk.Frame(frame, bg=SECONDARY_COLOR)
    skills_frame.pack(fill="x", padx=20, pady=10)

    # Add skills title
    skills_title_label = tk.Label(skills_frame, text="Skills", font=SECTION_FONT, fg=PRIMARY_COLOR, bg=SECONDARY_COLOR, anchor="w")
    skills_title_label.pack(fill="x")

    # Add skills list
    skills_label = tk.Label(skills_frame, text="• Proficient in HTML, CSS, and JavaScript\n"
                                            "• Experienced with modern JavaScript frameworks like React, Angular, and Vue.js\n"
                                            "• Familiar with version control systems like Git and GitHub\n"
                                            "• Skilled in responsive web design and cross-browser compatibility\n"
                                            "• Ability to create and manage databases using SQL and NoSQL technologies", font=FONT, justify="left", bg=SECONDARY_COLOR, anchor="w")
    skills_label.pack(fill="x", padx=10, pady=5)

    root.mainloop()

create_resume_template()