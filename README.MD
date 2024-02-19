# Midjourney upscaled image downloader bot

This Discord bot automatically downloads images posted by Midjourney Bot in Discord channels and saves them to a specified directory. It can also rename the images based on predefined settings.

## Features

- **Automatic Image Download**: Downloads upscaled images posted by Midjourney bot in Discord channels.
- **Customizable Download Path**: Allows setting a custom path where images will be saved.
- **Image Renaming**: Option to rename downloaded images for better organization. Omitting the username and the long string of 
numbers and text at the end of the filename.

## Prerequisites

Before you start using this bot, make sure you have the following installed:

- Python 3.8 or higher
- `discord.py` library
- `python-dotenv` library

## Setup

1. **Clone the Repository**

   ```
   git clone https://github.com/R1nex1/MidjourneyImgUpscaleBot.git
   cd midjourney-img-upscale-bot
   ```

2. **Install Dependencies**

   ```
   pip install -r requirements.txt
   ```

### 3. Create a Discord Bot Account

- Navigate to the [Discord Developer Portal](https://discord.com/developers/applications).
- Click on the "New Application" button, give it a name, and create your application.
- Go to the "Bot" tab, then click "Add Bot".
- Give bot permissions to Read Messages/View Channels and Read Message History.
- Invite the Midjourney Bot and your own bot to a Discord server using the generated invite link.
- Under the "TOKEN" section, click "Copy" to copy your bot's token.



4. **Configure Environment Variables**
   - Open `.env.example` and replace `YOUR_BOT_TOKEN_HERE` with your bot's token.
   - Rename `.env.example` to `.env`.

5. **Set Up `settings.json`**

   - Modify `settings.json` with your preferred download path and rename settings:
     ```json
     {
       "download_path": "C:\\Users\\YourUsername\\Downloads",
       "rename_images": true
     }
     ```


6. **Run the Bot**

   ```
   python main.py
   ```

## Usage

Once the bot is running and invited to your server, it will automatically start downloading upscaled images posted by Midjourney Bot in any of the channels it has access to.

## Customization

- **Download Path**: Change the `download_path` in `settings.json` to your preferred location.
- **Renaming Images**: Set `rename_images` to `true` in `settings.json` if you want the bot to rename the downloaded images.


## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you have suggestions or encounter any problems.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the `discord.py` team for the fantastic library.
- This bot was inspired by the need to automate upscaled image downloads by Midjourney bot.

---

**Note**: This bot is intended for personal use and should be used in compliance with Discord's Terms of Service. Always respect privacy and copyright laws when downloading and sharing images.