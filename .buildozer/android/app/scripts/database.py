import os
import sqlite3

# Database Connection
def connect():
    return sqlite3.connect('scripts/lasersandfeelings.db')

def close():
    conn = connect()
    conn.close()

def check_db():
    if not os.path.exists('scripts/lasersandfeelings.db'):
        conn = connect()
        conn.close()
        Player.create_player_table()
        Player.create_player_notes_table()
        Ship.create_ship_table()
        Ship.create_ship_notes_table()

class Player:
    def create_player_table():
        conn = connect()
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS player
                    (id INTEGER PRIMARY KEY, name TEXT, style TEXT, role TEXT, goal TEXT, number INTEGER)''')
        conn.commit()
        conn.close()

    def create_player_notes_table():
        conn = connect()
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS player_notes
                    (id INTEGER PRIMARY KEY, player_id INTEGER, notes TEXT,
                    FOREIGN KEY(player_id) REFERENCES player(id))''')
        conn.commit()
        conn.close()
    
    def insert_player(name, style, role, goal, number):
        conn = connect()
        c = conn.cursor()
        c.execute("INSERT INTO player (name, style, role, goal, number) VALUES (?, ?, ?, ?, ?)", (name, style, role, goal, number))
        conn.commit()
        conn.close()

    def insert_player_notes(player_id, notes):
        conn = connect()
        c = conn.cursor()
        c.execute("INSERT INTO player_notes (player_id, notes) VALUES (?, ?)", (player_id, notes))
        conn.commit()
        conn.close()
    
    def get_players():
        conn = connect()
        c = conn.cursor()
        c.execute("SELECT * FROM player")
        players = c.fetchall()
        conn.close()
        return players

    def get_latest_player_note(player_id):
        conn = connect()
        c = conn.cursor()
        c.execute("SELECT notes FROM player_notes WHERE player_id = ? ORDER BY id DESC LIMIT 1", (player_id,))
        note = c.fetchone()
        conn.close()
        return note[0] if note else ""


class Ship:
    @staticmethod
    def create_ship_table():
        conn = connect()
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS ship (
                    ship_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    strength_one TEXT NOT NULL,
                    strength_two TEXT NOT NULL,
                    problem TEXT NOT NULL
                )''')
        conn.commit()
        conn.close()

    @staticmethod
    def create_ship_notes_table():
        conn = connect()
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS ship_notes
                    (id INTEGER PRIMARY KEY, ship_id INTEGER, notes TEXT, datetime TEXT,
                    FOREIGN KEY(ship_id) REFERENCES ship(ship_id))''')
        conn.commit()
        conn.close()
    
    @staticmethod
    def insert_ship(name, strength_one, strength_two, problem):
        conn = connect()
        c = conn.cursor()
        c.execute("INSERT INTO ship (name, strength_one, strength_two, problem) VALUES (?, ?, ?, ?)", (name, strength_one, strength_two, problem))
        ship_id = c.lastrowid
        conn.commit()
        conn.close()
        return ship_id

    @staticmethod
    def get_ships():
        conn = connect()
        c = conn.cursor()
        c.execute('''SELECT ship.ship_id, ship.name, ship.strength_one, ship.strength_two, ship.problem, 
                            (SELECT notes FROM ship_notes WHERE ship_id = ship.ship_id ORDER BY id DESC LIMIT 1) as latest_note
                     FROM ship''')
        ships = c.fetchall()
        conn.close()
        return ships

    @staticmethod
    def insert_ship_notes(ship_id, notes):
        from datetime import datetime
        conn = connect()
        c = conn.cursor()
        datetime_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        c.execute("INSERT INTO ship_notes (ship_id, notes, datetime) VALUES (?, ?, ?)", (ship_id, notes, datetime_now))
        conn.commit()
        conn.close()

    @staticmethod
    def get_latest_ship_notes(ship_id):
        conn = connect()
        c = conn.cursor()
        c.execute("SELECT notes FROM ship_notes WHERE ship_id = ? ORDER BY id DESC LIMIT 1", (ship_id,))
        note = c.fetchone()
        conn.close()
        return note[0] if note else ""

    @staticmethod
    def get_all_ship_notes(ship_id):
        conn = connect()
        c = conn.cursor()
        c.execute("SELECT notes, datetime FROM ship_notes WHERE ship_id = ? ORDER BY id DESC", (ship_id,))
        notes = [(note[0], note[1]) for note in c.fetchall()]
        conn.close()
        return notes
