from telethon import TelegramClient
import asyncio

# Replace with your own values
api_id = 28428735
api_hash = 'f9fd0dd9c29450c34d81da1fcf14b102'
group_id = -1002641361364  # Group ID (target chat)
topic_id = 1178              # Topic ID (message_thread_id)

client = TelegramClient('session_name', api_id, api_hash)

async def main():
    await client.start()

    print(f"Deleting messages in topic ID {topic_id} from chat {group_id}...")

    async for message in client.iter_messages(group_id, reply_to=topic_id):
        try:
            await client.delete_messages(group_id, message.id)
            print(f"Deleted message ID: {message.id}")
        except Exception as e:
            print(f"Failed to delete message ID {message.id}: {e}")

    print("✅ Done.")

asyncio.run(main())
