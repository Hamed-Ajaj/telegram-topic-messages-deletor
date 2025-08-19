# Telegram Topic Messages Deletor

A Python script to delete all messages from a specific topic in a Telegram supergroup. This script uses the [Telethon](https://github.com/LonamiWebs/Telethon) library to interact with the Telegram API.

---

## Features
- Deletes all messages from a specific topic in a Telegram supergroup.
- Handles rate limits gracefully.
- Provides error handling for failed deletions.

---

## Prerequisites
Before using this script, ensure you have the following installed:
1. **Python** (version 3.7 or higher)
2. **pip** (Python package manager)

### Installing Python and pip
#### On Ubuntu/Debian:
```bash
sudo apt update
sudo apt install python3 python3-pip -y
```

#### On macOS:
```bash
brew install python
```

#### On Windows:
1. Download Python from the [official website](https://www.python.org/).
2. During installation, ensure you check the box **"Add Python to PATH"**.
3. pip is included with Python, so no additional installation is needed.

---

## Installation and Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/Hamed-Ajaj/telegram-topic-messages-deletor.git
   ```

2. Navigate to the project directory:
   ```bash
   cd telegram-topic-messages-deletor
   ```

3. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

4. Install the required dependencies:
   ```bash
   pip install telethon
   ```

5. Configure the script:
   - Open `deleteAllTopicMessages.py` in a text editor.
   - Replace the placeholders for `api_id`, `api_hash`, `group_id`, and `topic_id` with your own values:
     ```python
     api_id = YOUR_API_ID
     api_hash = 'YOUR_API_HASH'
     group_id = -100XXXXXXXXXX  # Replace with your group ID
     topic_id = 12345  # Replace with your topic ID
     ```

6. Run the script:
   ```bash
   python deleteAllTopicMessages.py
   ```

---

## How to Get Your API ID and Hash
1. Go to [my.telegram.org](https://my.telegram.org/).
2. Log in with your Telegram account.
3. Navigate to **API Development Tools**.
4. Create a new application and note down the `api_id` and `api_hash`.

---

## How to Get the Group ID and Topic ID
1. Use the `get_dialogs` or `get_topics` method in Telethon to fetch the group and topic IDs.
2. Refer to the script in the repository for an example of how to list topics in a group.

---

## Notes
- Ensure the bot has the necessary permissions to delete messages in the group and the specific topic.
- This script is designed for **supergroups** with topics enabled.
- Be mindful of Telegram's rate limits when deleting a large number of messages.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
