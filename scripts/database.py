import os
import sqlite3
from datetime import datetime

def connect():
    return sqlite3.connect('scripts/lasersandfeelings.db')

def check_db():
    # Checks if database exists, if not, calls methods that will create it.
    if not os.path.exists('scripts/lasersandfeelings.db'):
        conn = connect()
        conn.close()
        Player.create_player_table()
        Player.create_player_notes_table()
        Ship.create_ship_table()
        Ship.create_ship_notes_table()
        Ship.create_ship_players_table()

class Player:
    @staticmethod
    def create_player_table():
        conn = connect()
        c = conn.cursor()
        c.execute('''
                    CREATE TABLE IF NOT EXISTS player (
                        player_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        style TEXT NOT NULL,
                        role TEXT NOT NULL,
                        goal TEXT NOT NULL,
                        number INTEGER NOT NULL
                    )
                  ''')
        conn.commit()
        conn.close()

    @staticmethod
    def create_player_notes_table():
        conn = connect()
        c = conn.cursor()
        c.execute('''
                    CREATE TABLE IF NOT EXISTS player_notes (
                        journal_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        player_id INTEGER,
                        journal TEXT,
                        datetime TEXT,
                        FOREIGN KEY(player_id) REFERENCES player(player_id)
                    )
                  ''')
        conn.commit()
        conn.close()

    @staticmethod
    def insert_player(name, style, role, goal, number):
        conn = connect()
        c = conn.cursor()
        c.execute("INSERT INTO player (name, style, role, goal, number) VALUES (?, ?, ?, ?, ?)", (name, style, role, goal, number))
        player_id = c.lastrowid
        conn.commit()
        conn.close()
        return player_id

    @staticmethod
    def insert_player_notes(player_id, journal):
        conn = connect()
        c = conn.cursor()
        datetime_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        c.execute("INSERT INTO player_notes (player_id, journal, datetime) VALUES (?, ?, ?)", (player_id, journal, datetime_now))
        conn.commit()
        conn.close()

    @staticmethod
    def get_latest_player_note(player_id):
        conn = connect()
        c = conn.cursor()
        c.execute("SELECT journal, datetime FROM player_notes WHERE player_id = ? ORDER BY journal_id DESC LIMIT 1", (player_id,))
        note = c.fetchone()
        conn.close()
        if note:
            return f"{note[1]}: {note[0]}"
        return ""

    @staticmethod
    def get_characters():
        conn = connect()
        c = conn.cursor()
        c.execute("SELECT player.player_id, player.name, player.style, player.role, player.goal, player.number, player_notes.journal FROM player LEFT JOIN player_notes ON player.player_id = player_notes.player_id")
        characters = c.fetchall()
        conn.close()
        return characters

class Ship:
    @staticmethod
    def create_ship_table():
        conn = connect()
        c = conn.cursor()
        c.execute('''
                    CREATE TABLE IF NOT EXISTS ship (
                        ship_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        strength_one TEXT NOT NULL,
                        strength_two TEXT NOT NULL,
                        problem TEXT NOT NULL
                    )
                  ''')
        conn.commit()
        conn.close()

    @staticmethod
    def create_ship_notes_table():
        conn = connect()
        c = conn.cursor()
        c.execute('''
                    CREATE TABLE IF NOT EXISTS ship_notes (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        ship_id INTEGER,
                        notes TEXT,
                        datetime TEXT,
                        FOREIGN KEY(ship_id) REFERENCES ship(ship_id)
                    )
                  ''')
        conn.commit()
        conn.close()

    @staticmethod
    def create_ship_players_table():
        conn = connect()
        c = conn.cursor()
        c.execute('''
                    CREATE TABLE IF NOT EXISTS ship_players (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        ship_id INTEGER,
                        player_id INTEGER,
                        FOREIGN KEY(ship_id) REFERENCES ship(ship_id),
                        FOREIGN KEY(player_id) REFERENCES player(player_id)
                    )
                  ''')
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
    def insert_ship_notes(ship_id, notes):
        conn = connect()
        c = conn.cursor()
        datetime_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        c.execute("INSERT INTO ship_notes (ship_id, notes, datetime) VALUES (?, ?, ?)", (ship_id, notes, datetime_now))
        conn.commit()
        conn.close()

    @staticmethod
    def insert_ship_player(ship_id, player_id):
        conn = connect()
        c = conn.cursor()
        c.execute("INSERT INTO ship_players (ship_id, player_id) VALUES (?, ?)", (ship_id, player_id))
        conn.commit()
        conn.close()

    @staticmethod
    def get_ships():
        conn = connect()
        c = conn.cursor()
        c.execute("SELECT * FROM ship")
        ships = c.fetchall()
        conn.close()
        return ships

    @staticmethod
    def get_all_ship_notes(ship_id):
        conn = connect()
        c = conn.cursor()
        c.execute("SELECT notes, datetime FROM ship_notes WHERE ship_id = ? ORDER BY id DESC", (ship_id,))
        notes = c.fetchall()
        conn.close()
        return notes
