import streamlit as st
import qrcode
import psycopg2
import os
from io import BytesIO

# PostgreSQL Environment Variables
DB_USER = os.getenv("POSTGRES_USER")
DB_PASS = os.getenv("POSTGRES_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("POSTGRES_DB")
def get_connection():
    return psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        host=DB_HOST,
        port=DB_PORT
    )

# Initialize Database Table
try:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS qr_history (
            id SERIAL PRIMARY KEY,
            url TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)
    conn.commit()
    cur.close()
    conn.close()
except Exception as e:
    st.error(f"Could not connect to PostgreSQL: {e}")

st.title("QR Code Generator with PostgreSQL")

url_input = st.text_input("Enter Link:", placeholder="https://github.com/sho6000/Qrcode-generator")

if st.button("Generate & Save"):
    if url_input:
        # Generate QR Code
        qr = qrcode.make(url_input)
        buf = BytesIO()
        qr.save(buf, format="PNG")
        st.image(buf.getvalue(), caption="Generated QR Code")
        
        # Save to PostgreSQL
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("INSERT INTO qr_history (url) VALUES (%s)", (url_input,))
            conn.commit()
            cur.close()
            conn.close()
            st.success(f"Link '{url_input}' saved to database!")
        except Exception as e:
            st.error(f"Failed to save to database: {e}")

if st.checkbox("Show Database History"):
    st.subheader("Last 5 Entries")
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT url FROM qr_history ORDER BY id DESC LIMIT 5")
        entries = cur.fetchall()
        for entry in entries:
            st.write(f"- {entry[0]}")
        cur.close()
        conn.close()
    except Exception as e:
        st.write("No data found or connection issue.")