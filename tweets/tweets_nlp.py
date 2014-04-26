__author__ = 'maud'

import tweets_preprocessing
import sentiwordnet

TENSION = ['tension', 'anxiety', 'antipathy', 'enmity', 'strained', 'stressful', 'charged', 'edgy',
           'ill', 'friction', 'hostility', 'unease', 'nervous', 'anxious', 'nervousness', 'concerned',
           'troubled', 'careful', 'doubtful', 'distrustful', 'dubious', 'unsure', 'undecided',
           'unconvinced', 'disturbed', 'uncomfortable, fearful', 'unsettled', 'agitated', 'taut',
           'disquiet', 'apprenhensive', 'edgy', 'watchful', 'jittery', 'perturbed', 'twitchy',
           'solicitous', 'overwrougth', 'fretful', 'unquiet', 'antsy', 'angsty', 'discomposed',
           'apprehension', 'pressure', 'suspense', 'restless', 'harassed', 'pressurized', 'stressed',
           'tenseness', 'tense', 'distressed', 'upset', 'worried', 'worry', 'worries', 'disquieted',
           'disturbed']
TENSION_OPP = ['certain', 'cool', 'collected', 'confident', 'calm', 'quiet', 'assured', 'unfazed',
               'serene', 'easy-going', 'relaxed', 'flexible', 'unperturbed', 'nonchalent', 'sure',
               'positive', 'satisfied', 'assured', 'clear', 'trustful', 'trust']

DEPRESSION = ['depression', 'dejection', 'depressed', 'pessimistic', 'deprived', 'needy', 'lowered',
              'devalued', 'weakened', 'impaired', 'depreciated', 'low', 'down', 'grieved', 'dismal',
              'glum', 'wistful', 'dejected', 'tragic', 'depressing', 'disastrous', 'pathetic',
              'poignant', 'harrowing', 'pitiable', 'pity', 'silly', 'disappointed', 'disappointing',
              'unfortunate', 'woeful', 'deplorable', 'lamentable', 'downcast', 'tearful', 'lugubrious',
              'pensive', 'disconsolate', 'doleful', 'cheerless', 'triste', 'gloomy', 'lonely',
              'demoralized', 'demoralize', 'demoralizes', 'melancholy', 'grave', 'somber', 'mournful',
              'sad', 'sadness', 'cry', 'crying', 'sorry', 'sad', 'deplorable', 'lamentable', 'distressing',
              'unhappy', 'sorrow']
DEPRESSION_OPP = ['happy', 'pleased', 'glad', 'cheerful', 'jolly', 'merry', 'cheery', 'joyous', 'joyful'
    , 'chirpy', 'blithe']

ANGER = ['anger', 'hostility', 'heated', 'mad', 'provoked', 'opposed', 'opposite', 'contrary',
         'inimical', 'belligerent', 'antagonistic', 'unkind', 'warlike', 'rancorous', 'adverse',
         'alien', 'ill-disposed', 'outraged', 'annoyed', 'irritated', 'raving', 'choked', 'pissed',
         'threatening', 'threatened', 'infuriated', 'incesed', 'enraged', 'ranting', 'irascible',
         'ireful', 'exasperated', 'irritable', 'resentful', 'angry', 'furious', 'raging',
         'tempestuous', 'wild', 'angered', 'enraged', 'infuriated', 'maddened', 'fierce', 'ferocious',
         'savage', 'hostile', 'unfriendly', 'enmity', 'hate', 'hates', 'hated']
ANGER_OPP = ['loving', 'friendly', 'calm', 'pleasant', 'mild', 'peaceful', 'peace', 'agreeable',
             'amiable', 'congenial', 'sympathetic', 'kind', 'approving', 'cordial', 'affable']

