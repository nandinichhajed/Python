import json
import requests as rq

def get_data(url):
    try:
        return rq.get(url).text
    except Exception as e:
        print("Unable to load URL")

def load_json(data):
    if not data is None:
        j = json.loads(data)

        fname = j["results"][0]["name"]["first"]
        lname = j["results"][0]["name"]["last"]
        email = j["results"][0]["email"]
        full_name = j["results"][0]["name"]["first"] + " " + j["results"][0]["name"] ["last"]
        gender = j["results"][0]["gender"]
        date = j["results"][0]["dob"]["date"]
        age = j["results"][0]["dob"]["age"]
        
        return fname, lname, email, gender, full_name, date, age

def main():
    url = "https://randomuser.me/api"

    values = load_json(get_data(url))

    if not values is None:
        print("First Name: ", values[0])
        print("Last Name: ", values[1])
        print("Email: ", values[2])
        print("Gender: ", values[3])
        print("Full Name: ", values[4])
        print("Date: ", values[5])
        print("age: ", values[6])

        
if __name__ == '__main__':
    main()