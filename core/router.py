from core.memory.manager import MemoryManager
from core.coding_engine import CodingEngine


class AIRouter:

    def __init__(self, ai_engine):

        self.ai = ai_engine
        self.coder = CodingEngine()
        self.memory = MemoryManager()

    def route(self, prompt):

        text = prompt.lower()

        # ====================================
        # MEMORY
        # ====================================

        memory_results = self.memory.remember(prompt)

        if memory_results:
            names = [m.content for m in memory_results]
            return f"Got it. I'll remember: {', '.join(names)}."

        # Check for memory queries
        if any(phrase in text for phrase in ["what is my name", "where do i live", "what are my projects", "what are my goals", "what do you know about me"]):
            relevant = self.memory.get_relevant_memories(prompt, top_k=5)
            if relevant:
                lines = [f"{m.memory_type.value.upper()}: {m.content}" for m in relevant]
                return "\n".join(lines) if lines else "I don't know."

        # ====================================
        # CODING MODE
        # ====================================

        coding_prefix = {

            "write",
            "create",
            "generate",
            "build",
            "make",
            "develop",
            "fix",
            "debug",
            "optimize",
            "convert",
            "explain"

        }

        coding_words = {

            # Languages
            "python", "java", "c", "c++", "c#",
            "go", "golang", "rust", "swift",
            "kotlin", "scala", "ruby", "perl",
            "php", "r", "dart", "lua",
            "haskell", "erlang", "elixir",
            "fortran", "cobol", "pascal",
            "ada", "assembly",

            # Web
            "html", "css", "javascript",
            "typescript", "node", "nodejs",
            "express", "react", "nextjs",
            "vue", "angular", "svelte",
            "jquery", "bootstrap",
            "tailwind",

            # Python
            "django", "flask", "fastapi",
            "streamlit", "gradio",
            "tkinter", "pyside", "pyqt",

            # Java
            "spring", "springboot",
            "hibernate", "maven", "gradle",

            # Mobile
            "android", "ios", "flutter",
            "react native",

            # Database
            "sql", "mysql", "postgres",
            "postgresql", "sqlite",
            "mongodb", "redis",
            "firebase", "supabase",

            # AI
            "tensorflow", "keras",
            "pytorch", "langchain",
            "huggingface", "transformers",
            "ollama", "gemini",
            "llm",

            # DevOps
            "docker", "kubernetes",
            "terraform", "ansible",

            # Cloud
            "aws", "azure", "gcp",

            # Data
            "numpy", "pandas",
            "matplotlib", "opencv",

            # Generic
            "api",
            "graphql",
            "algorithm",
            "dsa",
            "leetcode",
            "bug",
            "error",
            "debug",
            "code",
            "coding",
            "program",
            "project",
            "function",
            "class",
            "object",
            "oop",
            "backend",
            "frontend",
            "fullstack"

        }

        has_prefix = any(word in text for word in coding_prefix)
        has_tech = any(word in text for word in coding_words)

        if has_prefix and has_tech:
            return self.coder.chat(prompt)

        # ====================================
        # GENERAL AI
        # ====================================

        return self.ai.chat(prompt)