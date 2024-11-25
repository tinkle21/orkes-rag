import os
import streamlit as st
import requests

st.title("AshBOT- Financial News Search")

query = st.text_input("Enter your search query:")

if st.button("Get Answer"):
  if query:
    workflow_name = "news-context-search"
    url = f"https://q4p1.orkescloud.io/api/workflow/execute/{workflow_name}?priority=0"
    # Set the headers
    headers = {
    'accept': 'text/plain',
    'X-Authorization': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImtqbVlNWThEV2VOU1lKZmZSSjFXNSJ9.eyJuaWNrbmFtZSI6ImFudWphLnNpbmdoIiwibmFtZSI6ImFudWphLnNpbmdoQG5leHRkYy5jb20iLCJwaWN0dXJlIjoiaHR0cHM6Ly9zLmdyYXZhdGFyLmNvbS9hdmF0YXIvZTllYmJmYjdkM2FlZjU2NWI1NjZhZTlmM2ZmNWU0OWY_cz00ODAmcj1wZyZkPWh0dHBzJTNBJTJGJTJGY2RuLmF1dGgwLmNvbSUyRmF2YXRhcnMlMkZhbi5wbmciLCJ1cGRhdGVkX2F0IjoiMjAyNC0xMS0yNFQyMzo0ODoyNC40NzZaIiwiZW1haWwiOiJhbnVqYS5zaW5naEBuZXh0ZGMuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImlzcyI6Imh0dHBzOi8vYXV0aC5vcmtlcy5pby8iLCJhdWQiOiJNeUhKWXVUc3FOTDhEYUxJR3dvdTZmU2F4ekYzVEZyVyIsImlhdCI6MTczMjQ5MjEwNiwiZXhwIjoxNzMyNTI4MTA2LCJzdWIiOiJhdXRoMHw2NzMzMDYwNmY5OGFkMmNjMjFmODFkYzMiLCJzaWQiOiJiQW9rNGd2b042aXlVemxqUkNaaVJDU0FYbGthbFpjeSIsIm5vbmNlIjoiYURsQ1JFUmlMVWxuUkdKUldFcElNRTFzYTBNeFpUaHRlRUpsTTBNdWFuSlpValV0UkV0RlpXRjRZZz09In0.O3wrR-a4mM9aFVEfkqZF_7Ui14VPYyMRc9MOuZX0RSq0JvW4eOJ2D-5phv1mR9_Md8f4xQGA5gctX5I2OL_fNzXmxBUn_t62Jki1Aj2bGYCBCvdWXOYkueGWAdq2I7B_9xaG9ZWh0fn-dvcXd5_wEktH_aePZLXk7tU7_WlMuUhLkhgbahscZwUcVoG8RCt4z_A_W-VuAICZBJiq1BMJQfZyh8kXq7N5CxP2KIk2kQPDN03tTtZwN8TZ57hqiSlHP4eqKYGzRh8jtUwtR-yWUTEhXZ-v5DnrqHP-PAYJ6PPwzilqqu2KwhAcTNJSb9qrAlGXbGQfeJrph_AWe1yV5g',
    'Content-Type': 'application/json'
    }
    payload = {"query": query}
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
      response_data = response.json()
      st.write("Response Result:", response_data.get('result', 'N/A'))
      print("Response:", response_data)
    else:
      st.write("Error:", response.status_code, response.text)
  else:
    st.write("Please enter a search query.")

