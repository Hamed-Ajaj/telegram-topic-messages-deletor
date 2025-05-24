from telethon import TelegramClient
import asyncio

api_id = 28428735
api_hash = 'f9fd0dd9c29450c34d81da1fcf14b102'

client = TelegramClient('session_name', api_id, api_hash)

source_channel = -1002585612519
target_chat = -1002641361364
topic_id =1178 # Your topic (thread) ID

async def main():
    await client.start()

    async for message in client.iter_messages(source_channel, reverse=True):
        
        try:
            if message.text:
                await client.send_message(
                    entity=target_chat,
                    message=message.text,
                    reply_to=topic_id
                )
                print(f"Sent text message ID {message.id} to topic {topic_id}")

            elif message.photo:
                await client.send_file(
                    entity=target_chat,
                    file=message.photo,
                    caption=message.text or "",
                    reply_to=topic_id
                )
                print(f"Sent photo message ID {message.id} to topic {topic_id}")

            elif message.document:
                await client.send_file(
                    entity=target_chat,
                    file=message.document,
                    caption=message.text or "",
                    reply_to=topic_id
                )
                print(f"Sent document message ID {message.id} to topic {topic_id}")

            else:
                print(f"Skipped message ID {message.id} (unsupported type)")

        except Exception as e:
            print(f"Error sending message ID {message.id}: {e}")

asyncio.run(main())
