from Student import question

question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]
obj = [
question("a", question_prompts[0]),
question("c", question_prompts[1]),
question("b", question_prompts[2])
]


def check(question):
    score = 0
    for question in question:
        question.prompt = input(question.prompt)
        if question.prompt == question.answer:
            score += 1
    return score

print(f"Score: {check(obj)}/ 3")

question1 = question("a", question_prompts[1])
print(question1.test())