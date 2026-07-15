from core.memory_engine import MemoryEngine

memory = MemoryEngine()

memory.save_profile("name", "Hariom")
memory.save_profile("city", "Jaipur")

memory.save_preference("language", "Python")
memory.save_preference("theme", "Dark")

memory.add_fact("I know C++")
memory.add_fact("I use VS Code")

memory.add_project("TORVAK")

memory.add_task("Finish Memory Module")

memory.add_goal("Become AI Engineer")

print(memory.load())