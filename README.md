# AirBnB Console Project
![AirBnB Logo](https://www.pngitem.com/pimgs/m/132-1322125_transparent-background-airbnb-logo-hd-png-download.png)

## Table of Contents

1. [Project Description](#project-description)
2.  [Installation](#installation)
3. [How it functions](#how-it-functions)
4. [Authors](#authors)

## Project Description

This is the first part of the AirBnB clone, whereby our group worked on the project's backend using Python language and cmd module to make our project interactive with the user.
Our project has a storage. We integrated file storage in our application with the help of JSON.

### Description of the command interpreter:
The application's command line interface is like a bash shell whereby a user inputs specific commands expecting a particular output. However, our application command interpreter accepts limited commands crafted to execute various purposes related to the Airbnb website. Overall, our command line interpreter acts as a frontend whereby users can interact with the backend using Python.

### Command accepted in our command interpreter
1. show
2. create
3. update
4. destroy
5. count

### Examples of how these commands will be implemented
1. creating new objects(ex. user, place or state)
2. Destroying the created objects
3. updating the objects

In short words, our application does not get far away from the CRUD principle, which is used in most backend codes.
CRUD in full is create Read Update and Destroy


## Installation

```
git clone https://github.com/alu-AirBnB_clone.git
```

After cloning, there are various directories and files under AirBnB_clone. 

Those are :
> ./console.py : The main executable of the project , the command interpreter
> 
> models/engine/file_storage.py : It is responsible to serializes intances to a Json File and deserializes Json file to instances
> 
> models/__ init __.py:  A unique `FileStorage` instance for the application
> models/base_model.py: Class that defines all common attributes/methods for other classes.
> 
> models/user.py: User class that inherits from BaseModel
> 
>models/state.py: State class that inherits from BaseModel
>
>models/city.py: City class that inherits from BaseModel
>
>models/amenity.py: Amenity class that inherits from BaseModel
>
>models/place.py: Place class that inherits from BaseModel
>
>models/review.py: Review class that inherits from BaseModel
>



## How it functions

Our app has two modes, which are interactive mode and non-interactive mode.

In *interactive mode*, the user will be able to interact with the command interpreter whereby he or she will always be prompted to enter a command that is among the above that are mentioned to be accepted in our command interpreter. The command interpreter prompt will stay on  until the user quits the program.


```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

In  **Non-interactive mode** , the user will have no participation in the application execution, whereby he or she will not be prompted to do anything as soon the execution of the app starts. The only parts he or she will need to play is to send a command through a pipe to the execution command 

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```


## Available commands and what they do

The recognizable commands by the interpreter are the following:

|Command| Description |
|--|--|
| **quit or EOF** | Exits the program |
| **Usage** | By itself |
| **-----** | **-----** |
| **help** | Provides a text describing how to use a command.  |
| **Usage** | By itself --or-- **help <command\>** |
| **-----** | **-----** |
| **create** | Creates a new instance of a valid `Class`, saves it (to the JSON file) and prints the `id`.  Valid classes are: BaseModel, User, State, City, Amenity, Place, Review. |
| **Usage** | **create <class name\>**|
| **-----** | **-----** |
| **show** | Prints the string representation of an instance based on the class name and `id`  |
| **Usage** | **show <class name\> <id\>** --or-- **<class name\>.show(<id\>)**|
| **-----** | **-----** |
| **destroy** | Deletes an instance based on the class name and `id` (saves the change into a JSON file).  |
| **Usage** | **destroy <class name\> <id\>** --or-- **<class name>.destroy(<id>)** |
| **-----** | **-----** |
| **all** | Prints all string representation of all instances based or not on the class name.  |
| **Usage** | By itself or **all <class name\>** --or-- **<class name\>.all()** |
| **-----** | **-----** |
| **update** | Updates an instance based on the class name and `id` by adding or updating attribute (saves the changes into a JSON file).  |
| **Usage** | **update <class name\> <id\> <attribute name\> "<attribute value\>"** ---or--- **<class name\>.update(<id\>, <attribute name\>, <attribute value\>)** --or-- **<class name\>.update(<id\>, <dictionary representation\>)**|
| **-----** | **-----** |
| **count** | Retrieve the number of instances of a class.  |
| **Usage** | **<class name\>.count()** |

## Author

Jacqueline Nyinawabagesera
Imanzi Kabisa Placide

