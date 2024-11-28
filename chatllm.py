from flask import Flask, request, jsonify, send_from_directory
import google.generativeai as genai
import os
from flask_cors import CORS  # Import CORS to handle cross-origin requests

app = Flask(__name__)
CORS(app)

# Configure the model with your API key
genai.configure(api_key="AIzaSyA_VwOY4Bc7e3UOm0i_LBjdsGrkASLkSxY")
model = genai.GenerativeModel("gemini-1.5-flash")

# Define the path to your HTML file
fd = r"E:/Rohit_BMS/3rd SEM/Hackathons" 

@app.route('/')
def index():
    # Serve the ChatWindow1.html file from the specified directory
    return send_from_directory(fd, 'ninjappa .html')

@app.route('/get_response', methods=['POST'])

def get_response():
    user_input = request.json.get('message')

    if user_input:
        try:
            # Generate the AI response
            response = model.generate_content(user_input)
            print(f"Generated Response: {response.text}")  # Log the AI response to the console
            return jsonify({'response': response.text})
        except Exception as e:
            print(f"Error: {str(e)}")  # Log any errors
            return jsonify({'response': f'Error: {str(e)}'})
    return jsonify({'response': 'Error: No input provided.'})

if __name__ == '__main__':
    app.run(debug=True)
