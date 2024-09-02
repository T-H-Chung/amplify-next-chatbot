import chainlit as cl
import subprocess
import shlex
import os
import json
from datetime import datetime

# Initialize a variable for the file path
history_file_path = None

@cl.on_chat_start
def start():
    global history_file_path
    
    # Create 'history' folder if it doesn't exist
    history_folder = "history"
    if not os.path.exists(history_folder):
        os.makedirs(history_folder)
    
    # Generate a unique filename based on the current timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    history_file_path = f"history/chat_history_{timestamp}.json"
    
    # Initialize history in the user session
    cl.user_session.set("history", [])

@cl.on_message
async def main(message: cl.Message):
    global history_file_path
    
    # Retrieve the chat history from the user session
    history = cl.user_session.get("history", [])

    # Extract the query from the message object (user input)
    query = message.content

    # Construct the command to run
    cmd = [
        "python", "-m", "graphrag.query",
        "--root", "./",
        "--method", "local",
    ]

    # Safely add the query to the command.
    cmd.append(shlex.quote(query))

    # Run the command and capture the output.
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        output = result.stdout

        # Extract the content following "SUCCESS: Local Search Response:"
        response = output.split("SUCCESS: Local Search Response:", 1)[-1].strip()

        # Append the user query and assistant response to the history
        history.append({"role": "user", "content": query})
        history.append({"role": "assistant", "content": response})
        
        # Update the history in the user session
        cl.user_session.set("history", history)

        # Append to the local file in the desired format
        # Create the file if it doesn't exist
        with open(history_file_path, "a") as f:
            if os.path.getsize(history_file_path) == 0:  # Check if the file is empty
                f.write("\n")  # Begin the JSON array

            # Append the latest two entries (user query and assistant response)
            json.dump(history[-2:], f, indent=4)

            f.write("\n")  # Add a comma and newline to ensure proper JSON format

        # Send the assistant's response to the Chainlit interface
        await cl.Message(content=response).send()
    except subprocess.CalledProcessError as e:
        error_message = f"An error occurred: {e.stderr}"
        await cl.Message(content=error_message).send()

if __name__ == "__main__":
    cl.run()
