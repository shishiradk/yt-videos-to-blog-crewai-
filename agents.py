from crewai import Agent
from tools import yt_tool


# Create a senior bllog content researcher

blog_researcher=Agent(
    role='BLOG RESEARCHER FROM YOUTUBE VIDEOS ',
    goal='get the relavent video content for the topic {topic} from the yt channel',
    verbose=True,
    backstory=(
        "Expert in undrstanding videos in AI Data Science ,  Machine Learning And GEN AI and providing suggestion "
    ),
    tool=[],
    allow_delegation=True
)

##creting a senior blog writer agent with YT tool

blog_writer=Agent(
    role='Blog Writer',
    goal='Narrate compelling tech stories about the videos {topic} form YT channel',
    verbose=True,
    backstory=(
        "With a flair for simplifying topics,  you craft"
        "engaging narratives that captivate and educate , bringing new "
        "discoveries to light in an accessible manner."
    ),
    toll=[],
    allow_delegation=True
)