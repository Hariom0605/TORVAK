from core.memory_manager import process_memory

while True:

    prompt = input("You : ")

    if prompt.lower() == "exit":
        break

    response = process_memory(prompt)

    print("TORVAK :", response)