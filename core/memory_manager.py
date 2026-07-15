import re
from core.memory_engine import MemoryEngine

memory = MemoryEngine()


def process_memory(prompt):

    text = prompt.strip()

    # ---------- PROFILE ----------

    match = re.search(r"my name is (.+)", text, re.IGNORECASE)
    if match:
        name = match.group(1).strip()
        memory.save_profile("name", name)
        return f"Nice to meet you, {name}."

    match = re.search(r"i live in (.+)", text, re.IGNORECASE)
    if match:
        city = match.group(1).strip()
        memory.save_profile("city", city)
        return f"I'll remember that you live in {city}."

    match = re.search(r"i am (\d+) years old", text, re.IGNORECASE)
    if match:
        age = match.group(1)
        memory.save_profile("age", age)
        return "Got it."

    # ---------- PREFERENCES ----------

    match = re.search(r"i like (.+)", text, re.IGNORECASE)
    if match:
        like = match.group(1).strip()
        memory.add_fact(f"Likes {like}")
        return f"I'll remember that you like {like}."

    match = re.search(r"i prefer (.+)", text, re.IGNORECASE)
    if match:
        pref = match.group(1).strip()
        memory.save_preference("preferred", pref)
        return "Preference saved."

    # ---------- PROJECT ----------

    match = re.search(r"i am working on (.+)", text, re.IGNORECASE)
    if match:
        project = match.group(1).strip()
        memory.add_project(project)
        return f"Project '{project}' saved."

    # ---------- GOALS ----------

    match = re.search(r"my goal is (.+)", text, re.IGNORECASE)
    if match:
        goal = match.group(1).strip()
        memory.add_goal(goal)
        return "Goal saved."

    # ---------- TASK ----------

    match = re.search(r"remember to (.+)", text, re.IGNORECASE)
    if match:
        task = match.group(1).strip()
        memory.add_task(task)
        return "Task saved."

    # ---------- QUESTIONS ----------

    if "what is my name" in text.lower():
        name = memory.get_profile("name")
        return name if name else "I don't know your name."

    if "where do i live" in text.lower():
        city = memory.get_profile("city")
        return city if city else "I don't know."

    if "what are my projects" in text.lower():
        projects = memory.get_projects()
        return ", ".join(projects) if projects else "No projects."

    if "what are my goals" in text.lower():
        goals = memory.get_goals()
        return ", ".join(goals) if goals else "No goals."

    if "what do you know about me" in text.lower():

        data = memory.load()

        return f"""
PROFILE:
{data['profile']}

PREFERENCES:
{data['preferences']}

FACTS:
{data['facts']}

PROJECTS:
{data['projects']}

GOALS:
{data['goals']}

TASKS:
{data['tasks']}
"""

    return None