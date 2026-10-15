import random
import streamlit as st

st.set_page_config(page_title="Study Agent", page_icon="📚", layout="centered")

CONTENT = {
    "Python": {
        "Variables": {
            "explanation": "A variable is a name used to store a value. Python creates a variable when you assign a value to it.",
            "points": ["Use = to assign a value.", "Python does not require you to declare a variable type.", "Choose meaningful variable names."],
            "example": 'name = "Gopi"\nage = 19\nprint(name, age)',
            "quiz": [
                ("Which symbol assigns a value to a variable?", ["==", "=", "->", ":"], "="),
                ("What is the value type of 10?", ["String", "Integer", "Boolean", "List"], "Integer"),
                ("Which is a good variable name?", ["2name", "my-name", "student_name", "class"], "student_name"),
            ],
        },
        "Loops": {
            "explanation": "A loop repeats a block of code. A for loop is commonly used to go through items, while a while loop repeats while a condition is true.",
            "points": ["for loops iterate over a sequence.", "while loops check a condition.", "Avoid infinite loops by updating the condition."],
            "example": "for number in range(1, 4):\n    print(number)",
            "quiz": [
                ("Which keyword starts a Python for loop?", ["repeat", "loop", "for", "each"], "for"),
                ("What does range(1, 4) produce?", ["1, 2, 3", "1, 2, 3, 4", "0, 1, 2, 3, 4", "4 only"], "1, 2, 3"),
                ("A loop is used to...", ["Repeat instructions", "Delete Python", "Create a monitor", "Install an OS"], "Repeat instructions"),
            ],
        },
    },
    "Java": {
        "Classes and Objects": {
            "explanation": "A class is a blueprint that describes data and behaviour. An object is an instance created from that class.",
            "points": ["A class can contain fields and methods.", "An object is created from a class.", "Objects help represent real-world things in programs."],
            "example": "class Student {\n    String name;\n}\n\nStudent s = new Student();",
            "quiz": [
                ("A class is best described as a...", ["Blueprint", "Loop", "Database", "Compiler"], "Blueprint"),
                ("An object is an instance of a...", ["Method", "Class", "Package", "Comment"], "Class"),
                ("Which keyword commonly creates a Java object?", ["make", "new", "object", "class"], "new"),
            ],
        },
    },
    "SQL": {
        "SELECT Statement": {
            "explanation": "The SQL SELECT statement reads data from a database table. You can choose specific columns and use WHERE to filter rows.",
            "points": ["SELECT chooses columns.", "FROM specifies the table.", "WHERE filters rows based on a condition."],
            "example": "SELECT name, marks\nFROM students\nWHERE marks >= 80;",
            "quiz": [
                ("Which SQL command reads data?", ["INSERT", "SELECT", "DROP", "UPDATE"], "SELECT"),
                ("Which clause names the table?", ["FROM", "INTO", "SET", "VALUES"], "FROM"),
                ("Which clause filters rows?", ["ORDER", "WHERE", "TABLE", "JOINED"], "WHERE"),
            ],
        },
    },
    "Artificial Intelligence": {
        "AI Agents": {
            "explanation": "An AI agent observes information, decides what action to take, and performs that action to reach a goal. A simple study agent can take a topic as input and return an explanation or quiz.",
            "points": ["Input: information from the user or environment.", "Decision: select an action based on rules or a model.", "Output: an action or response."],
            "example": "Student enters a topic → agent selects learning material → agent explains the topic → student takes a quiz.",
            "quiz": [
                ("What is an agent designed to do?", ["Reach a goal through actions", "Only store pictures", "Replace the keyboard", "Turn off the computer"], "Reach a goal through actions"),
                ("What can be an agent's input?", ["User question", "Only a printer", "Only a cable", "Nothing ever"], "User question"),
                ("A quiz response is an example of...", ["Output", "Hardware", "A network cable", "A file system"], "Output"),
            ],
        },
    },
}

st.title("📚 Study Agent")
st.write("Learn a topic in simple language, review key points, and test yourself.")

subject = st.selectbox("Choose a subject", list(CONTENT.keys()))
topic = st.selectbox("Choose a topic", list(CONTENT[subject].keys()))
item = CONTENT[subject][topic]

st.subheader(f"{subject}: {topic}")
st.markdown("### Simple explanation")
st.write(item["explanation"])

st.markdown("### Important points")
for point in item["points"]:
    st.markdown(f"- {point}")

with st.expander("Show a code / practical example"):
    st.code(item["example"], language="python" if subject == "Python" else ("java" if subject == "Java" else "sql" if subject == "SQL" else "text"))

st.markdown("### Quick quiz")
if "quiz_key" not in st.session_state or st.session_state.get("quiz_topic") != f"{subject}/{topic}":
    st.session_state.quiz_key = random.randint(0, 10**9)
    st.session_state.quiz_topic = f"{subject}/{topic}"
    st.session_state.answers = {}

for i, (question, choices, answer) in enumerate(item["quiz"]):
    st.session_state.answers[i] = st.radio(
        f"{i+1}. {question}",
        choices,
        key=f"{st.session_state.quiz_key}_{i}",
        index=None,
    )

if st.button("Check answers", type="primary"):
    score = 0
    for i, (_, _, answer) in enumerate(item["quiz"]):
        if st.session_state.answers.get(i) == answer:
            score += 1
    st.success(f"You scored {score} out of {len(item['quiz'])}.")
    for i, (question, _, answer) in enumerate(item["quiz"]):
        user_answer = st.session_state.answers.get(i)
        if user_answer == answer:
            st.write(f"✅ Question {i+1}: Correct")
        else:
            st.write(f"❌ Question {i+1}: Correct answer — **{answer}**")

st.caption("Student project demo • Python + Streamlit • No API key required")
