import asyncio
import nest_asyncio
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError

# Apply nest_asyncio to allow nested event loops
nest_asyncio.apply()

# Replace these with your own values
api_id = 'YOUR_API_ID'  # Replace with your API ID
api_hash = 'YOUR_API_HASH'  # Replace with your API Hash
phone_number = 'YOUR_PHONE_NUMBER'  # Replace with your phone number

# Read usernames and message from files
def read_usernames(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def read_message(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()

async def main():
    # Create the client and connect
    client = TelegramClient('session_name', api_id, api_hash)

    await client.start()

    # Check if the user needs to enter a password
    if not await client.is_user_authorized():
        try:
            await client.send_code_request(phone_number)
            code = input('Enter the code you received: ')
            await client.sign_in(phone_number, code)
        except SessionPasswordNeededError:
            password = input('Enter your password: ')
            await client.sign_in(password=password)

    # Read usernames and message
    usernames = read_usernames('usernames.txt')
    message = read_message('message.txt')

    # Send the message to each user
    for username in usernames:
        try:
            await client.send_message(username, message)
            print(f'Message sent to {username}')
        except Exception as e:
            print(f'Failed to send message to {username}: {e}')

    await client.disconnect()

# Run the main function
if __name__ == '__main__':
    asyncio.run(main())