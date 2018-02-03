import random
import subprocess

__author__ = 'shrek.zhou'
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm


def do_print(pages):
    file_name = "num_%s.pdf" % 1
    c = canvas.Canvas(file_name)
    for i in range(pages):
        for col in range(1, 3):
            for j in range(12, 18):
                c.setFont("Helvetica", 28)
                c.drawString(70 * col + ((col - 1) * 190), j * 40,
                             '%s + %s =' % (random.randint(1000, 9999), random.randint(1000, 9999)))        
        page_num = c.getPageNumber()
        text = "page %s" % page_num
        c.setFont("Helvetica", 14)
        c.drawRightString(200*mm, 20*mm, text)
        c.showPage()
    c.save()
    # subprocess.call(['lpr', file_name])
    subprocess.call(['open',file_name])

if __name__=='__main__':
    do_print(10)