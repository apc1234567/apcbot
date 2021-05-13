import discord

import os

import random



client = discord.Client()



@client.event

async def on_ready():

    print('We have logged in as {0.user}'.format(client))



@client.event

async def on_message(message):

    if message.author == client.user:

        return

    if message.content == "apc.help":

        await message.channel.send('These are the available commands: \n apc.solve [multiple choice problem] \n apc.fortune [yes or no question] \n apc.pasta [requested pasta] \n apc.problem [problem search keyword] \n apc.hydrovinylation')

    ##Meme Commands

    if str(message.channel.id) in ["708421994206462022", "529124258710945811", "529125682509512744", "702686828121161828"]: ##The channels you want the bot to use

        if message.content.startswith('apc.hydrovinylation'):

            await message.channel.send('In organic chemistry, hydrovinylation is the formal insertion of an alkene into the C-H bond of ethylene. The more general reaction, hydroalkenylation is the formal insertion of an alkene into the C-H bond of any terminal alkene. The reaction is catalyzed by metal complexes. A representative reaction is the conversion of styrene and ethylene to 3-phenybutene')

            

        if message.content.startswith('apc.solve'):

            num = random.randint(25, 100)

            await message.channel.send('The answer is C with ' + str(num) + '% confidence')

            

        if message.content.startswith('apc.fortune'):

            input = str(message.content)

            fortunes = ["Yes", "No", "Maybe So", "Indeed", "Hmmmmm", "I don't Know", "yes", "thats weird", "no???", "whyyyy?", "probably yes", "probably no", "Not sure", "Ask someone else", "NOOOO", "Ask Again", "you have been reported"]

            fortune_number = abs(77*len(input) % len(fortunes))

            await message.channel.send(fortunes[fortune_number])

            

        if message.content.startswith('apc.pasta'):

            input = str(message.content)

            key = input[10::]

            dict = {

                "tennis" : "gideon's balls",

                "hydrovinylation" : "In organic chemistry, hydrovinylation is the formal insertion of an alkene into the C-H bond of ethylene. The more general reaction, hydroalkenylation is the formal insertion of an alkene into the C-H bond of any terminal alkene. The reaction is catalyzed by metal complexes. A representative reaction is the conversion of styrene and ethylene to 3-phenybutene",

                "fuming" : "I'm fuming. I'm fuming so much that more smoke is coming from the top of my head than the cup of starbucks coffee I bought two minutes ago. I was talking a walk to get my daily starbucks venti americano until I saw your message. I broke down out of despair and dropped my coffee on the sidewalk. I can't believe it. Not only did I waste $4 because of your pathetic message, but I lost hope in humanity.",

                "interject" : "i never said i did but also not everything's about you - you don't need to interject yourself into everything",

                "denied" : 'consider your request officially denied. You probably expected it since you\'re so annoying but just in case you\'re unaware of the world around you, I\'ll explain. What you say in this server doesn\'t actually have any emotional impact on me. However, it shows me what type of person you are — a child. It indicates that you\'re the type of person who deliberately tries to provoke negative reactions from other people. I don\'t wish to interact with anyone like that, so I have to block you. It has nothing to do with "hurt feelings" or "not being able to take a joke". It has to do with the content of your character and being a HUGE failure.',



                }

            if key == "help":

                await message.channel.send('To order a delicious pasta, type "apc.pasta [desired_pasta]". \n Here are the available pastas on the menu:')

                menu = "\n"

                for j in dict:

                    menu = menu + "\n" + str(j)

                await message.channel.send(menu)

            else:

                await message.channel.send(dict[key])

                

        if "deez nuts" in str(message.content):

            await message.channel.send("C O M E D Y \n A C H I E V E D")

    

    ##Useful Commands

    

    if message.content.startswith('apc.problem'):

        input = message.content[12::]

        results = ["Try these problems:",]

        problems = {'IChO Prep 2008 problem 2': 'Inorganic, Vanadium chem, 3, 3, 4, fairly good\\n', 'IChO Prep 2008 problem 8': 'General, superacids,  mcb,  HF as a solvent,  predicting reactions, 4, 4, 5, HF,  superacids,  stuff like that. Really weird mechanism for the last question,  I really like the consideration of equilibrium problem and what condition is required for the two to be equal. Still can\\t solve e)\\n', 'IChO Prep 2008 problem 12': 'Analytical, redox calculations, 1.5, 3.5, 4, A very solid problem for developing an intuition on nernst and utilizing the equation. Not gonna lie,  the first time solving this I was kinda amused by how they utilized it lol\\n', 'IChO Prep 2008 problem 27': 'Physical, organic kinetics, 2.5, 3.5, 5, A very solid organic pchem problem. The solutions are rather clever (and is lowkey deceptive if you try to plug and chug,  youll get it wrong),  I want to remake this problem later on\\n', 'IChO Prep 2008 problem 13': 'Analytical, Nernst and redox, 3, 4, 4.5, A very solid problem for Ksp & Electrochemistry,  very cool\\n', 'IChO Prep 2008 problem 4': 'Inorganic, SiO2 units and bonds, 4, 3, 4, kind of clever question with SiO2. Honestly Im not sure how I fell for it for the second time\\n', 'IChO Prep 2008 problem 5': 'Inorganic, FeS2; pyrite, 3.5, 3, 4.5, a really good question that literally everyone should try out. Hard to describe,  its just really cool\\n', 'IChO 2008 problem 9': 'Analytical, redox calculations, 4.5, 3.5, 4, Good practice for redox,  somewhat amusing ig\\n', 'IChO Prep 2008 problem 3': 'Analytical, Transition metal redox, 2, 2.5, 3, stock Vanadium (spoiler) chemistry\\n'}

        if input == "help":

            await message.channel.send('Type apc.problem [keyword] where [keyword] is a term you want to search for, like "oxidation." Search is not case sensitive. If you cannot find an exact term, try searching for a part of the term, like "oxid."')

        else:

            for id in problems:

                if input.lower() in problems[id].lower():

                    results.append(id)

            send_this = ""

            for id in results:

                send_this = send_this + "\n" + str(id)

            await message.channel.send(send_this)





client.run({Your bot token})
