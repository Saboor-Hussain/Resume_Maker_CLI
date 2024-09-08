import tkinter as tk
from tkinter.font import Font
from tkinter import filedialog
from tkinter import simpledialog
from PIL import Image, ImageDraw, EpsImagePlugin
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas as pdf_canvas
import os

# Create the main window
window = tk.Tk()

# Set the window size to A4 dimensions in (794 x 1123) pixels at 96 dpi
window.geometry("794x1123")
window.resizable(False, False)
window.title("Template 1")

# Define fonts
header_font = Font(family="Helvetica", size=20, weight="bold")
subheader_font = Font(family="Helvetica", size=12, weight="bold")
normal_font = Font(family="Helvetica", size=12)
small_font = Font(family="Helvetica", size=10)

# Create a canvas
canvas = tk.Canvas(window, width=794, height=1123)
canvas.pack()

def add_header(canvas):
    # Draw a rectangle for the header background
    canvas.create_rectangle(0, 0, 794, 150, fill="#000000")

    # Add header text
    canvas.create_text(100, 40, text="DENVER DAHL", font=header_font, fill="white", anchor="nw")
    canvas.create_text(100, 80, text="Account Manager", font=subheader_font, fill="white", anchor="nw")
    canvas.create_text(100, 110, text="☎ +1 555 555 5555    📧 denver.dahl@example.com    🔗 linkedin.com/denver-dahl",
                       font=small_font, fill="white", anchor="nw")

def add_experience(canvas):
    # Add section title with underline
    canvas.create_text(50, 180, text="EXPERIENCE", font=subheader_font, fill="black", anchor="nw")
    canvas.create_line(50, 200, 700, 200, fill="black", width=3)

    # Add experience content
    experience_text = """Key Account Manager
Lauzon
🗓2016 - Ongoing    📍 San Francisco, CA
Lauzon is a leading worldwide manufacturer, designer, and supplier of bearings, linear motion products, precision bearings, spindles, seals, and services. Responsible for business development with Key Accounts with main focus in ENERGY, POWER UTILITIES and HEAVY industries.
• Achieved 12% growth in the account's revenue and 7% profitability improvement.
• Generated $2,000,000+ new revenue by signing 10 new accounts.
• Presented to over 600 delegates in Europe for facilitating new insurance tracking process.
• Established a Cloud Team and increased Cloud Business profit 8X.

Senior Account Manager
Koep Inc
🗓 2014 - 2016    📍 San Francisco, CA
Koep Inc is Google Street View certified agency.
• Managed Search, Shopping & Display ads for major brands with total monthly ad spend of around $150,000/month.
• Managed the largest key account generating $17,500,000 annually.
• Worked with the BSO team for 6 months as being the sole responsible for their online marketing campaigns.
"""
    canvas.create_text(50, 210, text=experience_text, font=small_font, fill="black", anchor="nw", width=650)

def add_education(canvas):
    # Add section title with underline
    canvas.create_text(50, 540, text="EDUCATION", font=subheader_font, fill="black", anchor="nw")
    canvas.create_line(50, 560, 700, 560, fill="black", width=3)

    # Add education content
    education_text = """Master of Marketing Management [MMM]
La Trobe University
2007 - 2008    San Francisco, CA"""
    canvas.create_text(50, 580, text=education_text, font=small_font, fill="black", anchor="nw")

def add_skills(canvas):
    # Add section title with underline
    canvas.create_text(50, 650, text="SKILLS", font=subheader_font, fill="black", anchor="nw")
    canvas.create_line(50, 670, 700, 670, fill="black", width=3)

    # Add skills content
    skills_text = """MS Office Programs     Windows & Mac OSX     Asana     Salesforce     Agile     CRM Systems     Hubspot
LinkedIn Sales Navigator     Dun & Bradstreet"""
    canvas.create_text(50, 680, text=skills_text, font=small_font, fill="black", anchor="nw")

def add_languages(canvas):
    # Add section title with underline
    canvas.create_text(50, 770, text="LANGUAGES", font=subheader_font, fill="black", anchor="nw")
    canvas.create_line(50, 790, 700, 790, fill="black", width=3)

    # Add languages content
    languages_text = """English - Native
German - Proficient
Greek - Advanced"""
    canvas.create_text(50, 800, text=languages_text, font=small_font, fill="black", anchor="nw")

def save_as_image(canvas):
    # Save the canvas to a postscript file
    canvas.postscript(file="cv.eps", colormode='color')

    # Use PIL to convert the postscript file to a high-resolution PNG
    EpsImagePlugin.gs_windows_binary = r"C:\Program Files\gs\gs10.03.1\bin\gswin64c.exe"  # Update the path to your Ghostscript binary
    img = Image.open("cv.eps")
    img.load(scale=10)  # Increase the scale to improve the resolution
    img.save("cv.png", "png")

    # Clean up the postscript file
    os.remove("cv.eps")

def save_as_pdf(canvas):
    # Directly create a high-resolution PDF with ReportLab
    pdf = pdf_canvas.Canvas("cv.pdf", pagesize=A4)
    
    # Save the canvas to a postscript file
    canvas.postscript(file="cv.eps", colormode='color')
    
    # Use PIL to convert the postscript file to a high-resolution PNG
    EpsImagePlugin.gs_windows_binary = r"C:\Program Files\gs\gs10.03.1\bin\gswin64c.exe"  # Update the path to your Ghostscript binary
    img = Image.open("cv.eps")
    img.load(scale=10)  # Increase the scale to improve the resolution
    img.save("cv.png", "png")

    # Draw the image on the PDF canvas
    pdf.drawImage("cv.png", 0, 0, width=A4[0], height=A4[1])
    pdf.showPage()
    pdf.save()
    
    # Clean up the postscript and PNG files
    os.remove("cv.eps")
    os.remove("cv.png")

def save_cv():
    # Ask the user for a file format
    file_type = simpledialog.askstring("Save As", "Enter file type (pdf/jpg):")
    if file_type == 'pdf':
        save_as_pdf(canvas)
    elif file_type == 'jpg':
        save_as_image(canvas)
    else:
        print("Invalid file type")


def create_resume():
    # Call all the functions to create the CV
    add_header(canvas)
    add_experience(canvas)
    add_education(canvas)
    add_skills(canvas)
    add_languages(canvas)

    # Add save button
    save_button = tk.Button(window, text="Save CV", command=save_cv)
    save_button.place(x=80, y=900)

    window.mainloop()


if __name__ == "__main__":
    create_resume()
