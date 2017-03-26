###################################################################
#   This program was written to host an alexa skill.              #
#   It gives a user a random bro code article.                    #
#                                                                 #
#   Author: Gyorgy Rethy                                          #
#   Date:   25/03/2017                                            #
###################################################################

from flask import Flask
from random import randint

app = Flask(__name__) #create app instance

#create data
array = ["Article 1. Bros before hoes. Always remember, girlfriends come and go, but your boys are always there. Breaking this rule is to commit the cardinal sin against Team Testosterone.",
"Article 2. Never drink the last beer, unless you have been granted specific permission that it is OK.",
"Article 3. If a girl falls into the following criteria, she is off limits forever until the end of time A. Was an ex-girlfriend. B. Your friend specifically told you he wanted her. C. Is your buddys sister. However, if it is your buddys cousin, well she is up for grabs, and you are welcome to rub it in his face for years to come.",
"Article 4. Never diss a guy if his team just lost a crushing game.",
"Article 5. You must never own a cat. New amendment to this rule. A Bro may never own more than 2 cats, but only if they adhere to the Bro Code.",
"Article 6. If you get 2 tickets to the big game, the priority list for granting the second ticket is as follows 1. Your best friends (in order of how long you have known them). 2. Your acquaintances. 3. Your co-workers. 4. The mailman. 5. The UPS guy. 6. NASA. 7. John Kerry .....1485726. Your girlfriend.",
"Article 7. You are allowed to enjoy exactly one chick TV show, and one chick flick. You may have no more.",
"Article 8. Birthday and Christmas presents for your guy friends are optional. Beer always makes a great gift.",
"Article 9. If you go the bar with your buddies, you must buy a round of drinks at least once. The Bro with the better paying job is required to buy the first round. If the other Bro is temporarily out of money or left his wallet at home drinks can be lended yet in the long run these drinks must be repaid, later that night by wingman services or any other act of entertainment or at the next gathering.",
"Article 10. There are no mercy rules when playing someone in Madden, hoops, street hockey, bare-fisted boxing, etc.",
"Article 11. If you owe someone money, pay them back as soon as humanly possible, unless it is a gambling debt, which must be paid immediately.",
"Article 12. Standard shotgun rules are as follows. A. Shotgun may only be called within full sight of the car. B. Shotgun must be called outside. C. Shotgun calls last approximately ten minutes. D. Shotgun never carries over to a second ride.",
"Article 13. NO PDA (Public Displays of Affection).",
"Article 14. It is alright to cheat at any game where money is not involved. In certain circumstances, relationships may be classified as games.",
"Article 15. Do not tell other guys elaborate stories about your weightlifting exercise routine. No one cares.",
"Article 16. Never openly question another guys sports wisdom, unless said information specifically pertains to your favorite team.",
"Article 17. When out with the guys, never accept a call from your girlfriend, unless she is dying or trapped under a burning fuel truck, and if that is the case, make it quick.",
"Article 18. Always allow a buffer zone at urinals and on couches.",
"Article 19. Never share a bed with a guy, unless there is no way around it.",
"Article 20. Bros Before Hoes. I know, I already used it. I can not stress it enough, though. It is absolutely infuriating how many of my guy friends have become insufferable beings since they have gone out with someone.",
"Article 21. In a 6 person hot tub, there should be a maximum of 3 guys.",
"Article 22. A Bro should not sing and dance at the same time",
"Article 23. A Bro should not watch Oxygen, Womens Entertainment, or Lifetime.",
"Article 24. Men do not lie about their age.",
"Article 25. A Bro should not swing his arms when he is walking.",
"Article 26. A Bro will, in a timely manner, alert his Bro to the existence of a girl fight. A Bro must never hesitate before communicating the possibility of fisticuffs between two humans of the female variety HENCEFORTH GIRL FIGHT , in an effort to make possible and probable that another Bro or Bros can partake in observation. A timely manner is open to interpretation based on the initial Bros viewing and processing of the potential feminine conflagration. Said Bro must use any and all methods of media distribution at his disposal, including but not limited to telecommunications, elbow nudging, fiber optics, the Broney express, and postcards. If an informed Bro is unable to witness the girl fight firsthand, the spotter Bro is responsible for documenting and relating details of the girl fight via pictures, video, or barring any other reasonable method, interpretive dance and or pantomime. Tabling Bro obligations to witness a XX chromosomal scuffle is not only condoned, but encouraged, and in some cases, required. Please refer to the Brobligation rubric as elucidated in AMENDMENT 83. The REALLY hot sister and other hump trumps.",
"Article 27. A Bro should never carry a womans handbag",
"Article 28. A Bro should never go tanning.",
"Article 29. No Bro should dye their hair",
"Article 30. A Bro should never refer to an athlete as a stud",
"Article 31. A Bro should never cry during a movie. In the event that he does, he must under no circumstance admit it to anyone other than a girl he is trying to score with.",
"Article 32. A Bro should not pop his collar.",
"Article 33. A Bro should not speak more than two languages. Unless 1. He has lived for a minimum of 9 months in a country whose main language is one of those languages 2. He uses the extra language as a means of picking up women who only speak that language 3. His job requires him to know more than 2 languages 4. It is a means of only to impress women and nothing else. If in the occurrence that a Bro knows more than 2 languages, it is the given right for said bro to invite other bros to parties where this language is spoken, having said bro escort and be the official bilingual wingman.",
"Article 34. Bros cannot make eye contact during a devils threeway two dudes.",
"Article 35. A Bro should never say it is to die for",
"Article 36. A Bro should not wear a scarf without a jacket or coat.",
"Article 37. A Bro should not wear an ascot.",
"Article 38. A Bro should never use the following words: fantabulous, ginormous and fierce.",
"Article 39. A Bro should never wrap a towel around his head after leaving the shower.",
"Article 40. A Bro should never sip and alcoholic drink through a straw",
"Article 41. A Bro should never wear a blouse.",
"Article 42. If you are not living with a girl you should not have tampons in your bathroom.",
"Article 43. A Bro should not wear crocs.",
"Article 44. A Bro should not wear a leotard or do pirouettes.",
"Article 45. A Bro should never wear a sweater over his shoulders",
"Article 46. A Bro should not eat grapes from the vines",
"Article 47. A Bro should never rollerblade",
"Article 48. The word cute should not be used other then describing a chick they want to bone",
"Article 49. If you compliment a guy on his six-pack, you better be referring to his beer.",
"Article 50. A Bro should never, ever wear capri pants.",
"Article 51. A Bro should not wear flip flops with a suit.",
"Article 52. No Bro should wear a speedo to the beach",
"Article 53. A Bro will, whenever possible, provide his Bro with protection. In the event that one Bro finds himself lacking the necessary prophylactic accoutrements needed to complete the act of coitus in a safe and effective manner, he is in the right to expect his Bro will use all measures within or without his means to provide the aforementioned prophylactic in a timely yet discreet fashion. When a Bro signals his need using previously agreed upon code words and or body signage, it is understood that his Bro will discontinue all present activity, excepting the act of coitus itself, whereby which Bro vows to finish as quickly as possible, in order to respond with a panoply of options at Bro-in-needs location. A Bro must patronize the most rapid method of transportation available while endeavoring to assist his Bro. In no instance may a two-wheeled bicycle be used as this is not only humiliating, but also potentially harmful to the perineum, a zone of tissue perilously adjacent to noted sexual organs. Unless a bicycle is the ONLY form of transportation, as in some Cambodian villages. In the event that a state, federal, international, or galactic law is breached due to recklessness, unacceptable levels of speed, and or the hijacking of an airborne vehicle, it is understood that the primary Bro will shoulder any associated legal fees or fines. However, any costs or damages incurred from the use of public transportation are the responsibility of the secondary Bro alone as this is an instance of Quid Pro Bro. Upon arrival at the primary Bros location, the secondary Bro must exercise complete discretion so as not to disrupt the primary Bros flow. It is understood that a Bro will engage in all training necessary to achieve this objective, including, at minimum, a five month Ninjitsu curriculum mastering the twin arts of stealth and secrecy. Once the primary Bro has been supplied with the necessary prophylactic, the Brocedure is deemed complete upon exchange of the traditional, though in this case silent, high five. Tacit in this unspoken ritual is the understanding that said episode will never be spoken of again, unless it is part of an awesome story.",
"Article 54. No Bro should make a kissing face in a photo.",
"Article 55. No Bro should wear girl jeans",
"Article 56. A Bro shall never reveal the score of a sporting event to another Bro until that Bro has thrice confirmed it is cool.",
"Article 57. A Bro may not speculate on the expected Bro chick ratio of a party or venue without first disclosing the present-time observed ratio.",
"Article 58. If a Bro, for whatever reason, becomes aware of another Bros girlfriends birthday and or anniversary date, he shall endeavor to make that information available to his Bro, regardless of whether he thinks his Bro already knows.",
"Article 59. One Bro makes a solo attack. A Second Bro provides a crutch, A third Bro rounds out the pack, But a fourth Bro is one too much.",
"Article 60. Should a Bro be near to closing with a girl, his Bro shall do anything within his means to ensure the desired outcome, up to and including the seduction of said girls wildly unattractive friend, cousin, sister.",
"Article 61. A Bro shall honor thy father and mother",
"Article 62. In the event that two Bros acquire the same target, the Bro with the longer dry spell has dibs. Should the dry spells be of equal length, a game of discreet roshambo, rock paper scissors, shall determine the outcome.",
"Article 63. In a scenario in which two or more Bros are engaged in entertainment of the adult variety, one Bro is forbidden from intentionally or unintentionally touching another Bro in any capacity, including but not limited to the high-five, the fist bump, or the congratulatory gluteus pat. Winking is also a no no.",
"Article 64. A Bro must provide his Bro to a ticket to an event if said event involves the second Bros favorite sports team in a playoff scenario",
"Article 65. A Bro must always reciprocate a round of drinks among Bros with the proviso that no existing wager supercedes this purchase and exchange of spirits.",
"Article 66. If a Bro suffers pain due to the permanent dissolution of a relationship with a lady friend, a Bro shall offer nothing more than that sucks, Bro and copious quantities of beer. A Bro will also refrain from pejorative commentary, deserved or not, regarding said lady friend for a period of three months, when the requisite BACKSLIDE WINDOW has closed.",
"Article 67. Should a Bro pick up a guitar at a party and commence playing , another Bro shall point out that he is a fool.",
"Article 68. If a Bro be on a hot streak, another Bro will do everything possible to ensure its longevity, even if that includes jeopardizing his own records, the missing of work, or temporary immigration to a foreign country.",
"Article 69. No Bro should ever get a pedicure.",
"Article 70. A Bro should never highlight his hair.",
"Article 71. A Bro should not talk to another Bro in the bathroom.",
"Article 72. A Bro should never sing show tunes.",
"Article 73. A Bro should never eat out of another Bros hands.",
"Article 74. Two men should not share an umbrella.",
"Article 75. A Bro should not have an outfit.",
"Article 76. A Bro should not wear a white belt.",
"Article 77. A Bro never cries. Unless it is regarding Article 31.",
"Article 78. A Bro should never wiggle out of a pair of pants.",
"Article 79. No Bro can hit another Bro in the groin unless victim Bro has broken the Bro code.",
"Article 80. A Bro may never seek entertainment from professional womens sports. Unless said entertainment be comedic or physical e.g. gymnastics, beach volleyball.",
"Article 81. What happens between bros stay between bros also known as the what happens in vegas stays in vegas rule and the what happens on tour stays on tour rule.",
"Article 82. If a Bro catches another Bro in plagiarism, albeit awesome plagiarism, a Bro shall be required to ask the Bro to cite his source.",
"Article 83. A Bro can not cockblock another Bro UNLESS sleeping with said girl would break a Bro code.",
"Article 84. Love thy neigh Bro",
"Article 85. No bros night out can start with the wife put out some cheese and end with everyone at home by eleven, booya.",
"Article 86. If said bros is lost to a relationship, they must void all rights to use the bros code for any purpose and are rightfully subjected to any and all humorous ploys made to said post-bros by previous bros.",
"Article 87. A Bro shall at all times say Yes.",
"Article 88. Any bros who notice a fellow bros passed out at any social gathering due to drug or alcohol consumption, is obligated to take humiliating photos and or videos of the passed out bros, unless said bros has consumed a whiskey, rum, scotch or other hard liquor to an excess of a ratio of, once ounce,3kg of body mass. 7lbs imperial.",
"Article 89. A Bro may never pursue the mom of another Bro. Be it here resolved that at no point is it permissible for one Bro to engage in carnal delicacies with another Bros mother. It is, however, allowed and encouraged for one Bro to graphically suggest to a Bro the athletic feats, animalia, and or machinery utilized during a fictional encounter with his mom. NOTA BENE: It is customary for a Bro to avoid such Brocularity if his Bros mom is a 9 or better, for fear of Oedipal inducement. Should a Bro discover his Bro is in fact adopted, he is free to pursue his Bros adoptive mother, but only after first corroborating nonbiological parentage through notarized birth certificates, hospital records, or comparative dioxyribonucleic acid gel electrophoresis, whichever is easiest. Since the adopted Bro cannot legitimately claim to have shared a canal with his Bro, ARTICLE 89 expressly prohibits the adopted Bro from invoking the Sloppy Second clause in any related filings with the International Court of Bros. Though the mom of a Bro is always off limits, the step-mom of a Bro is allowed if she initiates it and or is wearing at least one article of leopard print clothing. If she looks good in it.",
"Article 90. No bros should know any fellow bros weight for any reason. Previous bros code stipulation should only have an assumed weight. If the assumed weight is on the turning point of humility and peace, humility over-ride.",
"Article 91. When bros are up for the same promotion job position and are subjected to interviews, bros in a prior interview must alert bros of any and all trick questions they can remember. This ensures all bros get an equal chance at the position title because it is well known fact that the bros performing the interview wants to get the process over as quick as possible and the only way for a fair chance is to make all subsequent bros seem better.",
"Article 92. When a bro introduces a fellow bro to their hot female friend, the introducer has the rights to the girl. The introduced bros can only attempt to get the girl if the introducer bro gives his consent.",
"Article 93. If any bros acts out of line and defies any bros code during a multiple bros conversation with any number of girls, the other bros have the right to tell any humiliating stories and facts about said bros for the purpose of ruining said bros chances with the girls.",
"Article 94. Should a Bro, 1st, 2nd or 3rd, be hooking up with an unattractive woman, the Bro that notices this must do all in their power to stop said Bro from closing the deal, unless they are helping another Bro with Article 60.",
"Article 95. Any girl passing out in a non-bedroom designated area of a dwelling occupied by more than one bros is not up for grabs under any circumstances. Additionally, said girl can be subjected to humiliating photos as long as other bros are alerted to its undertaking"
]

@app.route('/',methods=['POST','GET'])
def randomCode():
    randomNo = randint(0,94)
    string = array[randomNo]
    response = '''
    {
        "version": "1.0",
        "sessionAttributes": {},
        "response": {
            "outputSpeech": {
            "type": "PlainText",
            "text": "'''+string+'''"
        },
        "card": {
            "type": "Simple",
            "title": "Bro Code",
            "content": "'''+string+'''"
        },
        "shouldEndSession": true
        }
    }
    '''

    return response
            
app.run()