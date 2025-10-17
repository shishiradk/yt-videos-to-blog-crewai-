from crewai import Task
from tools import yt_tool
from agents import blog_researcher, blog_writer

# Research Task
research_task = Task(
    description=(
        "Identify the video about {topic}. "
        "Get detailed information about the video from the YouTube channel."
    ),
    expected_output="A comprehensive 3-paragraph report based on the {topic} video content.",
    tools=[yt_tool],
    agent=blog_researcher,
)

# Writing Task
write_task = Task(
    description=(
        "Use information from the YouTube channel on the topic {topic}."
    ),
    expected_output="Summarize and create a blog post based on the YouTube video for {topic}.",
    tools=[yt_tool],
    agent=blog_writer,
    async_execution=False,
    output_file="new-blog-post.md"
)
