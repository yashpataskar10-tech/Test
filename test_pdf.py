from report.pdf_generator import PDFGenerator


report = """
# AI Strategy Report

## Executive Summary

TCS is one of the world's largest IT services companies.

## Strengths

- Strong global presence
- Large workforce
- AI investments

## Opportunities

- Generative AI
- Cloud Computing

## Conclusion

TCS is well positioned for future growth.
"""

generator = PDFGenerator()

pdf = generator.generate(
    "TCS",
    report
)

print(pdf)