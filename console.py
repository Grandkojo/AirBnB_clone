#!/usr/bin/python3
"""This is entry point of the command interpreter"""

import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.review import Review
from models.place import Place
from models.city import City
import re


class HBNBCommand(cmd.Cmd):
    """The HBNB command"""
    prompt = '(hbnb) '
    models_list = ["BaseModel", "User", "State", "City",
                   "Amenity", "Place", "Review"]

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def help_quit(self):
        """The help command for the quit command"""
        print("Quit command to exit the program")

    def do_EOF(self, line):
        """EOF command to close the program"""
        return True

    def do_create(self, line):
        """Creates a new instance of the Basemodel and prints it id"""
        if not line:
            print("** class name is missing **")
            return

        line = line.split()
        class_name = line[0]

        if class_name in self.models_list:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")

    def help_create(self):
        """The help command for create"""
        print("This function creates a new instance of the BaseModel",
              "\nEx:$ create BaseModel\nAny other class name returns an error")

    def do_show(self, line):
        """Prints string representation of an instance with cls_name and id"""
        if line:

            line = line.split()
            class_name = line[0]

            if class_name in self.models_list:
                if len(line) > 1:
                    keys = ".".join(line[0:2])
                    for key, value in storage.all().items():
                        if keys == key:
                            print(value)
                            break
                        else:
                            print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing ***")

    def help_show(self):
        """The help function for the show class"""
        print("Returns the string representation of the BaseModel class with",
              "the class name and id\nAny other ommisions returns an error",
              "Ex:$ show < cls_name > < cls_id >")

    def do_destroy(self, line):
        """deletes an instance based on cls_name and id"""

        if line:

            line = line.split()
            class_name = line[0]

            if class_name in self.models_list:
                if len(line) > 1:
                    key = ".".join(line[0:2])
                    if key in storage.all().keys():
                        storage.delete(key)
                        storage.save()
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def help_destroy(self):
        """The help function for the destroy command"""
        print("Deletes an instance of the BaseModel with reference to",
              "its id\nEx:$ destroy < class_name > < class_id>")

    def do_all(self, line):
        """Prints all instances of BaseModel, with or without cls_name"""
        lists = []
        if line:
            line = line.split()
            class_name = line[0]
            if class_name in self.models_list:
                lists = [str(objects) for k, objects in storage.all().items()
                         if k.startswith(class_name)]
            else:
                print("** class doesn't exist **")
        else:
            lists = [str(objects) for objects in storage.all().values()]
        if lists:
            print(lists)

    def help_all(self):
        """the help command for the all function"""
        print("Prints all the instances of the BaseModel with",
              "or without the class name",
              "\nEx:$ all BaseModel or all\n")

    def do_update(self, line):
        """This is the update command parser"""
        objs_dict = storage.all()
        if not line:
            print("** class name missing **")
            return
        line = self.parse_line(line)
        if line[0] not in self.models_list:
            print("** class doesn't exist **")
            return
        if len(line) <= 1:
            print("** instance id missing **")
            return
        key = ".".join(line[0:2])
        if key not in objs_dict.keys():
            print("** no instance found **")
            return
        if len(line) <= 2:
            print("** attribute name missing **")
            return
        if len(line) <= 3:
            try:
                type(eval(line[2])) != dict
            except NameError:
                print("** value missing **")
                return
        val = None
        list_string = []
        if len(line) >= 4:
            if line[3].startswith("\""):
                for s in line[3:]:
                    list_string.append(s)
                    if s.endswith("\""):
                        break
                val = " ".join(list_string)
            else:
                val = line[3]
            storage.update(key, line[2], eval("{}").format(val))
            storage.save()
        else:
            for k, v in eval(line[2]).items():
                storage.update(key, k, v)
            storage.save()

    def help_update(self):
        """The update command help desk"""
        print("Usage: update <class name> <id> <attribute name>",
              "\"<attribute value>\"\n",
              "Updates an instance based on the class name and id",
              "by adding or updating attribute",
              "(save changes to the JSON file).\nEx:",
              "$ update BaseModel 1234-1234-1234 email \"airbnb@mail.com\"\n")

    def emptyline(self):
        """this is the empty line parser"""
        pass

    def parse_line(self, line):
        """The parse_line function"""
        match = re.match(r"^(.*?)===(.*)===(.*)$", line)
        if match:
            return list(match.groups())
        else:
            return line.split()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
