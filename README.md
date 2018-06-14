# Holberton AirBnB project

<img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/263/HBTN-hbnb-Final.png"/>

## How to use:
~ Clone the repo:
https://github.com/Syssos/AirBnB_clone
<br>
Use <bold>chmod</bold> to make program executable (console)
<br>
ex: chmod u+x console.py

## How to use:
This program is an interactive/non-interactive interface that allows for someone to create/manage objects <br>
of multiple classes related to the AirBnB clone. To use this program correctly please take in not how it is used below

### adding objects:
When a user adds an object they will see the JSON string representation of that object being stored in the "file.json" file <br>
The "file.json" is the "Database" for the project. <br>
To create an instance of a class use the keyword Create <br>
There are 2 classes you can create "user" and "BaseModel" to create versions of these you will have to specify that when using create <br>
ex: create BaseModel
<br>
Other commands include:
~ all - shows all instances saved <br>
<br>
  (hbnb) all <br>
<br>
~ show - shows all information for a specific instance <br>
<br>
  (hbnb) show BaseModel/User <id number> <br>
<br>
~ create - creates instance <br>
<br>
  (hbnb) create BaseModel/User <br>
<br>
~ destroy - removes instance <br>
<br>
  (hbnb) destroy BaseModel/User <id number><br>
<br>
~ update - updates an instance of a class <br>
<br>
  (hbnb) update BaseModel <id number> first_name "Betty"<br>
<br>
~ EOF (ctrl + D) - quits the program <br>
<br>
~ help - shows a breif description of the command <br>
<br>
  (hbnb) help <command> <br>
<br>
~ quit - quits the program <br>
<br>
  (hbnb) quit <br>
<br>
