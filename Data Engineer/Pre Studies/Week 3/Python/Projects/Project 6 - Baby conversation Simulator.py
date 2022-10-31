#! Python3

# Project 6 - Baby Conversation Simulator
# A small program simulating a conversation with a baby

# 8.49

# Importing necessary libraries
from random import choice

questions = [
    "Can I have meatballs?",
    "Where is the cat?",
    "Mommy?",
    "Why is the sky blue?"
]

question = choice(questions)

answer = input(question + ": ").strip().lower()

while answer != "just because":
    answer = input("Why?: ").strip().lower()

print("Oh... Okay")
