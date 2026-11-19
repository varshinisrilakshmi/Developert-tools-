
from google import genai
from getpass import getpass

# Enter Gemini API key
api_key = getpass("Enter Gemini API key: ")

# Create Gemini client
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
            model="gemini-2.5-flash",
            contents=f"""
            Create a beginner-friendly learning path for: {topic}

            Include:
            1. Prerequisites
            2. Five learning steps
            3. Practical projects
            4. Free learning resources to search for
            5. A weekly study plan
            """
        )

        print("\nYour Learning Path:\n")
        print(response.text or "No response received.")

    except Exception as e:

        error = str(e)

        if "429" in error or "RESOURCE_EXHAUSTED" in error:
            print("Gemini quota exceeded. Check your API usage and limits.")

        elif "API_KEY_INVALID" in error or "API key not valid" in error:
            print("Invalid API key. Check your Gemini API key.")

        elif "503" in error or "UNAVAILABLE" in error:
            print("Gemini server is temporarily unavailable. Try again later.")

        else:
            print("Error:", error)

