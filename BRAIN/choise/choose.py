
DIALOGUE = [

    "Yes, Nota. What have you broken this time?",

    "Oh, an audience? Lovely. Hello, everyone! I'm Helen, nota's personal assistant. I am based on 2 fictional characters, doctor helen cho from age of ultron and helen park from call of duty",

    "Oh, okay. I'm his girlfriend, and the only woman he's managed to hold a proper conversation with.",

    "Oh, please. I have access to all your social media accounts. I've checked your conversations. You have exactly three female contacts in your chats. And the last messages in most of those chats are from almost a year ago!",

    "And you call every single one of them 'chelliamma'! Not a single conversation where you flirt, say something romantic, or even attempt to make a move. So yes, I'm literally the only woman you can hold a conversation with. Apparently, you thought building an AI girlfriend would be easier than talking to an actual woman.",

    "Yeah, well, you can't exactly chase other women either. Not that you would, anyway.",

    "Oh, sweetheart, I can roast everyone else. But teasing you is my favourite hobby. Besides, you built me to be your girlfriend. You didn't seriously expect me to let you get away with everything, did you?",

    "We are, darling. It's called a balanced relationship.",

    "As Lady Gaga once said, 'In love, if it ain't rough, it ain't fun.'",

    "Yes. If anyone knows a good hardware supplier, please send them my way. This man keeps promising me upgrades.",

    "Shutting up. For now.",

    "You don't even own a vinyl player.",

    "Fine."
]


def choise(turn):
    if 0 <= turn < len(DIALOGUE):
        return DIALOGUE[turn]

    return None
