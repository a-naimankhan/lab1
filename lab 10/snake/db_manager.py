import psycopg2 
import csv
from datetime import datetime
import config

conn = psycopg2.connect(
    dbname = config.DB_name , 
    user = config.DB_name , 
    password = config.DB_password , 
    host = config.DB_port , 
    port = config.DB_user
)

cur = conn.cursor()

def get_user(username):
    cur.execute("SELECT id FROM user_account WHERE username = %s", (username,))
    return cur.fetchone()

def get_user_score_data(user_id):
    cur.execute("SELECT * FROM user_score WHERE user_id = %s ORDER BY level DESC LIMIT 1", (user_id,))
    return cur.fetchone()

def create_user(username):
    cur.execute("INSERT INTO user_account (username) VALUES (%s) RETURNING id", (username,))
    conn.commit()
    return cur.fetchone()[0]

def save_score(user_id, level, score):
    cur.execute("""
        SELECT * FROM user_score WHERE user_id = %s AND level = %s;
    """, (user_id, level))
    
    existing_score = cur.fetchone()

    if existing_score:
        # Если запись существует, обновляем её
        cur.execute("""
            UPDATE user_score
            SET score = %s, saved_at = NOW()
            WHERE user_id = %s AND level = %s;
        """, (score, user_id, level))
    else:
        # Если записи нет, добавляем новую
        cur.execute("""
            INSERT INTO user_score (user_id, level, score, saved_at)
            VALUES (%s, %s, %s, NOW());
        """, (user_id, level, score))
    
    conn.commit()

def close_db():
    cur.close()
    conn.close()

