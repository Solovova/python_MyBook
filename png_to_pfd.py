from fpdf import FPDF
from PIL import Image
import os.path

def numToStr(i:int):
    s = str(i)
    while (len(s) != 4):
        s = "0" + s
    return s

def makePdf(pdfFileName, listPages, dir = ''):
    if (dir):
        dir += "/"

    cover = Image.open(dir + str(listPages[0]) + ".jpg")
    width, height = cover.size

    pdf = FPDF(unit = "pt", format = [width, height])

    for page in listPages:
        pdf.add_page()
        pdf.image(dir + str(page) + ".jpg", 0, 0)

    pdf.output(dir + pdfFileName + ".pdf", "F")

cover = Image.open("pages\\0001.png")
width, height = cover.size
pdf = FPDF(unit = "pt", format = [width, height])

for i in range(1,9999):
    print (i)
    if not os.path.exists("pages\\"+ numToStr(i) + ".png"):
        break
    pdf.add_page()
    pdf.image("pages\\"+ numToStr(i) + ".png", 0, 0)

pdf.output("pages\\result.pdf", "F")