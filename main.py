# Plan

# The aim is to create a bot that makes the best statistically-possible Wordle guesses
# By best statistically-possible guess, I mean a guess that uses the most common letters possible each time
# This will involve looping over a long list of possible words each time, I will try to optimise this performance
# Over time I hope this bot will yield impressive stats

# I have grabbed the 14885 ords in the wordle word list from the Wordle source code (available via developer tools)

import json

with open("words.json", "r") as file:
    wordle_words = json.load(file)

print(f"Total words: {len(wordle_words)}")

# previous words grabbed from https://www.rockpapershotgun.com/wordle-past-answers
# AUTOMATE THIS!

previous_words_string = "ABACK ABASE ABATE ABBEY ABIDE ABOUT ABOVE ABYSS ACORN ACRID ACTOR ACUTE ADAGE ADAPT ADMIT ADOBE ADOPT ADORE ADULT AFFIX AFTER AGAIN AGAPE AGATE AGENT AGILE AGING AGLOW AGONY AGREE AHEAD AISLE ALBUM ALIEN ALIKE ALIVE ALLOW ALOFT ALONE ALOOF ALOUD ALPHA ALTAR ALTER AMASS AMBER AMISS AMPLE ANGEL ANGER ANGRY ANGST ANODE ANTIC ANVIL AORTA APART APHID APPLE APPLY APRON APTLY ARBOR ARDOR ARGUE AROMA ASCOT ASIDE ASKEW ASSET ATLAS ATOLL ATONE AUDIO AUDIT AVAIL AVERT AWAIT AWAKE AWASH AWFUL AXIOM AZURE BACON BADGE BADLY BAGEL BAKER BALSA BANAL BARGE BASIC BASIN BATHE BATON BATTY BAWDY BAYOU BEACH BEADY BEAST BEAUT BEEFY BEGET BEGIN BEING BELCH BELIE BELLY BELOW BENCH BERET BERTH BESET BEVEL BINGE BIOME BIRCH BIRTH BLACK BLADE BLAME BLAND BLARE BLAZE BLEAK BLEED BLEEP BLIMP BLOCK BLOKE BLOND BLOWN BLUFF BLURB BLURT BLUSH BOAST BONUS BOOBY BOOST BOOZE BOOZY BORAX BOSSY BOUGH BOXER BRACE BRAID BRAIN BRAKE BRASH BRASS BRAVE BRAVO BRAWN BREAD BREAK BREED BRIAR BRIBE BRIDE BRIEF BRINE BRING BRINK BRINY BRISK BROAD BROKE BROOK BROOM BROTH BROWN BRUSH BRUTE BUDDY BUGGY BUGLE BUILD BUILT BULKY BULLY BUNCH BURLY CABLE CACAO CACHE CADET CAMEL CAMEO CANDY CANNY CANOE CANON CAPER CARAT CARGO CAROL CARRY CARVE CATCH CATER CAULK CAUSE CEDAR CHAFE CHAIN CHALK CHAMP CHANT CHAOS CHARD CHARM CHART CHEAP CHEAT CHEEK CHEER CHEST CHIEF CHILD CHILL CHIME CHOCK CHOIR CHOKE CHORD CHORE CHOSE CHUNK CHUTE CIDER CIGAR CINCH CIRCA CIVIC CLASS CLEAN CLEAR CLEFT CLERK CLICK CLIMB CLING CLOAK CLOCK CLONE CLOSE CLOTH CLOUD CLOWN CLUCK COACH COAST COCOA COLON COMET COMMA CONDO CONIC CORER CORNY COULD COUNT COURT COVER COVET COWER COYLY CRAFT CRAMP CRANE CRANK CRASS CRATE CRAVE CRAWL CRAZE CRAZY CREAK CREDO CREPE CREPT CRIME CRIMP CRISP CROAK CRONE CROSS CROWD CROWN CRUMB CRUSH CRUST CRYPT CUMIN CURLY CYBER CYNIC DADDY DAISY DANCE DANDY DEATH DEBIT DEBUG DEBUT DECAL DECAY DECOY DECRY DELAY DELTA DELVE DENIM DEPOT DEPTH DETER DEVIL DIARY DICEY DIGIT DINER DINGO DINGY DISCO DITTO DITTY DODGE DOGMA DOING DOLLY DONOR DONUT DOUBT DOWRY DOZEN DRAFT DRAIN DRAWN DREAM DRINK DRIVE DROLL DROOL DROOP DROVE DUCHY DUTCH DUVET DWARF DWELL DWELT EAGLE EARLY EARTH EASEL EBONY EDICT EGRET EJECT ELDER ELOPE ELUDE EMAIL EMBER EMPTY ENACT ENDOW ENEMA ENJOY ENNUI ENSUE ENTER EPOCH EPOXY EQUAL EQUIP ERODE ERROR ERUPT ESSAY ETHER ETHIC ETHOS EVADE EVENT EVERY EVOKE EXACT EXALT EXCEL EXERT EXIST EXPEL EXTRA EXULT FACET FAINT FAITH FALSE FANCY FARCE FAULT FAVOR FEAST FEIGN FERAL FERRY FEVER FEWER FIBER FIELD FIEND FIFTY FILET FINAL FINCH FINER FIRST FISHY FIXER FJORD FLAIL FLAIR FLAKE FLAME FLANK FLARE FLASH FLASK FLESH FLICK FLING FLINT FLIRT FLOAT FLOCK FLOOD FLOOR FLORA FLOSS FLOUR FLOUT FLOWN FLUFF FLUME FLUNG FLUNK FLYER FOCAL FOCUS FOGGY FOLLY FORAY FORCE FORGE FORGO FORTE FORTH FORTY FOUND FOYER FRAIL FRAME FRANK FRESH FRIED FROCK FROND FRONT FROST FROTH FROWN FROZE FULLY FUNGI FUNKY FUNNY GAMER GAMMA GAMUT GAUDY GAUNT GAUZE GAWKY GECKO GENRE GHOUL GIANT GIDDY GIRTH GIVEN GLASS GLAZE GLEAM GLEAN GLIDE GLOAT GLOBE GLOOM GLORY GLOVE GLYPH GNASH GOING GOLEM GONER GOODY GOOFY GOOSE GORGE GOUGE GRACE GRADE GRAIL GRAIN GRAND GRANT GRAPH GRASP GRATE GREAT GREEN GREET GRIEF GRIME GRIMY GRIND GRIPE GROIN GROOM GROUP GROUT GROVE GROWL GRUEL GUANO GUARD GUEST GUIDE GUILD GUILE GULLY GUMMY GUPPY GUSTY HAIRY HALVE HANDY HAPPY HARSH HATCH HATER HAVOC HEADY HEARD HEART HEATH HEAVE HEAVY HEFTY HEIST HELIX HELLO HENCE HERON HILLY HINGE HIPPO HITCH HOARD HOBBY HOMER HONEY HORDE HORSE HOTEL HOUND HOUSE HOWDY HUMAN HUMID HUMOR HUMPH HUNCH HUNKY HURRY HUTCH HYENA HYPER ICING IGLOO IMAGE IMPEL INANE INDEX INEPT INERT INFER INLAY INNER INPUT INTER INTRO IONIC IRATE IRONY ISLET ITCHY IVORY JAUNT JAZZY JELLY JERKY JIFFY JOINT JOKER JOLLY JOUST JUDGE JUICE KARMA KAYAK KAZOO KEBAB KHAKI KIOSK KNACK KNAVE KNEAD KNEEL KNELT KNOCK KNOLL KOALA LABEL LABOR LAGER LANKY LAPEL LAPSE LARGE LARVA LASER LATTE LAYER LEAFY LEAKY LEAPT LEARN LEASH LEAVE LEDGE LEECH LEERY LEGGY LEMON LEMUR LIBEL LIGHT LILAC LIMIT LINEN LINER LINGO LITHE LIVER LOCAL LOCUS LOFTY LOGIC LOOPY LOSER LOUSE LOVER LOWER LOWLY LOYAL LUCID LUCKY LUNAR LUNCH LUNGE LUSTY LYING MACAW MADAM MAGIC MAGMA MAIZE MAJOR MAMBO MANIA MANGA MANLY MANOR MAPLE MARCH MARRY MARSH MASON MASSE MATCH MATEY MAUVE MAXIM MAYBE MAYOR MEALY MEANT MEDAL MEDIA MEDIC MELON MERCY MERGE MERIT MERRY METAL METER METRO MICRO MIDGE MIDST MIMIC MINCE MINER MINUS MODEL MODEM MOIST MOLAR MOMMY MONEY MONTH MOOSE MOSSY MOTOR MOTTO MOULT MOUNT MOURN MOUSE MOVIE MUCKY MULCH MUMMY MURAL MUSHY MUSIC MUSTY NAIVE NANNY NASTY NATAL NAVAL NEEDY NEIGH NERDY NERVE NEVER NICER NICHE NIGHT NINJA NINTH NOBLE NOISE NORTH NYMPH OCCUR OCEAN OCTET OFFAL OFTEN OLDER OLIVE ONION ONSET OPERA ORDER ORGAN OTHER OUGHT OUNCE OUTDO OUTER OVERT OWNER OXIDE PAINT PANEL PANIC PAPAL PAPER PARER PARRY PARTY PASTA PATIO PATTY PAUSE PEACE PEACH PEARL PEDAL PENNE PERCH PERKY PESKY PHASE PHONE PHONY PHOTO PIANO PICKY PIETY PILOT PINCH PINEY PINKY PINTO PIOUS PIPER PIQUE PITHY PIXEL PIXIE PLACE PLAIT PLANK PLANT PLATE PLAZA PLEAT PLUCK PLUMB PLUNK POINT POISE POKER POLKA POLYP PORCH POUND POWER PRESS PRICE PRICK PRIDE PRIME PRIMO PRIMP PRINT PRIOR PRIZE PROBE PRONE PRONG PROSE PROUD PROVE PROWL PROXY PRUNE PSALM PULPY PUPIL PURGE QUALM QUART QUEEN QUERY QUEST QUEUE QUICK QUIET QUIRK QUITE QUOTE RADIO RAINY RAISE RAMEN RANCH RANGE RAPID RATIO RAYON REACH REACT READY REALM REBEL REBUS REBUT RECAP RECUR REFER REGAL RELAX RELIC RENEW REPAY REPEL RERUN RESIN RETCH RETRO RETRY REVEL REVUE RHINO RHYME RIDER RIDGE RIGHT RIPER RISEN RIVAL RIVET ROBIN ROBOT ROCKY RODEO ROGUE ROOMY ROUGE ROUND ROUSE ROUTE ROVER ROWER ROYAL RUDDY RUDER RUMBA RUPEE RUSTY SAINT SALAD SALLY SALSA SALTY SANDY SASSY SAUCY SAUNA SAUTE SAVOR SCALD SCALE SCANT SCARE SCARF SCENT SCOFF SCOLD SCONE SCOPE SCORE SCORN SCOUR SCOUT SCOWL SCRAM SCRAP SCRUB SEDAN SEEDY SENSE SERUM SERVE SEVEN SEVER SHADE SHAFT SHAKE SHAKY SHALL SHAME SHANK SHAPE SHARD SHARE SHARP SHAVE SHAWL SHELL SHIFT SHINE SHIRE SHIRK SHORE SHORN SHOUT SHOVE SHOWN SHOWY SHRUB SHRUG SHUNT SHYLY SIEGE SIGHT SILLY SINCE SISSY SIXTH SKATE SKIER SKIFF SKILL SKIMP SKIRT SKUNK SLANG SLATE SLEEK SLEEP SLICE SLOPE SLOSH SLOTH SLUMP SLUNG SMALL SMART SMASH SMEAR SMELT SMILE SMIRK SMITE SMITH SMOCK SMOKE SNACK SNAFU SNAIL SNAKE SNAKY SNARE SNARL SNEAK SNOOP SNORT SNOUT SOGGY SOLAR SOLID SOLVE SONIC SOUND SOWER SPACE SPADE SPEAK SPECK SPELL SPELT SPEND SPENT SPICE SPICY SPIEL SPIKE SPILL SPINE SPIRE SPLAT SPOKE SPOON SPOUT SPRAY SPRIG SPURT SQUAD SQUAT SQUID STAFF STAGE STAID STAIN STAIR STAKE STALE STALL STAND STARE STARK START STASH STATE STEAD STEAM STEED STEEL STEEP STEIN STERN STICK STIFF STILL STING STINK STINT STOCK STOIC STOLE STOMP STONE STONY STOOL STORE STORM STORY STOUT STOVE STRAP STRAW STRAY STUDY STUNG STYLE SUGAR SULKY SUNNY SUPER SURER SURLY SUSHI SWATH SWEAT SWEEP SWEET SWELL SWILL SWINE SWIRL SWISH SWOON SWUNG SYRUP TABLE TABOO TACIT TACKY TAKEN TALLY TALON TANGY TAPER TAPIR TARDY TASTE TASTY TAUNT TAWNY TEACH TEARY TEASE TEMPO TENTH TEPID TERSE THANK THEIR THEME THERE THESE THIEF THIGH THING THINK THIRD THORN THOSE THREE THREW THROW THUMB THUMP THYME TIARA TIBIA TIDAL TIGER TILDE TIPSY TITAN TITHE TITLE TOAST TODAY TONIC TOOTH TOPAZ TOPIC TORCH TORSO TOTAL TOTEM TOUCH TOUGH TOWEL TOXIC TOXIN TRACE TRACT TRADE TRAIN TRAIT TRASH TRAWL TREAT TREND TRIAD TRICE TRITE TROLL TROPE TROVE TRULY TRUSS TRUST TRUTH TRYST TUNIC TUTOR TWANG TWEAK TWEED TWICE TWINE TWIRL TWIST UDDER ULCER ULTRA UNCLE UNDER UNDUE UNFED UNFIT UNIFY UNITE UNLIT UNMET UNTIE UNTIL UNZIP UPPER UPSET URBAN USAGE USHER USING USUAL USURP UTTER UVULA VAGUE VALET VALID VALUE VAPID VAULT VENOM VERGE VERVE VIDEO VIGOR VINYL VIOLA VIRAL VISOR VITAL VIVID VODKA VOICE VOILA VOTER VOUCH VYING WACKY WAFER WAGON WALTZ WASTE WATCH WEARY WEDGE WEIRD WHACK WHALE WHEEL WHELP WHERE WHICH WHIFF WHILE WHINE WHINY WHIRL WHISK WHOOP WIDEN WINCE WINDY WITCH WOKEN WOMAN WOOER WORDY WORLD WORRY WORSE WORST WOULD WOVEN WRATH WREAK WRIST WRITE WRONG WROTE WRUNG YACHT YEARN YIELD YOUNG YOUTH ZEBRA ZESTY"
previous_words = previous_words_string.split(" ")

