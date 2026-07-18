from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def create_report(summary, comparison, similarity):

    doc = SimpleDocTemplate("AI_Report.pdf")
    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph("<b>AI Multi Document Analysis Report</b>", styles["Title"]))

    story.append(Paragraph("<br/><b>Summary</b>", styles["Heading2"]))
    story.append(Paragraph(summary.replace("\n", "<br/>"), styles["BodyText"]))

    story.append(Paragraph("<br/><b>Comparison</b>", styles["Heading2"]))
    story.append(Paragraph(comparison.replace("\n", "<br/>"), styles["BodyText"]))

    story.append(Paragraph("<br/><b>Similarity Score</b>", styles["Heading2"]))
    story.append(Paragraph(similarity, styles["BodyText"]))

    doc.build(story)

    return "AI_Report.pdf"