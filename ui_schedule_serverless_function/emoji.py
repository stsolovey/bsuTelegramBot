import random

def random_smileys():
    emoji = ['😀','😃','😄','😁','😆','😅','🤣','😂','🙂','😉',
     '😊','😇','🥰','😍','🤩','😘','😗','😚','😙','🥲',
     '😏', '😌','😋','😛','😜','🤪','😝','🤗','🤭','🫢',
     '🫣','🤫','🤔','🫡','🤤','🤠','🥳','🥸','😎','🤓','🧐']
    return random.choice(emoji)

def random_upside_down():
    emoji = ['🙃','🫠','🤐','🤨','😐','😑','😶',
     '🫥','😶‍🌫️','😒','🙄','😬', '😮‍💨' ,'🤥']
    return random.choice(emoji)

def random_negative():
    emoji = ['😕','🫤','😟','🙁','☹️','😮',
             '😯','😲','😳','🥺','🥹','😦',
             '😧','😨','😰','😥','😢','😭',
             '😱','😖','😣','😞','😓','😩',
             '😫','😤','😡','😠','🤬','👿']
    return random.choice(emoji)

def random_negative_funny():
    emoji = ['😈', '👿', '💀', '☠️', '🤡', 
             '👹', '👺', '👻', '👽', '👾',
             '🙀', '😿', '😾', '🙈',
             '🙉', '🙊']
    return random.choice(emoji)

def random_positive():
    emoji = ['🥀','🤗','👼','☀️','💃',
             '🤪','✨','🌞','💫','🥰',
             '😍','🤩','😘','😺','😸', 
             '😹','😻','😼','😽','🤖']
    return random.choice(emoji)

def random_notification():
    emoji = ['🛎️','🚨','🔔',
             '⏰','🔔','🔊',
             '🔔','🔔','🔔']
    return random.choice(emoji)

def random_schedule():
    emoji = ['📜','🗒️','📃','📇',
             '🗓️','📅','📝','📑',
             '📋','🧾','📄',]
    return random.choice(emoji)

def random_settings():
    emoji = ['⚙️','🔩','⚒️','🪚',
             '🛠️','⛏️','🔨','🪛',
             '🔧','⛓️', '⚙️','⚙️',
             '⚙️','⚙️']
    return random.choice(emoji)

def random_teacher():
    emoji = ['🦈','🐊','🦖','🦅',
             '🧑🏻‍🏫','🧑🏼‍🏫','👨🏻‍🏫','👩🏻‍🏫',
             '👨🏼‍🏫','👩🏼‍🏫','👨🏻‍💻','👨🏼‍💻',
             '👴🏼','👨🏼','👨🏻‍🚀','👨🏼‍🚀']
    return random.choice(emoji)

def random_current_week():
    emoji = ['🏊🏻','🌊','🏄🏻','🐳']
    return random.choice(emoji)