import sqlite3 as sql
from pathlib import Path
from typing import List, Tuple

db_file = Path("database/rizla.db")

try:
    if not db_file.exists():
        db_file.parent.mkdir(parents=True, exist_ok=True)
        db_file.touch()

    with sql.connect(str(db_file)) as conn:
        cursor = conn.cursor()

        tables: List[Tuple[str]] = [
            """CREATE TABLE IF NOT EXISTS nations (
                 discord_id INT PRIMARY KEY,
                 nation_id INT,
                 nation_name TEXT,
                 leader_name TEXT,
                 continent TEXT,
                 alliance_name TEXT,
                 alliance_link TEXT,
                 color TEXT,
                 cities INT,
                 infrastructure INT,
                 vacation_mode INT,
                 beige_turns INT,
                 war_policy TEXT,
                 domestic_policy TEXT,
                 score FLOAT,
                 last_active DATETIME,
                 soldiers INT,
                 tanks INT,
                 aircrafts INT,
                 ships INT,
                 missiles INT,
                 nukes INT,
                 offensive_wars INT,
                 defensive_wars INT
                 )""",
            """CREATE TABLE IF NOT EXISTS alliances (
                 alliance_id INT,
                 alliance_name TEXT,
                 acronym TEXT,
                 score FLOAT,
                 color TEXT,
                 members INT,
                 average_score FLOAT,
                 treaties TEXT,
                 flag TEXT,
                 forum_link TEXT,
                 discord_link TEXT,
                 wiki_link TEXT
                 )""",
            """CREATE TABLE IF NOT EXISTS registered (
                 discord_id INT PRIMARY KEY,
                 nation_id INT,
                 nation_name TEXT,
                 leader_name TEXT,
                 continent TEXT,
                 alliance_name TEXT,
                 alliance_link TEXT,
                 color TEXT,
                 cities INT,
                 vacation_mode INT,
                 beige_turns INT,
                 war_policy TEXT,
                 domestic_policy TEXT,
                 score FLOAT,
                 last_active DATETIME,
                 soldiers INT,
                 tanks INT,
                 aircrafts INT,
                 ships INT,
                 missiles INT,
                 nukes INT,
                 offensive_wars INT,
                 defensive_wars INT 
                 )""",
            """CREATE TABLE IF NOT EXISTS raid (
                 nation_id INT,
                 nation_name TEXT,
                 alliance_name TEXT,
                 alliance_link TEXT,
                 color TEXT,
                 cities INT,
                 vacation_mode INT,
                 beige_turns INT,
                 score FLOAT,
                 last_active DATETIME,
                 soldiers INT,
                 tanks INT,
                 aircrafts INT,
                 ships INT,
                 missiles INT,
                 nukes INT,
                 defensive_wars INT,
                 loot_value TEXT 
                 )""",
            """CREATE TABLE IF NOT EXISTS loot (
                 attacker_id INT,
                 attacker_name TEXT,
                 defender_id INT,
                 defender_name TEXT,
                 loot_info TEXT
                 )""",
            """CREATE TABLE IF NOT EXISTS trade (
                 highest_bid INT,
                 lowest_big INT,
                 margin INT
                 )""",
            """CREATE TABLE IF NOT EXISTS prices (
                 money INT,
                 food INT,
                 aluminum INT,
                 steel INT,
                 munitions INT,
                 gasoline INT,
                 bauxite INT,
                 iron INT,
                 lead INT,
                 uranium INT,
                 oil INT,
                 coal INT,
                 credits INT
                 )""",
        ]

        for table in tables:
            cursor.execute(table)

        conn.commit()

except sql.Error as e:
    print(f"Error while working with SQLite: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")

finally:
    conn.close()
