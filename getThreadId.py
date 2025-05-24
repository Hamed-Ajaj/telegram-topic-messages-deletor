from telethon import TelegramClient, types
import asyncio

api_id = 28428735
api_hash = 'f9fd0dd9c29450c34d81da1fcf14b102'

client = TelegramClient('session', api_id, api_hash)

async def main():
    await client.start()

    # Replace with your channel invite link or username
    channel = await client.get_entity("https://t.me/+pMmNhru2O8I4OGE8")

    print(f"Channel: {channel.title}\nListing topic (thread) IDs:")

    async for message in client.iter_messages(channel, limit=100):
        # Filter MessageService type messages only
        if isinstance(message, types.MessageService) and isinstance(message.action, types.MessageActionTopicCreated):
            topic_id = message.id
            topic_title = message.action.title
            print(f"- Topic title: {topic_title} → thread_id: {topic_id}")

asyncio.run(main())
