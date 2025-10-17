# YouTube-to-Blog with CrewAI

A Python project that uses **CrewAI** to automatically generate blog posts from YouTube videos.

## Features
- **Blog Researcher Agent**: Finds relevant videos on a YouTube channel for a given topic.
- **Blog Writer Agent**: Creates structured, engaging blog content from video transcriptions.
- **Sequential Task Execution**: Research → Writing.
- **YouTube Channel Integration**: Supports channel URLs and IDs.
- **Embeddings & Memory**: Uses Chroma + OpenAI embeddings for content storage and retrieval.
- **Markdown Output**: Saves generated blog posts to `.md` files.

## Folder Structure
yt-videos-to-blog-crewai/
│
├── agents.py # Defines blog_researcher and blog_writer agents
├── crew.py # Main script to run the crew workflow
├── tasks.py # Defines research_task and write_task
├── tools.py # YouTube search tool configuration
├── .env # Environment variables (API keys)
└── requirements.txt # Python dependencies

markdown
Copy code

## Requirements
- Python 3.10+
- Libraries: `crewai`, `crewai_tools`, `chroma`, `openai`, `pytube`, `python-dotenv`

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/yt-videos-to-blog-crewai.git
   cd yt-videos-to-blog-crewai

## Create a .env file with your API keys:

```bash
OPENAI_API_KEY=your_openai_api_key
CHROMA_OPENAI_API_KEY=your_chroma_openai_api_key
```

```bash
pip install -r requirements.txt
```

```python
yt_tool = YoutubeChannelSearchTool(
    youtube_channel_handle='https://www.youtube.com/channel/UCn-3f8tw_E1jZvhuHatROwA'
)
```
```python
result = crew.kickoff(inputs={'topic': 'Your Topic Here'})
Usage
```

```bash
python crew.py
Output blog will be saved as new-blog-post.md.
```

##Notes
Make sure your OpenAI quota is sufficient; embedding video transcripts consumes tokens.

If no videos are found, refine your topic keywords.

Ensure .env variables are correctly set for OpenAI and Chroma APIs.

License
MIT License

Copy code
