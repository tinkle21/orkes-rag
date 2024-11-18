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
    'X-Authorization': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImtqbVlNWThEV2VOU1lKZmZSSjFXNSJ9.eyJuaWNrbmFtZSI6ImFudWphLnNpbmdoIiwibmFtZSI6ImFudWphLnNpbmdoQG5leHRkYy5jb20iLCJwaWN0dXJlIjoiaHR0cHM6Ly9zLmdyYXZhdGFyLmNvbS9hdmF0YXIvZTllYmJmYjdkM2FlZjU2NWI1NjZhZTlmM2ZmNWU0OWY_cz00ODAmcj1wZyZkPWh0dHBzJTNBJTJGJTJGY2RuLmF1dGgwLmNvbSUyRmF2YXRhcnMlMkZhbi5wbmciLCJ1cGRhdGVkX2F0IjoiMjAyNC0xMS0xN1QyMzoxODo1Ni4zMTdaIiwiZW1haWwiOiJhbnVqYS5zaW5naEBuZXh0ZGMuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImlzcyI6Imh0dHBzOi8vYXV0aC5vcmtlcy5pby8iLCJhdWQiOiJNeUhKWXVUc3FOTDhEYUxJR3dvdTZmU2F4ekYzVEZyVyIsImlhdCI6MTczMTg4NTUzOCwiZXhwIjoxNzMxOTIxNTM4LCJzdWIiOiJhdXRoMHw2NzMzMDYwNmY5OGFkMmNjMjFmODFkYzMiLCJzaWQiOiJOMXlBZ2hIMWhINWRQUjJkSjB2a1JTZXJ4Wm84N0pRZiIsIm5vbmNlIjoiTVVGdlYzTkxZV1ZJVDNaZk4yMDFUazVIZGtKU09VcFdhVzlQY0hsNVZGSXdaMGx0TUVoUmMyTTVlQT09In0.oqIgTrcUx21gOFLWn1vs9LfwzWPPqJFD3_Am4bzVf2k9Yt7Lhm9AAPdKhWChJvyBv2YLWHKMWuZ7uKyVdBfWob-dueCVxMGGg60ikSoVIkJilQPFmnFDCVMdZoLtNFl0sUCB6fMCkwIONtuImWocPlbO7DM8b95Na2B1vkB78H1djTsiloS-L-Nh8ENppRyXfG6LElNikkta4kk3mIOoGkHr0DuIL_AYkuwaFxZ6Mmi_C5s0o7Ox1BhhBhbzHIy009oE-MIKYcL0P6vBy-hRaevi4t2YKKMb8AFXiaeGLkWzhc7DkH5jQEfFBtGDZexvrewOFPqplhKLTKxbxDwqTg',
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

