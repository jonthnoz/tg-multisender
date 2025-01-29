# Send Telegram Messages Using Google Colab

This project allows you to send messages to Telegram users using a Python script. You can run the script in Google Colab, which is a free online Jupyter notebook environment that requires no installation.

## Prerequisites

1. **Google Account**: You need a Google account to access Google Colab.
2. **Telegram API Credentials**: You need to create a Telegram application to get your `api_id` and `api_hash`. You can do this by visiting [my.telegram.org](https://my.telegram.org/apps).

## Files Required

-   `send_message.py`: The Python script that sends messages.
-   `message.txt`: A text file containing the message you want to send.
-   `usernames.txt`: A text file containing the usernames of the recipients (one username per line).

## Using Google Colab

For your convenience, a Google Colab notebook has been set up to run this script without needing to install anything locally. You can access the notebook here:

[Google Colab Notebook](https://colab.research.google.com/drive/1mseP5syXhzy5SFD6Xz6PZcCDFS-9oymk?usp=sharing)

### Steps to Use the Notebook

1. **Open the Notebook**: Click on the link above to open the Google Colab notebook.
2. **Upload Required Files**: In the left sidebar, click on the folder icon to open the file explorer. Upload the `message.txt` and `usernames.txt` files.
3. **Install Required Libraries**: The notebook will include a cell to install the necessary libraries (`telethon` and `nest_asyncio`).
4. **Set Up Your Credentials**: Follow the instructions in the notebook to enter your Telegram API credentials.
5. **Run the Script**: Execute the code cells in the notebook to authenticate your Telegram account and send messages to the specified users. Click the play button at the top left of each cell, from the top to the bottom, to run the code.

## Creating Your Own Google Colab Notebook

If you prefer to create your own Google Colab notebook, follow these steps:

1. **Open Google Colab**: Go to [Google Colab](https://colab.research.google.com/).
2. **Create a New Notebook**: Click on `File` > `New Notebook`.
3. **Rename the Notebook**: Click on the title (usually "Untitled0.ipynb") at the top and rename it to something meaningful, like "Telegram Message Sender".
4. **Install Required Libraries**: In the first cell, run the following code to install the necessary libraries:
    ```python
    !pip install telethon
    !pip install nest_asyncio
    ```
5. **Copy the Script**: In a new cell, copy and paste the contents of `send_message.py` into the cell. Make sure to replace the placeholders for `api_id`, `api_hash`, and `phone_number` with your actual credentials.
6. **Upload Required Files**: In the left sidebar, click on the folder icon to open the file explorer. Click on the upload icon (the paper with an arrow) to upload the `message.txt` and `usernames.txt` files.
7. **Run the Script**: Execute the code cells in the notebook to authenticate your Telegram account and send messages to the specified users.

## Important Notes

-   Make sure to replace `YOUR_API_ID`, `YOUR_API_HASH`, and `YOUR_PHONE_NUMBER` with your actual Telegram API credentials.
-   The first time you run the script, it will prompt you to enter a code sent to your Telegram account for authentication.
-   **Two-Factor Authentication**: If you have two-factor authentication (2FA) enabled on your Telegram account, you will need to enter your password after entering the code sent to your phone.
-   **Session File**: The session file will be created after successful authentication. This file allows you to avoid re-entering your credentials in future runs.

## Conclusion

You can now send messages to Telegram users using this script in Google Colab. If you have any questions or issues, feel free to reach out for help.