VIGOR = ['vigor', 'strength', 'activity', 'lively', 'dynamic', 'busy', 'occupied', 'strenuous',
         'sparkling', 'animated', 'committed', 'engaged', 'enthusiastic', 'enterprising', 'forward',
         'assertive', 'forceful', 'feisty', 'spanking', 'sprightly', 'vivacious', 'forcible', 'powerful',
         'strong', 'healtly', 'alive', 'intense', 'energy', 'vigour', 'zip', 'dynamism', 'heartiness',
         'vim', 'vitality', 'industrious', 'tireless', 'activeness', 'action', 'move', 'moving', 'moves',
         'moved', 'travel', 'travelling', 'act', 'acts', 'acted', 'travelled', 'travels', 'untiring',
         'hardworking', 'indefatigable', 'unwearying', 'unflagging', 'gumtious', 'vigorous', 'forceful',
         'energetic', 'action', 'strong', 'active']
VIGOR_OPP = ['weak', 'lethargic', 'feeble', 'apathetic', 'lifeless', 'torpic', 'spiritless',
             'slow', 'lazy', 'inactive', 'frail', 'lethargic', 'weedy', 'effete', 'wussy', 'wimpish',
             'wimpy']

FATIGUE = ['fatigue', 'inertia', 'tired', 'pall', 'weary', 'jade', 'exhaust', 'exhausted', 'exhausting',
           'fatigued', 'flagging', 'sleepy', 'aspleed', 'bushed', 'dead', 'wasted', 'crippled',
           'disabled', 'jaded', 'prostrated', 'sleeping', 'drooping', 'knackered', 'drownsy', 'zonked',
           'annoyed', 'stock', 'sap', 'tire', 'bore', 'bored', 'boring', 'banal']
FATIGUE_OPP = ['fresh', 'lively', 'refreshed', 'energetic', 'awake', 'alive', 'rested', 'enthusiastic',
               'active', 'restored', 'stimulated', 'revived', 'idle', 'sluggish', 'sedentary',
               'unoccupied', 'dull', 'dormant']

CONFUSION = ['confusion', 'bewilderment', 'confused', 'bewildered', 'chaotic', 'surprised',
             'surprise', 'surprises', 'unaware', 'ignorant', 'unfamilar', 'surprising', 'stunned',
             'stunning', 'uncertain', 'startled', 'awed', 'dazed', 'dizzy', 'speechless', 'giddy',
             'confound', 'confounded', 'astonished', 'confounds', 'stunned', 'confused', 'stupefied',
             'stupefying', 'disordered', 'jumbled', 'untidy', 'topsy-turvy', 'puzzled', 'baffled',
             'muddled', 'dazed', 'perplexed', 'disoriented', 'muzzy', 'nonplussed', 'flummoxed']
CONFUSION_OPP = ['aware', 'arranged', 'organized', 'tidy', 'orderly', 'informed', 'enlightened',
                 'sussed', 'expert']


def sa(text, method):
    nb_capital_letter, nb_exclamations_mark, words_feature, inv = tweets_preprocessing.preprocess(text)

    if method  ==  "POMS":
        sentiment = poms_sa(words_feature, nb_capital_letter, nb_exclamations_mark, inv)
    else:
        sentiment = lexicon_based_sent(words_feature, nb_capital_letter, nb_exclamations_mark, inv)

    return sentiment


def poms_sa(words_feature, nb_capital_letter, nb_exclamations_mark, inv):
    tension = 0
    depression = 0
    anger = 0
    vigor = 0
    fatigue = 0
    confusion = 0

    for word in words_feature:
        if word in TENSION:
            tension += 1
        elif word in TENSION_OPP:
            tension += 1
        elif word in DEPRESSION:
            depression += 1
        elif word in DEPRESSION_OPP:
            depression += 1
        elif word in ANGER:
            anger += 1
        elif word in ANGER_OPP:
            anger += 1
        elif word in VIGOR:
            vigor += 1
        elif word in VIGOR_OPP:
            vigor += 1
        elif word in FATIGUE:
            fatigue += 1
        elif word in FATIGUE_OPP:
            fatigue += 1
        elif word in CONFUSION:
            confusion += 1
        elif word in CONFUSION_OPP:
            confusion += 1

    return [tension, depression, anger, vigor, fatigue, confusion]


def lexicon_based_sent(words_feature, nb_capital_letter, nb_exclamations_mark, inv):
    tweet_score = 0
    for word in words_feature:
        p_score, n_score = sentiwordnet.get_scores("SentiWordNet.txt", word)
        tweet_score = tweet_score - n_score + p_score
    pass
