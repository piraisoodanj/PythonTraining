from pymongo import MongoClient
import sqlite3

# MongoDB connection string
connection_string = r"mongodb+srv://pirai2011:3WnIucTSkOHlSYVa@cluster0.m1iht.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"


try:
    # MongoDB client setup
    client = MongoClient(connection_string,tlsAllowInvalidCertificates=True)
    print('connected to mongo atlas successfully')

    db = client["movies_db"] 
    collection = db["movies"]  

    # Fetch all movie data from MongoDB
    movies_data = collection.find()

    # SQLite database setup
    sqlite_db = "movies_local.db"  
    conn = sqlite3.connect(sqlite_db)
    cursor = conn.cursor()

    # Create a table in SQLite
    cursor.execute("""
    CREATE TABLE movies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        year INTEGER,
        director TEXT  
    )
    """)

    # Insert movie data into SQLite
    def insert_movie_into_sqlite(movie):
        cursor.execute("""
        INSERT INTO movies (title, year,director)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (
            movie.get('title'),
            movie.get('year'),
            movie.get('director')
        ))

    # Iterate 
    for movie in movies_data:
        insert_movie_into_sqlite(movie)

    conn.commit()
    conn.close()

    print("Data transfer from MongoDB to SQLite is complete.")

except Exception as e:
    print(e)
