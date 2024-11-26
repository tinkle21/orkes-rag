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
    'X-Authorization': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImtqbVlNWThEV2VOU1lKZmZSSjFXNSJ9.eyJuaWNrbmFtZSI6ImFudWphLnNpbmdoIiwibmFtZSI6ImFudWphLnNpbmdoQG5leHRkYy5jb20iLCJwaWN0dXJlIjoiaHR0cHM6Ly9zLmdyYXZhdGFyLmNvbS9hdmF0YXIvZTllYmJmYjdkM2FlZjU2NWI1NjZhZTlmM2ZmNWU0OWY_cz00ODAmcj1wZyZkPWh0dHBzJTNBJTJGJTJGY2RuLmF1dGgwLmNvbSUyRmF2YXRhcnMlMkZhbi5wbmciLCJ1cGRhdGVkX2F0IjoiMjAyNC0xMS0yNFQyMzo0ODoyNC40NzZaIiwiZW1haWwiOiJhbnVqYS5zaW5naEBuZXh0ZGMuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImlzcyI6Imh0dHBzOi8vYXV0aC5vcmtlcy5pby8iLCJhdWQiOiJNeUhKWXVUc3FOTDhEYUxJR3dvdTZmU2F4ekYzVEZyVyIsImlhdCI6MTczMjU5MzA0MiwiZXhwIjoxNzMyNjI5MDQyLCJzdWIiOiJhdXRoMHw2NzMzMDYwNmY5OGFkMmNjMjFmODFkYzMiLCJzaWQiOiJiQW9rNGd2b042aXlVemxqUkNaaVJDU0FYbGthbFpjeSIsIm5vbmNlIjoiWVd0a01uZEdMbHBKWkdOSFMydDBPWEZ5UVhsRVkzRTVVRTAxUW41blVqTlVTWEo2VWtScU0xODFYdz09In0.I7f_wXA5zT9NFEqfDrYvVYw-K_YpROsZblA1qLw7cq6onbtb81i0Iv0xmQLIp7hkqV6YCYEqbfp18kxFpyetb7kk6176TiybtIecPaC7-R6IPbgCkMEB5Tq2MIfePZbsmIz9HT5tUPJMQq_Wr3XRewxABdXZLD5Wve5IbA_eO_z3GaW-Ef0VzOzZCE-NZmP0rg7hNT8hU_kzNQtE7xp6jYIguNGzYmCWz6PN6hxVyCeJXD6_UrB-m3P6x0chz2dfuLMbOc8Y0qXtWZsJaf5yWWHWfLFy8dx2xDVWDUQxYMyFeQr20bMTy14JCSJpN9OOmgGGB7euWfwqEtA4lkatfg',
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

