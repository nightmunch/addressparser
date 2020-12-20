import re
import json


class Address:
    def setApt(self, apt):
        self.apt = apt

    def setCity(self, city):
        self.city = city

    def setState(self, state):
        self.state = state

    def setPostcode(self, postcode):
        self.postcode = postcode

    def setStreet(self, street):
        self.street = street

    def setSection(self, section):
        self.section = section

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=False, indent=4)


user_input = input("Input: ")
# Remove comma and stop
user_input = user_input.replace(",", "")
user_input = user_input.replace(".", " ")

newaddress = Address()

# Apt
def findApt():
    try:
        global user_input
        x = re.findall("[No ]{3}\d*", user_input)
        newaddress.setApt(x[0])
        user_input = user_input.replace(x[0], "")
    except:
        pass


# City
def findCity():
    global user_input
    city_list = [
        "Kuala Terengganu",
        "Kuala Lumpur",
        "Bangi",
        "Kajang",
        "Bangi",
        "Damansara",
        "Petaling Jaya",
        "Puchong",
        "Subang Jaya",
        "Cyberjaya",
        "Putrajaya",
        "Mantin",
        "Kuching",
        "Seremban",
    ]

    for x in city_list:
        if x in user_input:
            newaddress.setCity(x)
            user_input = user_input.replace(x, "")


# State
def findState():
    global user_input
    state_list = [
        "Selangor",
        "Terengganu",
        "Pahang",
        "Kelantan",
        "Pulau Pinang",
        "Kedah",
        "Johor",
        "Perlis",
        "Sabah",
        "Sarawak",
    ]

    for x in state_list:
        if x in user_input:
            newaddress.setState(x)
            user_input = user_input.replace(x, "")


# Postcode
def findPostcode():
    try:
        global user_input
        x = re.findall(
            "(0100[0-9]|010[1-9][0-9]|01[1-9][0-9]{2}|0[2-9][0-9]{3}|[1-8][0-9]{4}|9[0-7][0-9]{3}|98[0-7][0-9]{2}|988[0-5][0-9])",
            user_input,
        )
        newaddress.setPostcode(x[0])
        user_input = user_input.replace(x[0], "")
    except:
        pass


# Street
def findStreet():
    global user_input
    try:
        street_list = [
            "[Jalan]{5}.*",
            "[Jln]{3}.*",
            "[Lorong]{6}.*",
            "[Persiaran]{9}.*",
        ]

        from_streetlist = ""

        for i in street_list:
            x = re.findall(i, user_input)
            if len(x) > 0:
                from_streetlist = x[0]

        street = [from_streetlist.split()[i] for i in range(3)]
        newaddress.setStreet(" ".join(street))
        user_input = user_input.replace(" ".join(street), "")
    except:
        # no street
        pass


def findSection():
    global user_input
    newaddress.setSection(" ".join(user_input.split()))


findApt()
findCity()
findState()
findPostcode()
findStreet()
findSection()

print("Output: ")
print(newaddress.toJSON())

# No 11, Chendering, 21080 Kuala Terengganu, Terengganu.