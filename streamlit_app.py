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
    'X-Authorization': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImtqbVlNWThEV2VOU1lKZmZSSjFXNSJ9.eyJuaWNrbmFtZSI6ImFudWphLnNpbmdoIiwibmFtZSI6ImFudWphLnNpbmdoQG5leHRkYy5jb20iLCJwaWN0dXJlIjoiaHR0cHM6Ly9zLmdyYXZhdGFyLmNvbS9hdmF0YXIvZTllYmJmYjdkM2FlZjU2NWI1NjZhZTlmM2ZmNWU0OWY_cz00ODAmcj1wZyZkPWh0dHBzJTNBJTJGJTJGY2RuLmF1dGgwLmNvbSUyRmF2YXRhcnMlMkZhbi5wbmciLCJ1cGRhdGVkX2F0IjoiMjAyNC0xMS0xOVQyMzo1OTo1MS45OTVaIiwiZW1haWwiOiJhbnVqYS5zaW5naEBuZXh0ZGMuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImlzcyI6Imh0dHBzOi8vYXV0aC5vcmtlcy5pby8iLCJhdWQiOiJNeUhKWXVUc3FOTDhEYUxJR3dvdTZmU2F4ekYzVEZyVyIsImlhdCI6MTczMjE0NDg4MCwiZXhwIjoxNzMyMTgwODgwLCJzdWIiOiJhdXRoMHw2NzMzMDYwNmY5OGFkMmNjMjFmODFkYzMiLCJzaWQiOiJsVkhOX1NYc1ZmcWc4dWpGV2ViSm1qaVQ5aFp3cVhDYiIsIm5vbmNlIjoiTWxGRlQzQnFmbEpMYW01SVZIaERWR3A1VkVWa2REUTNSVFI2YjJseVJUVm9SSEIyWVdNMVFWWjBhZz09In0.e46CGRxR7yktTcYvjORPzzFEPW5Ozw51NQwlhQ4_jCWCNRej2KCvJyklqQV0hVKomMEh6yuxRlyQwtWmOQAEFYwI0Xhl5OEse_cykGrwX0vzlzhNR3G2BVpGb62QXLCDzAHw0k65W159eBAYhxGMbWI-Gz1NFC-vPzpx_L8eHmshjiVfhytPogKA3eK2vEQ6bPt8szxo4w-O21CgyeDoX0fcSbQkwzpIzzvg7pss2OflhIwQL38yoSfS621lqeocX-Qz4GMP9dABnT6jU6x69AqPDdo_5d5RqU5nuHirXe0Hy404loG-hSbYMh7gD9D51Jq17nVQdJocyK7NciQqQw',
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

