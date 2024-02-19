from typing import Final
from os import path, getenv
from json import load, JSONDecodeError
from requests import get
from urllib.parse import urlparse, unquote
from discord import Intents, Client, Message
from dotenv import load_dotenv

def get_settings() -> dict:
    try:
        with open('settings.json', 'r') as file:
            return load(file)
    except FileNotFoundError:
        print("settings.json file not found.")
    except JSONDecodeError:
        print("Error decoding JSON from settings.json.")

def download_image(image_url, download_path, rename_images, username):
    parsed_url = urlparse(image_url)
    url_path = unquote(parsed_url.path)
    filename = path.basename(url_path)

    if rename_images:
        parts = filename.split('_')
        if len(parts) > 2:
            new_filename = '_'.join(parts[1:-1])
        else:
            new_filename = '_'.join(parts)
    else:
        new_filename = f"{filename}_{username}"

    counter = 1
    file_extension = path.splitext(filename)[1]
    file_path = path.join(download_path, f"{new_filename}{str(counter).zfill(2)}{file_extension}")

    while path.exists(file_path):
        counter += 1
        file_path = path.join(download_path, f"{new_filename}_{str(counter).zfill(2)}{file_extension}")

    response = get(image_url)
    if response.status_code == 200:
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print(f"Image downloaded to {file_path}")
    else:
        print(f"Failed to download image. Status code: {response.status_code}")

load_dotenv()
TOKEN: Final[str] = getenv('DISCORD_TOKEN')
print(TOKEN)

intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)

@client.event
async def on_ready() -> None:
    print(f"{client.user} is now running!")

@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return

    settings = get_settings()
    download_path = settings['download_path']
    rename_images = settings['rename_images']

    if "Midjourney Bot" in message.author.name and any(trigger in message.content for trigger in ["Image #1", "Image #2", "Image #3", "Image #4", "Upscaled (Subtle)", "Upscaled (Creative)"]):
        for attachment in message.attachments:
            image_url = attachment.url
            download_image(image_url, download_path, rename_images, str(message.author))

def main() -> None:
    client.run(TOKEN)

if __name__ == '__main__':
    main()