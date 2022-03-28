# Declare characters used by this game.
define m = Character(_("Me"), color="#ffb7c5")
define p = Character(_("Perfect Match"), color="#708090")
define i = Character(_("Isabelle"), color="#fcf75e")
define j = Character(_("Judith"), color="7a942e")
define b = Character(_("Bayonetta"), color="23297a")


# The game starts here.
label start:

    # Start by playing some music.
    play music cafe

    scene bg cafe
    with fade

    "You finally arrive at your final destination - the \"Singles\" bar."

    "Looking around the small yet surprinsingly cozy place, you notice your table right away."

    m "Gosh, what a name for a bar. I still can't believe I'm actually doing this..."

    "Reluctantly you take a seat at the table reserved just for you, hoping that the comfortable couch will be able to sooze your growing nervousness."

    "Your eyes meet the eyes of the waiter, and he casually nods at you, acknowledging your existance."

    m "I guess I can't order anything just yet?.."

    "Visibly confused, but still awkwardly patient you just start staring at other people around you."

    "A few couples here already. Everyone looks colorful to say the least."

    m "They don't look out of place and anxious, so why do I feel this way?"

    "Your best friend told you about this bar around two weeks ago or so, and you weren't sure if coming here was the right thing to do."

    "Claire broke up with you two months ago. She didn't care to put any emotional effort into it either."

    "\"You can't last longer than five minutes. Good luck next <\3\" - read the text message on your phone that day."

    "Your ego took a giant blow, can say this much."

    "Bill, your best friend, suggested that you check out this new bar. He said he got a gorgeous date there. Mileena, or whatever her name was."

    "The bar is not just your basic bar as well. Its whole shtick is that it is a blind date place."

    "Being a fan of actually knowing who you're meeting before you meet them, you were on the fence about the idea. At first."

    "Yet here you are today. Dreading the moment you have to choose."

    "And right as this thought pops up in your mind, the surface of the table starts glowing light blue."

    m "What the hell?"

    "The glow quickly dissipates and the surface now looks glass-like. It's a screen!"

    "The screen goes from the grey nothingness to a grey nothingnes with three cards displayed on it. They looks like playing cards, but with no indication on them."

    p "Hello there! We're Perfect Match, a service helping unite people together to have long lasting relationships full of love. Thank YOU for choosing us."

    "The robotic voice that makes you flinch, because of its sudden appearance, seems to be coming out of nowhere and everyhere at the same time."

    "But only you seem to hear it."

    p "Perfect Match is a unique service that allows us to connect humanoids and the like to have a bond that will truly span a life time of either of the participants."

    p "We use a revolutionary warping device that lets YOU meet the perfect person from anywhere in time and space."

    "A what now? This blind date thing definitely got way more exciting."

    p "You are presented with three cards that each represent a potential partner for YOU."

    p "We will describe each of the matches and YOU will choose according to your needs and desires."

    p "Shall we proceed?"

    menu:

        "Yes":
            jump yes

        "No":
            jump no


label yes:

    "The first card takes a yellowish hue and some letter pattern appears on it."

    p "Your first Perfect Match (later PM) is a kind and gentle soul. Her whole town seems to love her and appreciate the work she does for the community."

    p "This PM describes herself hard-working and non-confrontational. She drinks coffee with milk and sugar, and is a great cook."

    "Claire was a bitch, clearly. And she never cooked."

    m "Sounds pretty good to me. Do I even need to hear about the rest? It's a blind date anyway."

    "The second card becomes olive green and has a weird looking symbol on it you're not familiar with."

    p "Your second PM is an ambitious, straightforward woman. Working as a scientist, she puts a lot of emphasis on intellect."

    p "The PM describes herself as a slender redhead with passion for adventure and new inventions."

    "Claire was dumb as a rock. She thought humans had been manufactured by aliens from deep space."

    m "I can always appreciate a smart woman."

    "The third card turns dark blue with flashes of hot pink around the edge."

    p "The third and final PM is a seductive witch with great hairstyles. Playful and cunning, she knows how to use her naturally big charms to her advantage."

    p "The PM says that she loves using sexual innuendos and is generally very emotional in all senses of the word."

    "Claire wasn't even that hot, honestly. Good riddance."

    "You suddenly get real excited."

    m "A charming lady, huh? Don't mind meeting her..."

    p "Now it's YOUR turn to choose! Perfect Match will be sure to match YOU with the love of your life!"

    "All three cards on the screen begin pulsating in front of you, as if eager to see which one you pick."

    m "I'm choosing ..."

    menu:

        "The first yellow card":
            jump yellow

        "The second olive card":
            jump olive

        "The third blue card":
            jump blue


label yellow:

    "With a flash, the screen on the table top goes dark."

    "You can't hear the robotice voice anymore either."

    "Suddenly, a person's silhouette starts forming right in front of your eyes, just across the table."

    "It goes from just a shadow to slowly gaining color and shape and finally turning into..."

    show isabelle smile
    with dissolve

    "A sweet little smile appears on her face."

    i "Hello, my name is Isabelle! Let's have this date and get to know each other better, shall we?"

    "She blinks excitedly and pulls her chair closer to you."

    scene black
    with dissolve

    "Well, that was unexpected. I'm not gonna peak into your date though, have a good one!"

    "{b}Isabelle Ending{/b}."

    return


label olive:

    "With a flash, the screen on the table top goes dark."

    "You can't hear the robotice voice anymore either."

    "Suddenly, a person's silhouette starts forming right in front of your eyes, just across the table."

    "It goes from just a shadow to slowly gaining color and shape and finally turning into..."

    show judith smile
    with dissolve

    "The woman quickly tries to fix her hair and adjust her turtleneck collar."

    j "Oh hi there, I'm Judith, Judith Mossman. I'm a scientist working at Black Mesa."

    "She looks quite serious, but you can see a gentle smile on her face."

    scene black
    with dissolve

    "She's iconic, isn't she. I'm not gonna peak into your date though, have a good one!"

    "{b}Judith Ending{/b}."

    return

label blue:

    "With a flash, the screen on the table top goes dark."

    "You can't hear the robotice voice anymore either."

    "Suddenly, a person's silhouette starts forming right in front of your eyes, just across the table."

    "It goes from just a shadow to slowly gaining color and shape and finally turning into..."

    show bayonetta smile
    with dissolve

    "The woman looks up and down at you through her glasses and then playfully winks."

    b "I'm Bayonetta. But you'll be allowed to call me by my real name, if you promise I can call you daddy."

    "She licks her lips and, as if tired from carrying them, casually rests her breasts on the table."

    scene black
    with dissolve

    "The Japanese dommy mommy herself. I'm not gonna peak into your date though, have a good one!"

    "{b}Cereza Ending{/b}."

    return


label no:

    m "No, this is too much for me."

    scene black
    with dissolve

    "Gurl, I'm making a silly little game here, you should be saying \"yes\", start over now! pls."

    "{b}Bad Ending{/b}."

    return
