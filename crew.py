from crewai import Crew, Process
from agents import blog_researcher, blog_writer
from tasks import research_task, write_task

# Forming the tech-focused crew
crew = Crew(
    agents=[blog_researcher, blog_writer],
    tasks=[research_task, write_task],
    process=Process.sequential,  # Sequential execution
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew=True
)

# Start the task execution
result = crew.kickoff(inputs={'topic': "ChatGPT Cryptocurrency by Robinhood! What is it, and what does it mean?"})
print(result)
