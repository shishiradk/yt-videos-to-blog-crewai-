from dotenv import load_dotenv
import os

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["CHROMA_OPENAI_API_KEY"] = os.getenv("CHROMA_OPENAI_API_KEY")

from crewai_tools import YoutubeChannelSearchTool

# Use a valid channel ID URL
yt_tool = YoutubeChannelSearchTool(
    youtube_channel_handle='https://www.youtube.com/channel/UCn-3f8tw_E1jZvhuHatROwA'
)
