from agents.orchestrator import ConsultantOrchestrator


def main():

    print("=" * 70)
    print("🤖 Agentic AI Strategy Consultant")
    print("=" * 70)

    company = input("\nEnter Company Name: ").strip()

    industry = input("Enter Industry: ").strip()

    orchestrator = ConsultantOrchestrator()

    result = orchestrator.execute(
        company,
        industry
    )

    print("\n")
    print("=" * 70)
    print("CONSULTING PROJECT COMPLETED")
    print("=" * 70)

    print(f"\nCompany : {company}")
    print(f"Industry: {industry}")

    print("\nGenerated Files")

    print(f"\nMarkdown Report : outputs/{company.replace(' ','_')}_Strategy_Report.md")

    print(f"PDF Report      : {result['pdf_path']}")

    print("\nThank you for using Agentic AI Strategy Consultant!")


if __name__ == "__main__":
    main()