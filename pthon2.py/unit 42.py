
from google import genai
import time

# Enter your Gemini API key
api_key = input("Enter your Gemini API key: ")

# Connect to Gemini
client = genai.Client(api_key=api_key)

# Select a model available for your API key
MODEL = "gemini-3.8-flash"

print("\n================================")
print("     AI SHOPPING ASSISTANT")
print("================================")
print("Welcome! I can help you find products.")

while True:

    query = input(
        "\nWhat do you want to buy? (type exit to quit): "
    )

    if query.lower() == "exit":
        print("\nThank you for shopping!")
        break

    # Try sending the request up to 3 times
    for attempt in range(3):

        try:
            response = client.models.generate_content(
                model=MODEL,
                contents=f"""
                You are a helpful AI Shopping Assistant.

                Recommend suitable products based on this request:
                {query}

                Give:
                1. Product suggestions
                2. Important features
                3. Advantages
                4. Buying advice

                Ask about budget or preferences if needed.
                Do not invent current prices or availability.
                """
            )

            print("\nAI Shopping Assistant:")
            print(response.text)

            break

        except Exception as e:

            error_message = str(e)

            if "503" in error_message:

                if attempt < 2:

                    wait_time = 5 * (2 ** attempt)

                    print("\nServer is busy!")
                    print("Retrying in", wait_time, "seconds...")

                    time.sleep(wait_time)

                else:
                    print("\nGoogle Gemini server is still busy.")
                    print("Please try again later.")

            else:
                print("\nAn error occurred:")
                print(error_message)
                break
