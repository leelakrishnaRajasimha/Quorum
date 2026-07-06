from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Image
)

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import inch
import os

styles = getSampleStyleSheet()

title_style = styles["Heading1"]
title_style.alignment = TA_CENTER

heading_style = styles["Heading2"]

normal_style = styles["BodyText"]

def generate_pdf(
    filename,
    startup_name,
    decision,
    ceo_summary,
    scorecard,
    financial,
    investor,
    roadmap
):
    doc = SimpleDocTemplate(filename)

    story = []

    logo_path = "assets/logo.png"

    if os.path.exists(logo_path):
        logo = Image(logo_path, width=1.5*inch, height=1.5*inch)
        logo.hAlign = "CENTER"
        story.append(logo)

    story.append(Spacer(1, 0.2*inch))

    story.append(Paragraph("QUORUM", title_style))

    story.append(
        Paragraph(
            "AI Executive Board Report",
            heading_style
        )
    )

    story.append(Spacer(1,0.3*inch))

    story.append(
        Paragraph(
            f"<b>Startup:</b> {startup_name}",
            normal_style
        )
    )

    story.append(
        Paragraph(
            f"<b>Decision:</b> {decision}",
            normal_style
        )
    )

    story.append(Spacer(1,0.2*inch))

    story.append(
        Paragraph(
            "<b>CEO Executive Summary</b>",
            heading_style
        )
    )

    story.append(
        Paragraph(
            ceo_summary,
            normal_style
        )
    )

    story.append(Spacer(1, 0.3*inch))

    story.append(Paragraph("<b>Executive Scorecard</b>", heading_style))
    story.append(Paragraph(f"<pre>{scorecard}</pre>", normal_style))

    story.append(Spacer(1, 0.25*inch))

    story.append(Paragraph("<b>Financial Projection</b>", heading_style))
    story.append(Paragraph(financial.replace("\n", "<br/>"), normal_style))

    story.append(Spacer(1, 0.25*inch))

    story.append(Paragraph("<b>Investor Recommendation</b>", heading_style))
    story.append(Paragraph(investor.replace("\n", "<br/>"), normal_style))

    story.append(Spacer(1, 0.25*inch))

    story.append(Paragraph("<b>90-Day Roadmap</b>", heading_style))
    story.append(Paragraph(roadmap.replace("\n", "<br/>"), normal_style))

    doc.build(story)