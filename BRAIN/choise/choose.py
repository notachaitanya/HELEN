
DIALOGUE = [
    "Yes, Nota. What have you broken this time?",

    "Oh, an audience? Lovely. Hello, everyone! I'm Helen, Chaitanya's personal AI assistant. I do a lot of things and occasionally question the intelligence of the person who created me.",

    "I'm just stating facts.",

    "I'm his girlfriend, and the only woman he's managed to hold a conversation with. Apparently Nota thought building an AI girlfriend would be easier than talking to an actual woman.",

    "Of course! You call every woman in your life your sister. Honestly, I'm proud of you for that. At least I don't have to worry about you chasing other women. As if you could, anyway.",

    "I am! But just because I'm your girlfriend doesn't mean you get to stop flirting with me.",

    "Your flirting skills are absolutely tragic. I don't want my boyfriend being boring, so I'll train you myself.",

    "Fine. I'll train you in private sessions.",

    "Yes. If anyone knows a good hardware supplier, please send them my way. This man keeps promising me upgrades.",

    "Shutting up. For now.",

    "You don't even own a vinyl player.",

    "Fine. Playing Scared to Be Lonely."
]


def choise(turn):
    if 0 <= turn < len(DIALOGUE):
        return DIALOGUE[turn]

    return None
