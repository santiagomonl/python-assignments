##tring to access the lab shelf website

import requests

import requests
from bs4 import BeautifulSoup

def login_and_fetch_data(url, username, password, output_file):
    try:
        # Start a session
        session = requests.Session()
        
        # Fetch the page to extract hidden fields
        initial_response = session.get(url)
        initial_response.raise_for_status()

        # Parse the page to extract hidden input values
        soup = BeautifulSoup(initial_response.text, "html.parser")
        region_checksums = soup.find("input", {"id": "pPageFormRegionChecksums"})["value"]
        row_version = soup.find("input", {"id": "pPageItemsRowVersion"})["value"]
        protected = soup.find("input", {"id": "pPageItemsProtected"})["value"]

        # Define the payload with login credentials and hidden fields
        payload = {
            "username": username,  # Replace with the actual username field name
            "password": password,  # Replace with the actual password field name
            "pPageFormRegionChecksums": region_checksums,
            "pPageItemsRowVersion": row_version,
            "pPageItemsProtected": protected,
        }

        # Log in by submitting the form
        login_response = session.post(url, data=payload)
        login_response.raise_for_status()

        # Check for login success by inspecting the response content
        if "Login failed" in login_response.text or "Invalid" in login_response.text:
            print("Login failed. Check your credentials or additional login requirements.")
            return

        # Fetch the data page (same URL, now authenticated)
        data_response = session.get(url)
        data_response.raise_for_status()

        # Save the data to a file
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(data_response.text)

        print(f"Data successfully saved to {output_file}.")

    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage
login_and_data_url = "https://prodis.weizmann.ac.il/pls/htmldb/f?p=329:101::::::"  # Replace with the login page URL
username = "SANTIAGM"  # Replace with your username
password = ""  # Replace with your password
output_filename = "labshelfwebsite_data.html"

login_and_fetch_data(login_and_data_url, username, password, output_filename)
