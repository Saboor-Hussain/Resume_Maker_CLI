import template_2 as resume_template

def get_input(prompt):
    return input(prompt).strip()

def get_list_input(prompt):
    items = []
    print(prompt)
    while True:
        item = input("Enter item (or press Enter to finish): ").strip()
        if item == "":
            break
        items.append(item)
    return items

def get_experience_input():
    experiences = []
    print("Enter your work experiences (press Enter after each to finish):")
    while True:
        company = get_input("Company: ")
        if not company:
            break
        position = get_input("Position: ")
        date = get_input("Dates (e.g., Jun 2022 - Current): ")
        responsibilities = get_list_input("Enter responsibilities:")
        experiences.append({
            "company": company,
            "position": position,
            "date": date,
            "responsibilities": responsibilities
        })
    return experiences

def get_summary_input():
    while True:
        summary = get_input("Enter a summary of your qualifications (160-350 characters): ")
        if 160 <= len(summary) <= 350:
            return summary
        else:
            print(f"Your summary must be between 160 and 350 characters long. Currently, it is {len(summary)} characters.")

def main():
    user_data = {
        'personal_info': {
            'name': get_input("Enter your name: "),
            'email': get_input("Enter your email: "),
            'phone': get_input("Enter your phone number: "),
            'website': get_input("Enter your website (optional): "),
            'job_title': get_input("Enter your job title: ")
        }
    }
    print()

    user_data['summary'] = get_summary_input()
    print()

    user_data['education'] = {
        'education': get_input("Enter your degree: "),
        'school': get_input("Enter your school/university: "),
        'dates': get_input("Enter the dates attended: ")
    }
    print()

    user_data['experience'] = get_experience_input()
    print()


    user_data['skills'] = get_list_input("Enter your skills (one per line): ")
    print()

    user_data['languages'] = get_list_input("Enter languages you know (one per line): ")
    print()

    resume_template.create_resume(user_data)

if __name__ == "__main__":
    main()
