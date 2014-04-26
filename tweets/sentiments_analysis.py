__author__ = 'maud'

import tweets_nlp
import datetime


def analyse(tweets, method):
    daily_volume = {}
    daily_tweetos = {}
    daily_tweetos_count = {}
    tweetos_power = {}
    daily_tot_followers = {}
    daily_sent = {}
    for ts, text, userid, nb_followers in tweets:

        day = extract_date(ts)
        sent = tweets_nlp.sa(text, method)
        
        if day in daily_sent:
            daily_sent[day].append(sent)
        else:
            daily_sent[day] = [sent]

        if userid not in tweetos_power:
            tweetos_power[userid] = nb_followers

        if day in daily_tweetos:
            if userid not in daily_tweetos[day]:
                daily_tweetos[day].append(userid)
                daily_tweetos_count[day] += 1
        else:
            daily_tweetos[day] = [userid]
            daily_tweetos_count[day] = 1


    total_followers = 0
    for day in daily_tweetos:
        for user in daily_tweetos[day]:
            user_followers = tweetos_power[user]
            total_followers += user_followers
        daily_tot_followers[day] = total_followers

    daily_sent_final = postprocess_daily_sent(daily_sent, method, daily_volume, daily_tweetos_count, daily_tot_followers)
    
    return daily_sent_final

def postprocess_daily_sent(daily_sent, method, daily_tweetos_count, daily_tot_followers):
    results = []
    if method == 'POMS':

        for day in daily_sent:
            if day in daily_tweetos_count:
                tweetos = daily_tweetos_count[day]
            else:
                tweetos = 0

            if day in daily_tot_followers:
                followers = daily_tot_followers[day]
            else:
                followers = 0


            daily_tension = 0
            daily_depression = 0
            daily_anger = 0
            daily_vigor = 0
            daily_fatigue = 0
            daily_confusion = 0
            daily_tweets = 0
            for pom in daily_sent[day]:
                tension, depression, anger, vigor, fatigue, confusion = pom
                daily_tension += tension
                daily_depression += depression
                daily_confusion += confusion
                daily_anger += anger
                daily_vigor += vigor
                daily_fatigue += fatigue
                daily_tweets += 1
            daily_tension /= daily_tweets
            daily_depression /= daily_tweets
            daily_fatigue /= daily_tweets
            daily_anger /= daily_tweets
            daily_vigor /= daily_tweets
            daily_confusion /= daily_tweets
            results.append([day, tweetos, followers, daily_tweets, daily_tension,daily_depression, daily_anger, daily_vigor, daily_fatigue, daily_confusion])

    else:
        for day in daily_sent:
            if day in daily_tweetos_count:
                tweetos = daily_tweetos_count[day]
            else:
                tweetos = 0

            if day in daily_tot_followers:
                followers = daily_tot_followers[day]
            else:
                followers = 0

            daily_tweets = len(daily_sent[day])
            avg_score = sum(daily_sent[day]) / float(daily_tweets)
            results.append([day, tweetos, followers, daily_tweets, avg_score])

    return results

def extract_date(ts):
    day = datetime.datetime.fromtimestamp(int(ts)).strftime("%Y-%m-%d")
    return day