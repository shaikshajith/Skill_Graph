from neo4j import GraphDatabase

from app.config import (
    COGNODB_URI,
    COGNODB_USERNAME,
    COGNODB_PASSWORD,
    validate_config,
)


class Database:
    """Handles all communication with CognoDB."""

    def __init__(self):
        validate_config()

        self.driver = GraphDatabase.driver(
            COGNODB_URI,
            auth=(COGNODB_USERNAME, COGNODB_PASSWORD)
        )

    def verify_connection(self):
        """Verify that the application can connect to CognoDB."""
        self.driver.verify_connectivity()

    def execute_query(self, query, parameters=None):
        """Execute a Cypher query and return the results."""
        if parameters is None:
            parameters = {}

        with self.driver.session() as session:
            result = session.run(query, parameters)
            return result.data()

    def close(self):
        """Close the database driver."""
        self.driver.close()