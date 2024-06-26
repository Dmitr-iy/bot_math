import psycopg2
import logging
from data.config import config_settings


def execute_query(query, params=None, fetch_all=True):
    conn = None
    cursor = None
    result = None
    try:
        conn = psycopg2.connect(
            dbname=config_settings.db_name,
            user=config_settings.db_user,
            password=config_settings.db_password.get_secret_value(),
            host=config_settings.db_host
        )
        cursor = conn.cursor()
        cursor.execute(query, params)
        if fetch_all:
            result = cursor.fetchall()
        else:
            result = cursor.fetchone()
    except Exception as e:
        logging.error(f"Error executing SQL query: {e}", exc_info=True)
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
    return result
