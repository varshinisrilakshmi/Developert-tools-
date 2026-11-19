from google import genai
from getpass import getpass

api_key = getpass("Enter Gemini API key: ")

client = genai.Client(api_key=api_key)

print("\nLearning Path Generator Agent")

while True:
    topic = input("\nEnter a topic to learn (or exit): ").strip()

    if topic.lower() == "exit":
        print("Goodbye!")
        break

    if not topic:
        print("Please enter a topic.")
        continue

    try:
        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=f"""Create a beginner-friendly learning path for: {topic}

Include:
1. Prerequisites
2. Five learning steps
3. Practical projects
4. Free learning resources
5. Weekly study plan"""
        )

        print("\nYour Learning Path:")
        print(response.text or "No response received.")

    except Exception as e:
        print("Error:", e)
        
