
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Permission to read Google Calendar events
SCOPES = [
    "https://www.googleapis.com/auth/calendar.readonly"
]


def main():

    creds = None

    # Check whether token.json already exists
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file(
            "token.json", SCOPES
        )

    # Check whether credentials are valid
    if not creds or not creds.valid:

        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())

        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )

            creds = flow.run_local_server(port=0)

        # Save credentials for future use
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    # Connect to Google Calendar
    service = build(
        "calendar",
        "v3",
        credentials=creds
    )

    print("\nGoogle Calendar Events")
    print("----------------------")

    # Get the next 5 events
    events_result = service.events().list(
        calendarId="primary",
        maxResults=5,
        singleEvents=True,
        orderBy="startTime"
    ).execute()

    events = events_result.get("items", [])

    # Display events
    if not events:
        print("No upcoming events found.")

    else:
        for event in events:
            start = event["start"].get(
                "dateTime",
                event["start"].get("date")
            )

            print(start, "-", event.get("summary", "No Title"))


if __name__ == "__main__":
    main()
