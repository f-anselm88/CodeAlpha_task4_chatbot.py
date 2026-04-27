"""
Task 4: Basic Rule-Based Chatbot
Internship: CodeAlpha -- Python Programming
Author: Anselm Munango
Description: A console chatbot that matches user input against predefined
             keyword rules and returns contextual responses.
             Demonstrates if-elif logic, functions, loops, and I/O.
"""

import random


# -- Response rules ------------------------------------------------------------
# Each rule maps a tuple of trigger keywords to a list of possible responses.
# A response is selected at random from the matching rule's list.

RULES = [
    (
        ("hello", "hi", "hey", "howdy", "greetings"),
        [
            "Hi there! How can I assist you today?",
            "Hello! What is on your mind?",
            "Hey! I am here and ready to help.",
        ],
    ),
    (
        ("how are you", "how are u", "what's up", "whats up", "how do you do"),
        [
            "I am doing great, thanks for asking! How about you?",
            "All systems running fine. What can I help you with?",
            "Running well! How are you doing today?",
        ],
    ),
    (
        ("i'm fine", "im fine", "i am fine", "i'm good", "im good", "i am good", "doing well"),
        [
            "Glad to hear it! What can I help you with?",
            "That is great to know. Feel free to ask me anything.",
            "Good to hear. How can I assist you today?",
        ],
    ),
    (
        ("your name", "who are you", "what are you", "what is your name"),
        [
            "I am AlphaBot, your Python-powered assistant built for CodeAlpha.",
            "You can call me AlphaBot. I was built in Python as part of the CodeAlpha internship.",
        ],
    ),
    (
        ("what can you do", "help", "capabilities", "features"),
        [
            "I can hold a conversation, answer simple questions, and respond to greetings and farewells. Try asking me something!",
            "I am a rule-based chatbot. Ask me anything and I will do my best to respond.",
        ],
    ),
    (
        ("joke", "funny", "make me laugh", "tell me a joke"),
        [
            "Why do programmers prefer dark mode? Because light attracts bugs.",
            "What did the Python developer say to the Java developer? You have too many brackets.",
            "Why was the developer broke? Because they used up all their cache.",
        ],
    ),
    (
        ("time", "date", "what day", "what time"),
        [
            "I do not have access to a live clock, but your system time is just a glance away.",
        ],
    ),
    (
        ("thank you", "thanks", "thx", "ty", "appreciate"),
        [
            "You are very welcome!",
            "Happy to help. Let me know if you need anything else.",
            "Anytime. That is what I am here for.",
        ],
    ),
    (
        ("bye", "goodbye", "exit", "quit", "see you", "later", "farewell"),
        [
            "Goodbye! Have a great day.",
            "See you next time. Take care.",
            "Farewell. It was great chatting with you.",
        ],
    ),
]

FAREWELL_TRIGGERS = {"bye", "goodbye", "exit", "quit", "see you", "later", "farewell"}

DEFAULT_RESPONSES = [
    "I am not sure I understand. Could you rephrase that?",
    "Interesting! I am still learning. Could you ask that differently?",
    "I do not have a great answer for that yet. Try asking something else.",
]


# -- Core matching logic -------------------------------------------------------
def get_response(user_input):
    """
    Match the normalized user input against the rule set.

    Returns a tuple of (response_string, is_farewell).
    """
    normalized = user_input.lower().strip()

    for triggers, responses in RULES:
        if any(trigger in normalized for trigger in triggers):
            is_farewell = any(t in normalized for t in FAREWELL_TRIGGERS)
            return random.choice(responses), is_farewell

    return random.choice(DEFAULT_RESPONSES), False


# -- Main loop -----------------------------------------------------------------
def run_chatbot():
    print("\n" + "=" * 50)
    print("          AlphaBot -- CodeAlpha Chatbot")
    print("=" * 50)
    print("  Type a message and press Enter to chat.")
    print("  Say 'bye' or 'quit' to end the session.")
    print("=" * 50 + "\n")

    while True:
        try:
            user_input = input("You:      ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nAlphaBot: Session interrupted. Goodbye.")
            break

        if not user_input:
            print("AlphaBot: It looks like you did not type anything. Go ahead!\n")
            continue

        response, is_farewell = get_response(user_input)
        print("AlphaBot: {}\n".format(response))

        if is_farewell:
            break

    print("=" * 50)
    print("  Chat session ended. Thanks for using AlphaBot.")
    print("=" * 50)


# -- Entry point ---------------------------------------------------------------
def main():
    run_chatbot()


if __name__ == "__main__":
    main()
