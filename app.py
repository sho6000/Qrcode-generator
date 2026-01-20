import streamlit as st
import qrcode
import pymongo
import os
from io import BytesIO

DB_USER = os.getenv("MONGO_USERNAME")
DB_PASS = os.getenv("MONGO_PASSWORD")
DB_HOST = "mongodb"  

try:
    connection_url = f"mongodb://{DB_USER}:{DB_PASS}@{DB_HOST}:27017/"
    client = pymongo.MongoClient(connection_url, serverSelectionTimeoutMS=5000)
    db = client["qr_database"]
    collection = db["history"]
    
    client.server_info() 
except Exception as e:
    st.error(f"Could not connect to MongoDB: {e}")


st.title("QR Code Generator with MongoDB")

url_input = st.text_input("Enter Link:", placeholder="https://github.com/sho6000/Qrcode-generator")

if st.button("Generate & Save"):
    if url_input:
        
        qr = qrcode.make(url_input)
        buf = BytesIO()
        qr.save(buf, format="PNG")
        st.image(buf.getvalue(), caption="Generated QR Code")

       
        try:
            collection.insert_one({"url": url_input})
            st.success(f"Link '{url_input}' saved to database!")
        except Exception as e:
            st.error(f"Failed to save to database: {e}")

if st.checkbox("Show Database History"):
    st.subheader("Last 5 Entries")
    try:
        entries = collection.find().sort("_id", -1).limit(5)
        for entry in entries:
            st.write(f"- {entry['url']}")
    except Exception as e:
        st.write("No data found or connection issue.")