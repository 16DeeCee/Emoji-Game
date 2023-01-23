from pyfiglet import figlet_format

title = figlet_format("Emoji Game", font = "ogre")

commands = '''
Commands
\help : shows the list of commands
\hint : uses hint to help the player solve the word
\skip : skips the current word
\menu : Go back to the Main Menu
'''

menu = ''':open_book: :open_book: Main Menu :open_book: :open_book:
:video_game: Start Game
:page_with_curl: How to play
:cross_mark_button: Exit game
'''

rules = ''':page_with_curl: :page_with_curl: HOW TO PLAY :page_with_curl: :page_with_curl:
:joystick: Gameplay
Guess the word based on the emoji shown. Your answer must only contain letters.

:level_slider: Difficulty
Choose your desired difficulty.
Easy: It will show scrambled letters.
Hard: It will show only number of words and letters

:double_exclamation_mark: Hints
Use hints to give you an advantage in getting the correct answer.
Easy: Hint allows you to reshuffle the word.
Hard: Hint allows you to get a random letter.

:star: Stars
Earn stars for every correct answer!
Stars are needed to use hints.

''' + commands + '''

GOODLUCK!
'''

emoji_words = [
    {
    "Category": "Movie",
    "Emoji": "🦖 🎢  🦕",
    "Answer": "JURASSIC PARK",
    "Trivia": '''Did you know?
The first two films in the Jurassic Park franchise (Jurassic Park and The Lost World) are
both based on novels written by acclaimed sci-fi and techno-thriller author Michael Crichton'''
    },
    {
    "Category": "Disney Movie",
    "Emoji": "👸 ❄️ ⛄️",
    "Answer": "FROZEN",
    "Trivia": '''Did you know?
When the gates open during "For The First Time in Forever," there is a cameo of Rapunzel
and Eugene (Flynn) from Tangled (2010).'''
    },
    {
    "Category": "Disney Movie",
    "Emoji": "🧜 🐠  🦞",
    "Answer": "LITTLE MERMAID",
    "Trivia": '''Did you know?
Ariel is the first Disney princess to have biological siblings.'''
    },
    {
    "Category": "Disney Movie",
    "Emoji": "👩 🌹 👹",
    "Answer": "BEAUTY AND THE BEAST",
    "Trivia": '''Did you know?
In Beauty and the Beast (1991), the Beast's castle is shown to be quite close to the village, 
yet nobody in the village knew about it, nor noticed the absence of those who live there,
when they are cursed. The prologue of this version elaborates on this part of the story, 
explaining part of the curse involved the world forgetting about the castle and its inhabitants.
.'''
    },
    {
    "Category": "Horror Movie Baddies",
    "Emoji": "🏒 🎭 🔪  🏕",
    "Answer": "JASON VOORHEES",
    "Trivia": '''Did you know?
Friday the 13th earned $39,754,601 at the domestic box office on a budget of $550,000. Its
worldwide gross was $59,754,601.'''
    },
    {
    "Category": "Horror Movie Baddies",
    "Emoji": "😱 🔪",
    "Answer": "GHOSTFACE",
    "Trivia": '''Did you know?
While filming the harrowing opening scene in which Ghostface's first victim Casey gets
terrorised and slashed to ribbons, Drew Barrymore actually, though accidentally, called 911 
a number of times.'''
    },
    {
    "Category": "Horror Movie Baddies",
    "Emoji": "🎈 🤡",
    "Answer": "PENNYWISE",
    "Trivia": '''Did you know?
The film is the highest grossing Stephen King adaptation film to date.'''
    },
    {
    "Category": "Horror Movie Baddies",
    "Emoji": "🎃 🔪",
    "Answer": "MICHAEL MYERS",
    "Trivia": '''Did you know?
Halloween was shot in 20 days in the spring of 1978'''
    },
    {
    "Category": "Horror Movie",
    "Emoji": "😴 😱 🌳  🏘",
    "Answer": "NIGHTMARE ON ELM STREET",
    "Trivia": '''Did you know?
Nightmare on Elm Street is the film debut of Johnny Depp.'''
    },
        {
    "Category": "Horror Movie",
    "Emoji": "📼 👻 💍",
    "Answer": "THE RING",
    "Trivia": '''Did you know?
Until Stephen King's It (2017), this movie was the highest-grossing horror remake in history,
with a total worldwide gross of over US $249 million'''
    }
]