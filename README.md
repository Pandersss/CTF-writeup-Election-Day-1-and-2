# CTF-writeup-Election-Day-1-and-2
CTF writeup Election Day 1 and 2

# Election Day 1:
In the source code i could see:\
flag_1=flag_1 if username == "admin" else None\
so i knew i had to log in as admin.\
I saw the the verify_user(username, password) function gets run every time you log in.\
I took a look and it is vaunerable for sql injections.\
query = f"SELECT * FROM users WHERE username = '{username}' AND password_hash = '{password}'"\
I go into the login page and type:\
username: admin\
password: ' OR 1=1--\
I got logged in as admin and got the flag.

# Election Day 2:
I had seen in the source code:\
flag_2=flag_2 if vote_percentages["Borat"] == 100 else None\
So borat needs 100% of the votes.\
So when i logged in as admin, i got a list of all the users.\
Now i knew that i could tecnically log in as every user with the same SQL injection.\
So i made a python script to log into every user with the username and password ' OR 1=1--, then it would automatically change the vote of that user.\
(See Election_Day_2.py)\
After running the script with a provided file y.txt with all usernames i finally got 100% borat votes and got the flag.
