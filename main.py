import tkinter as tk
from tkinter import messagebox
import template_2 as resume_template

def submit_data(user_data):
    resume_template.create_resume(user_data)
    messagebox.showinfo("Success", "Resume created successfully!")

def main():
    root = tk.Tk()
    root.title("Resume Maker")
    root.attributes("-fullscreen", True)

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    column_width = screen_width // 4

    # Configure grid layout
    root.grid_columnconfigure(0, weight=1)
    # root.grid_columnconfigure(1, weight=2)
    root.grid_columnconfigure(2, weight=1)
    root.grid_columnconfigure(3, weight=1)
    # root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=1)
    # root.grid_rowconfigure(2, weight=1)


    # Title Frame
    frame0 = tk.Frame(root, width=screen_width, height=50, bd=2, relief="solid", bg="#2c3e50")
    frame0.grid(column=0, row=0, columnspan=4, sticky="nsew")
    tk.Label(frame0, text="CV MAKER", font=("Helvetica", 24, "bold"), fg="white", bg="#2c3e50").pack(pady=10)

    # Personal Info Frame
    frame1 = tk.Frame(root, width=column_width, height=screen_height, bd=2, relief="solid", bg="#ecf0f1")
    frame1.grid(column=0, row=1, sticky="nsew", padx=10, pady=10)
    tk.Label(frame1, text="Personal Info", font=("Helvetica", 18, "bold"), bg="#ecf0f1").pack(pady=20)
    
    name_var = tk.StringVar()
    email_var = tk.StringVar()
    phone_var = tk.StringVar()
    website_var = tk.StringVar()
    job_title_var = tk.StringVar()

    tk.Label(frame1, text="Name:", font=("Helvetica", 14), bg="#ecf0f1").pack(pady=5)
    tk.Entry(frame1, textvariable=name_var, font=("Helvetica", 12), bd=2, relief="groove").pack(pady=5)
    
    tk.Label(frame1, text="Email:", font=("Helvetica", 14), bg="#ecf0f1").pack(pady=5)
    tk.Entry(frame1, textvariable=email_var, font=("Helvetica", 12), bd=2, relief="groove").pack(pady=5)
    
    tk.Label(frame1, text="Phone:", font=("Helvetica", 14), bg="#ecf0f1").pack(pady=5)
    tk.Entry(frame1, textvariable=phone_var, font=("Helvetica", 12), bd=2, relief="groove").pack(pady=5)
    
    tk.Label(frame1, text="Website/Linkdln:", font=("Helvetica", 14), bg="#ecf0f1").pack(pady=5)
    tk.Entry(frame1, textvariable=website_var, font=("Helvetica", 12), bd=2, relief="groove").pack(pady=5)
    
    tk.Label(frame1, text="Job Title:", font=("Helvetica", 14), bg="#ecf0f1").pack(pady=5)
    tk.Entry(frame1, textvariable=job_title_var, font=("Helvetica", 12), bd=2, relief="groove").pack(pady=5)

    tk.Label(frame1, text="Summary", font=("Helvetica", 18, "bold"), bg="#ecf0f1").pack(pady=20)
    summary_var = tk.Text(frame1, height=5, wrap=tk.WORD, font=("Helvetica", 12), bd=2, relief="groove")
    summary_var.pack(pady=5)

    # Education Section
    frame2 = tk.Frame(root, width=column_width, height=screen_height, bd=2, relief="solid", bg="#ecf0f1")  # Increased width
    frame2.grid(column=1, row=1, sticky="nsew", padx=10, pady=10)
    tk.Label(frame2, text="Education", font=("Helvetica", 18, "bold"), bg="#ecf0f1").pack(pady=20)

    education_var = tk.StringVar()
    school_var = tk.StringVar()
    dates_var = tk.StringVar()

    tk.Label(frame2, text="Degree:", font=("Helvetica", 14), bg="#ecf0f1").pack(pady=5)
    tk.Entry(frame2, textvariable=education_var, font=("Helvetica", 12), bd=2, relief="groove").pack(pady=5)
    
    tk.Label(frame2, text="School/University:", font=("Helvetica", 14), bg="#ecf0f1").pack(pady=5)
    tk.Entry(frame2, textvariable=school_var, font=("Helvetica", 12), bd=2, relief="groove").pack(pady=5)
    
    tk.Label(frame2, text="Dates Attended:", font=("Helvetica", 14), bg="#ecf0f1").pack(pady=5)
    tk.Entry(frame2, textvariable=dates_var, font=("Helvetica", 12), bd=2, relief="groove").pack(pady=5)

    # Experience Section
    frame3 = tk.Frame(root, width=column_width, height=screen_height, bd=2, relief="solid", bg="#ecf0f1")
    frame3.grid(column=2, row=1, sticky="nsew", padx=10, pady=10)
    tk.Label(frame3, text="Experience", font=("Helvetica", 18, "bold"), bg="#ecf0f1").pack(pady=20)

    experiences = []

    def add_experience():
        company = company_var.get().strip()
        position = position_var.get().strip()
        dates = dates_exp_var.get().strip()
        responsibilities = responsibilities_var.get("1.0", "end").strip().splitlines()
        if company and position and dates:
            experiences.append({
                "company": company,
                "position": position,
                "date": dates,
                "responsibilities": responsibilities
            })
            company_var.set("")
            position_var.set("")
            dates_exp_var.set("")
            responsibilities_var.delete("1.0", "end")

    company_var = tk.StringVar()
    position_var = tk.StringVar()
    dates_exp_var = tk.StringVar()
    responsibilities_var = tk.Text(frame3, height=4, wrap=tk.WORD, font=("Helvetica", 12), bd=2, relief="groove")

    tk.Label(frame3, text="Company:", font=("Helvetica", 14), bg="#ecf0f1").pack(pady=5)
    tk.Entry(frame3, textvariable=company_var, font=("Helvetica", 12), bd=2, relief="groove").pack(pady=5)
    
    tk.Label(frame3, text="Position:", font=("Helvetica", 14), bg="#ecf0f1").pack(pady=5)
    tk.Entry(frame3, textvariable=position_var, font=("Helvetica", 12), bd=2, relief="groove").pack(pady=5)
    
    tk.Label(frame3, text="Dates (e.g., Jun 2022 - Current):", font=("Helvetica", 14), bg="#ecf0f1").pack(pady=5)
    tk.Entry(frame3, textvariable=dates_exp_var, font=("Helvetica", 12), bd=2, relief="groove").pack(pady=5)
    
    tk.Label(frame3, text="Responsibilities:", font=("Helvetica", 14), bg="#ecf0f1").pack(pady=5)
    responsibilities_var.pack(pady=5)
    
    tk.Button(frame3, text="Add Experience", font=("Helvetica", 12, "bold"), bg="#3498db", fg="white", command=add_experience).pack(pady=10)

    # Skills and Languages Section
    frame4 = tk.Frame(root, width=column_width, height=screen_height, bd=2, relief="solid", bg="#ecf0f1")
    frame4.grid(column=3, row=1, sticky="nsew", padx=10, pady=10)
    
    tk.Label(frame4, text="Skills", font=("Helvetica", 18, "bold"), bg="#ecf0f1").pack(pady=20)
    skills_var = tk.Text(frame4, height=5, wrap=tk.WORD, font=("Helvetica", 12), bd=2, relief="groove")
    skills_var.pack(pady=5)
    
    tk.Label(frame4, text="Languages", font=("Helvetica", 18, "bold"), bg="#ecf0f1").pack(pady=20)
    languages_var = tk.Text(frame4, height=5, wrap=tk.WORD, font=("Helvetica", 12), bd=2, relief="groove")
    languages_var.pack(pady=5)

    # Submit Button
    def on_submit():
        user_data = {
            'personal_info': {
                'name': name_var.get(),
                'email': email_var.get(),
                'phone': phone_var.get(),
                'website': website_var.get(),
                'job_title': job_title_var.get()
            },
            'summary': summary_var.get("1.0", "end").strip(),
            'education': {
                'education': education_var.get(),
                'school': school_var.get(),
                'dates': dates_var.get()
            },
            'experience': experiences,
            'skills': skills_var.get("1.0", "end").strip().splitlines(),
            'languages': languages_var.get("1.0", "end").strip().splitlines()
        }
        submit_data(user_data)

    submit_frame = tk.Frame(root, width=screen_width, height=100, bg="#2c3e50")
    submit_frame.grid(column=0, row=2, columnspan=4, sticky="nsew")
    tk.Button(submit_frame, text="Create Resume", font=("Helvetica", 14, "bold"), bg="#27ae60", fg="white", command=on_submit).pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()
