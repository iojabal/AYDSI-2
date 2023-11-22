from pymongo import MongoClient


class MongoDBConnection:
    def __init__(self, host, port, username, password, database):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.database = database
        self.client = None

    def connect(self):
        try:
            self.client = MongoClient(
                host=self.host,
                port=self.port,
                username=self.username,
                password=self.password,
                authSource=self.database,
                authMechanism='SCRAM-SHA-256',
            )
            return self.client[self.database]
        except Exception as e:
            print(f"Error connecting to MongoDB: {str(e)}")

    def disconnect(self):
        try:
            if self.client:
                self.client.close()
                print("Disconnected from MongoDB.")
        except Exception as e:
            print(f"Error disconnecting from MongoDB: {str(e)}")
