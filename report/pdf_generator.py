from pathlib import Path

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate


class PDFGenerator:

    def __init__(self):

        self.styles = getSampleStyleSheet()

    def generate(
        self,
        company,
        markdown_report
    ):

        Path("outputs").mkdir(exist_ok=True)

        filename = f"outputs/{company.replace(' ', '_')}_Strategy_Report.pdf"

        document = SimpleDocTemplate(filename)

        story = []

        lines = markdown_report.split("\n")

        for line in lines:

            line = line.strip()

            if not line:
                continue

            # Convert Markdown headings
            if line.startswith("# "):
                story.append(
                    Paragraph(
                        f"<b><font size=18>{line[2:]}</font></b>",
                        self.styles["Heading1"]
                    )
                )

            elif line.startswith("## "):
                story.append(
                    Paragraph(
                        f"<b><font size=14>{line[3:]}</font></b>",
                        self.styles["Heading2"]
                    )
                )

            elif line.startswith("- "):
                story.append(
                    Paragraph(
                        f"• {line[2:]}",
                        self.styles["BodyText"]
                    )
                )

            elif line.startswith("**") and line.endswith("**"):
                story.append(
                    Paragraph(
                        f"<b>{line.replace('**','')}</b>",
                        self.styles["BodyText"]
                    )
                )

            elif line == "---":
                continue

            else:
                story.append(
                    Paragraph(
                        line,
                        self.styles["BodyText"]
                    )
                )

        document.build(story)

        print(f"\n✓ PDF saved to {filename}")

        return filename