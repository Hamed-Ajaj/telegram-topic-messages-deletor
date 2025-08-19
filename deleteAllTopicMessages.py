from telethon import TelegramClient
import asyncio

# NOTE: also check the README file

api_id = # api ID from https://my.telegram.org
api_hash = # api ID and hash from https://my.telegram.org
group_id = # grup or channel ID to delete messages from
topic_id =  # Topic ID to delete messages from

client = TelegramClient('session_name', api_id, api_hash)

async def main():
    await client.start()
    print(f"Deleting messages from topic {topic_id} in chat {group_id}...")

    deleted_count = 0

    async for message in client.iter_messages(group_id, reply_to=topic_id):
        try:
            await client.delete_messages(group_id, message.id)
            print(f"Deleted message ID: {message.id}")
            deleted_count += 1
            await asyncio.sleep(0.5)  # small delay to avoid rate limits
        except Exception as e:
            print(f"Error deleting message {message.id}: {e}")
            await asyncio.sleep(2)  # wait longer if error

    print(f"✅ Done. Total deleted: {deleted_count}")

asyncio.run(main())
