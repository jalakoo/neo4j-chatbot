from dataclasses import dataclass
from neo4j import GraphDatabase

@dataclass
class Driver:
    def __init__(self, uri:str, user:str, password:str):
        self.uri = uri
        self.user = user
        self.password = password

    # Experimental query
    def execute_query(self, query, params={}):
        # Returns a tuple of records, summary, keys
        with GraphDatabase.driver(self.uri, auth=(self.user, self.password)) as driver:
            records, summary, keys =  driver.execute_query(query, params)
            # Only interested in list of result records
            return records

