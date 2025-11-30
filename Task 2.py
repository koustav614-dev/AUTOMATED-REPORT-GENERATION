from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# Function to create PDF from text file
def make_pdf(input_file, output_file="report.pdf"):
    doc = SimpleDocTemplate(output_file)
    styles = getSampleStyleSheet()
    story = []
    with open(input_file, "r") as f:
        for line in f:
            text = line.strip()
            story.append(Paragraph(text, styles["Normal"]))
            story.append(Spacer(1, 12))

    doc.build(story)
    print("PDF created:", output_file)

# Example usage
make_pdf("data.txt")