import json

from pymongo import MongoClient


class DBClient:
    """Client data base

    This class includes the database access methods. It shall
    The functionalities of creation, editing, deletion of the documents of each collection shall be covered.
    of the documents of each collection shall be covered.

    Attributes:
        client (MongoClient): pymongo library client to access the database.
        to the database.

    Args:
        url (str): MongoDB database address.
        database_name (str): Interaction database name
        mongo_user (str): User name for authentication in the database
                          the database
        mongo_pass (str): Password of the user in the database.
        mongo_authdb (str): Name of the authentication database
    """
    def __init__(self, url, database_name, mongo_user, mongo_pass, 
                 mongo_authdb, port=27017):
        self.client = MongoClient(host=url,
                                  port=port,
                                  username=mongo_user,
                                  password=mongo_pass,
                                  authSource=mongo_authdb)
        self.database = database_name

    def createDatabase(self, name):
        database = self.client[name]
        return database

    def clean_collection(self, collection):
        """
        Deletes all documents in the specified collection.

        Args:
            collection (str): Name of the collection to which all documents will be deleted.
                              all documents will be deleted.

        Returns:
            Boolean: True if the collection has been successfully emptied.
                     False if the collection does not exist.
        """
        self.client[self.database][collection].drop()

    def find_one(self, collection, query, mongoID=False):
        """
        Checks if the document exists in our database and
        returns a query with the document data if it is found.
        found. Only the first occurrence of 'find_one' is searched.

        Args:
            collection (str): Name of the collection on which the 'find_one' will be performed.
                              find_one' will be performed
            query (dict): contains the query query in the collection.
                          E.g., {"username": "defense"}
            mongoID (bool): Evaluation of whether we want to obtain the
                            mongo identifier for each of the
                            elements found

        Returns:
            dictionary: Dictionary containing the query information for each search.
                         query for each search.
                         Returns "None" if the searched query
                         does not exist in our database.
        """

        if mongoID is False:
            result = self.client[self.database][collection].find_one(
                query,
                {"_id": 0}
            )
        elif mongoID is True:
            result = self.client[self.database][collection].find_one(
                query
            )
        else:
            raise ValueError("Expected mongoID as True or False")

        return result

    def find(self, collection, query, mongoID=False):
        """
        Checks if there are documents in our database that meet the query conditions
        that meet the conditions of the query and returns a query with the
        query with the document data if found.
        All documents matching the query 'find' are searched.

        Args:
            collection (str): Name of the collection on which the 'find' will be performed.
                              find' will be performed
            query (dict): contains the query query in the collection.
                          E.g.,
                              {
                              {'date': {
                                  '$gte': '2020-21-10',
                                  '$lt': '2020-30-11', '$lt': '2020-30-11', }}
                               }}
            mongoID (bool): Evaluation of whether we want to obtain the
                            mongo identifier for each of the
                            elements found

        Returns:
            list: List of products (each in a dictionary) that meet the search requirements.
                   the search requirements.
        """
        if mongoID is False:
            filtered_products_cursor = self.client[self.database][collection].find(
                                                                query, {"_id": 0})
        elif mongoID is True:
            filtered_products_cursor = self.client[self.database][collection].find(
                                                                query)
        else:
            raise ValueError("Expected mongoID as True or False")

        return list(filtered_products_cursor)
    
    def insert_one(self, collection, new_document):
        """
        Adds a new document to the specified collection

        Args:
            collection (str): Name of the collection on which the 'find_one' will be performed.
                              find_one' will be performed
            new_document (dict): contains the new document to be inserted into find
                                 the collection. E.g., {"username": "defence"}

        returns:
            dictionary: dictionary containing the result of the insertion
                         with the 'inserted_id' field indicating the ID of the new inserted document.
                         of the new inserted document.
        """
        result = self.client[self.database][collection].insert_one(new_document)

        return result

    def insert_many(self, collection, new_documents):
        """
        Adds multiple documents to the specified collection

        Args:
            collection (str): Name of the collection on which the 'find_one' will be performed.
                              find_one' will be performed
            new_documents (list(dict)): contains the list of new documents to be inserted.
                                        documents to be inserted.
                                        E.g., [{"username": "defensa"},
                                               {"username": "defence2"}]]

        Returns:
            InsertManyResult: List of the _ids of the inserted documents.
        """
        result = self.client[self.database][collection].insert_many(new_documents)

        return result

    def update_one(self, collection, query, update, operator = "set"):
        """
        Updates a new document to the specified collection.

        Args:
            collection (str): Name of the collection on which the 'find_one' will be performed.
                              find_one' will be performed
            query (dict): contains the query query in the collection.
                          E.g., {'providerId': _id}
            update (dict): contains the information to update in the collection.
                            E.g., {'metadata.EPSG': EPSG}

        Returns:
            Instance of the UpdateResult class.
        """
        result = self.client[self.database][collection].update_one(query, { "$" + operator:update}, upsert=False)

        return result

    def update_many(self, collection, query, update):
        """
        Updates multiple documents to the specified collection.

        Args:
            collection (str): Name of the collection on which the 'find_one' will be performed.
                              find_one' will be performed
            query (dict): contains the query query on the collection.
                          E.g., {'providerId': _id}
            update (dict): contains the information to update in the collection.
                            E.g., {'metadata.EPSG': EPSG}

        Returns:
            Instance of the UpdateResult class.
        """
        result = self.client[self.database][collection].update_many(query, {"$set":update}, upsert=False)

        return result

    def delete_one(self, collection, query):
        """
        Deletes a document from the specified collection.

        Args:
            collection (str): Name of the collection on which the 'delete_one' is to be performed.
                              delete_one' will be performed
            query (dict): contains the query query in the collection.
                          E.g., {'providerId': _id}

        Returns:
            Instance of the DeleteResult class.
        """
        result = self.client[self.database][collection].delete_one(query)

        return result

    def delete_field(self, collection, query, field):
        """
        Removes a given field from a Pymongo document (both key and value).
        key and value).

        Args:
            collection (str): Name of the collection on which the 'delete_field' will be
                              delete_field' will be performed
            query (dict): Contains the query query in the collection.
            field (str): Relative address within the document of the field
                         we want to delete.
        
        Returns:
            Instance of the UpdateResult class
        """
        result = self.client[self.database][collection].update_one(query,
                                                                   {"$unset": {field: None}},
                                                                   upsert=False)
    
        return result