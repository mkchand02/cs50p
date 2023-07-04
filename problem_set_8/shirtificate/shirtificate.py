"""
Suppose that you’d like to implement a CS50 “shirtificate,” a PDF with an image of an I took CS50 t-shirt, shirtificate.png, customized with a user’s own name.

In a file called shirtificate.py, implement a program that prompts the user for their name and outputs, using fpdf2, a CS50 shirtificate in a file called shirtificate.pdf similar to this one for John Harvard, with these specifications:

The orientation of the PDF should be Portrait.
The format of the PDF should be A4, which is 210mm wide by 297mm tall.
The top of the PDF should “CS50 Shirtificate” as text, centered horizontally.
The shirt’s image should be centered horizontally.
The user’s name should be on top of the shirt, in white text.
All other details we leave to you. You’re even welcome to add borders, colors, and lines. Your shirtificate needn’t match John Harvard’s precisely. And no need to wrap long names across multiple lines.
"""
from fpdf import FPDF

class PDF(FPDF):
  def process(self, name, img):
    #Add a page
    self.add_page()
    #Set font
    self.set_font("Arial", "B", 35)
    #Add title
    self.cell(0, 50, "CS50 Shirtificate", new_x = "LMARGIN", new_y = "NEXT", align = "C")
    #Add the shirt img
    self.image(img, w = self.epw)

    #Set font and white text color for the next content
    self.set_font("Arial", "B", 15)
    self.set_text_color(255, 255, 255)
    self.cell(200, -240, f"{name} took CS50", new_x = "LMARGIN", new_y = "NEXT", align = "C")
    #save output as pdf
    self.output("shirtificate.pdf")

name = input("Name :")
img = "shirtificate.png"
pdf = PDF()
pdf.process(name, img)