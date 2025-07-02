import os

class DBPropertyUtil:
    @staticmethod
    def get_db_properties():
        properties = {}  #the db.properties file is now converted into dictionary
        path = os.path.join(os.path.dirname(__file__), "db.properties")
#__file__ gives the current file’s path (e.g., DBPropertyUtil.py).
# os.path.dirname(__file__) gives the folder name containing this file.
# os.path.join(..., "db.properties") constructs the full path to db.properties file, assuming it's in the same folder as DBPropertyUtil.py.

#Opens the file db.properties for reading.
#with ensures the file is automatically closed after reading.

        with open(path, "r") as file:
            for line in file:
                if line.strip() and not line.startswith("#"):  #ignores empty lines and comments
                    key, value = line.strip().split("=") #again makes it to original form like host=localhost
                    properties[key.strip()] = value.strip()  #adds key-value pair dictionary after removing extra spaces
        return properties   #returns the final dictionary
