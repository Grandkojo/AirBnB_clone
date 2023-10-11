#!/usr/bin/python3
"""This is the file storage engine"""


class FileStorage:
    """The files storage class"""
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """The constructor of the class"""
        pass

    def all(self):
        """ Returns the dictionary of __objects """
        return FileStorage.__objects

    def new(self, obj):
        """creates an new obj with key <obj class name>.id"""
        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        import json
        with open(FileStorage.__file_path, "w", encoding="utf-8") as sfile:
            json_dictionary = {}
        for key, value in FileStorage.__objects.items():
            if key and value:
                json_dictionary[key] = value.to_dict()
        json_string = json.JSONENCODER().encode(json_dictionary)
        sfile.write(json_string)

    def reload(self):
        """Deserializes JSON files to objects"""
        import json
        with open(FilesStorage.__file_path, "r", encoding="utf=8") as ofile:
            json_string = ofile.read()
            if len(json_string) > 0:
                json_dictionary = json.JSONDECODER().decode(json_string)
            for key, value in json_dictionary.items():
                FileStorage.__objects[key] = value
