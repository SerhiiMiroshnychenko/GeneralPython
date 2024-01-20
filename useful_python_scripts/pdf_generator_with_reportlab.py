from reportlab.pdfgen import canvas

pdf_file = 'output.pdf'
text = 'Hello, this is a sample PDF.'

c = canvas.Canvas(pdf_file)
c.drawString(100, 750, text)
c.save()
