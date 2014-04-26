__author__ = 'maud'

import sys
import tweets_parser
import configparser
import sentiments_analysis


def main():
    config = configparser.ConfigParser()
    config.read('config.ini')
    data_path = config['PATHS']['file_path_intel']
    method = config['SENTIMENTS']['method']
    tweets = tweets_parser.import_file(data_path)
    daily_volume, daily_tweetos, daily_avg_power, daily_sent = sentiments_analysis.analyse(tweets, method)

if __name__ == "__main__":
    main()