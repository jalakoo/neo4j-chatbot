from dataclasses import dataclass
from neo4j import GraphDatabase

@dataclass
class Driver:
    def __init__(self, uri:str, user:str, password:str):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))

    # Experimental query
    def execute_query(self, query, params={}):
        # Returns a tuple of records, summary, keys
        records, summary, keys =  self._driver.execute_query(query, params)
        # Only interested in list of result records
        return records
        
    def close(self):
        # Don't forget to close the driver connection when you are finished
        # with it
        self._driver.close()

