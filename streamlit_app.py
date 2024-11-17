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
    'X-Authorization': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImtqbVlNWThEV2VOU1lKZmZSSjFXNSJ9.eyJuaWNrbmFtZSI6ImFudWphLnNpbmdoIiwibmFtZSI6ImFudWphLnNpbmdoQG5leHRkYy5jb20iLCJwaWN0dXJlIjoiaHR0cHM6Ly9zLmdyYXZhdGFyLmNvbS9hdmF0YXIvZTllYmJmYjdkM2FlZjU2NWI1NjZhZTlmM2ZmNWU0OWY_cz00ODAmcj1wZyZkPWh0dHBzJTNBJTJGJTJGY2RuLmF1dGgwLmNvbSUyRmF2YXRhcnMlMkZhbi5wbmciLCJ1cGRhdGVkX2F0IjoiMjAyNC0xMS0xMlQyMjowNjoyNC42NzJaIiwiZW1haWwiOiJhbnVqYS5zaW5naEBuZXh0ZGMuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImlzcyI6Imh0dHBzOi8vYXV0aC5vcmtlcy5pby8iLCJhdWQiOiJNeUhKWXVUc3FOTDhEYUxJR3dvdTZmU2F4ekYzVEZyVyIsImlhdCI6MTczMTQ0OTE4NiwiZXhwIjoxNzMxNDg1MTg2LCJzdWIiOiJhdXRoMHw2NzMzMDYwNmY5OGFkMmNjMjFmODFkYzMiLCJzaWQiOiJ0Z0FwVkpweFVzRm41WDlRMVFiR1lYSUNzQ1M5a0VEcyIsIm5vbmNlIjoiVTNCbFRpNUNabUV3T0ZwK01tcFBSVVJtZFhobFR5MUJTa0p6YlhJeFpUSXVjazFwU0hsbWNqQllMUT09In0.jAf6d2N8OFfKRpqjfPFDE1rZpc-UBrpa3pmfQK_7OGbbd7z4hlxf6G_KL5YjvMQQvXQqDmzrUebCeex7aPSKgA-3YTZm3MibAKn_I130De-GdWD_UtRNuICMTDapiPIzTnQhk1UBEhgl6WSTW0gOSsM-JMNhFgoE5zv9o2i5DEcpLoYQjZ99NSesCRJYXwa5NpyTBrepp6UBnwnWDwfm6jE5rk4utBFOBTEs6y35uKdBe6h5go6Jjbt5oadYWt_lUSp7BFI01UkxtHhZBDBVYsYUyLanE6jNpKeBzre9I-M7QhVXLamTp8YqypbLMsdX_wyaXrmdghA0FGZBa_v0hQ',
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

