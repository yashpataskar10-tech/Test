from services.gemini_service import GeminiService

llm = GeminiService()

response = llm.generate_json("""
Return ONLY this JSON.

{
  "name":"TCS",
  "industry":"IT"
}
""")

print(response)