print(f"Total previous words: {len(previous_words)}")

# This map of letter frequency in the English dictionary is taken from https://www3.nd.edu/~busiforc/handouts/cryptography/letterfrequencies.html
letter_frequency = {
"E": 11.1607,
"M": 3.0129,
"A": 8.4966,
"H": 3.0034,
"R": 7.5809,
"G": 2.4705,
"I": 7.5448,
"B": 2.0720,
"O": 7.1635,
"F": 1.8121,
"T": 6.9509,
"Y": 1.7779,
"N": 6.6544,
"W": 1.2899,
"S": 5.7351,
"K": 1.1016,
"L": 5.4893,
"V": 1.0074,
"C": 4.5388,
"X": 0.2902,
"U": 3.6308,
"Z": 0.2722,
"D": 3.3844,
"J": 0.1965,
"P": 3.1671,
"Q": 0.1962,
} 

letter_frequency_sorted = []

for i in range(26):
    highest_val = 0
    highest_letter = ""
    for letter in letter_frequency:
        current_val = float(letter_frequency[letter])
        if current_val > highest_val:
            highest_val = current_val
            highest_letter = letter

    letter_frequency_sorted.append([highest_letter.lower(), highest_val])
    del letter_frequency[highest_letter]

print(letter_frequency_sorted)

# find a word that includes the top 5 most frequent (and available letters)

available_letters = []
for i in range(5):
    available_letters.append(letter_frequency_sorted[i][0])

print(available_letters)

for word in wordle_words:
    possible = True
    for char in word:
        if char not in available_letters:
            possible = False
    
    if possible:
        print(word)

    # need to avoid repreated letters in the same word 

# Making the best guess based on most common letters




# Making the best guess including clues









# I would like to get the bot to play automtically, I believe i can do this by using selenium to control a web browser


