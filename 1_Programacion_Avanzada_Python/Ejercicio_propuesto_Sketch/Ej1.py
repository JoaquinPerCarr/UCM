"""
Program to analyze the logs files of an apache server.
An example of file accompanies this file: access.log
"""
import doctest


def get_user_agent(line: str) -> str:
    """
    Get the user agent of the line.
    :param line: Str with current line
    :return: str with user agent

    Examples
    ---------
    >>> get_user_agent('66.249.66.35 - - [15/Sep/2023:00:18:46 +0200] "GET /~luis/sw05-06/libre_m2_baja.pdf HTTP/1.1" 200 5940849 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"')
    'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'

    >>> get_user_agent('147.96.46.52 - - [10/Oct/2023:12:55:47 +0200] "GET /favicon.ico HTTP/1.1" 404 519 "https://antares.sip.ucm.es/" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0"')
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0'
    """
    user_agent = line.split('"')[5]

    return user_agent


def is_bot(line: str) -> bool:
    """
    Check of the access in the line corresponds to a bot
    :param line: Str with current line
    :return: bool saying if the current line is a bot or not

    Examples
    --------
    >>> is_bot('147.96.46.52 - - [10/Oct/2023:12:55:47 +0200] "GET /favicon.ico HTTP/1.1" 404 519 "https://antares.sip.ucm.es/" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0"')
    False

    >>> is_bot('66.249.66.35 - - [15/Sep/2023:00:18:46 +0200] "GET /~luis/sw05-06/libre_m2_baja.pdf HTTP/1.1" 200 5940849 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"')
    True

    >>> is_bot('213.180.203.109 - - [15/Sep/2023:00:12:18 +0200] "GET /robots.txt HTTP/1.1" 302 567 "-" "Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)"')
    True
    """
    bot: bool = False
    # Check if any of these statements are in the text
    if "Bot" in line or "bot" in line:
        bot = True

    return bot


def get_ipaddr(line):
    """
    Gets the IP address of the line
    :param line: str with all the line
    :return: str: IP address

    Examples
    --------
    >>> get_ipaddr('213.180.203.109 - - [15/Sep/2023:00:12:18 +0200] "GET /robots.txt HTTP/1.1" 302 567 "-" "Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)"')
    '213.180.203.109'

    >>> get_ipaddr('147.96.46.52 - - [10/Oct/2023:12:55:47 +0200] "GET /favicon.ico HTTP/1.1" 404 519 "https://antares.sip.ucm.es/" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0"')
    '147.96.46.52'
    """
    get_ip_address = line.split('- -')[0].strip()

    return get_ip_address


def get_hour(line: str) -> int:
    """
    Get the hour of the line.
    :param line: Actual line of the access.log
    :return: int with the int value of this line

    Examples
    ---------
    >>> get_hour('66.249.66.35 - - [15/Sep/2023:00:18:46 +0200] "GET /~luis/sw05-06/libre_m2_baja.pdf HTTP/1.1" 200 5940849 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"')
    0

    >>> get_hour('147.96.46.52 - - [10/Oct/2023:12:55:47 +0200] "GET /favicon.ico HTTP/1.1" 404 519 "https://antacres.sip.ucm.es/" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0"')
    12
    """
    hour = line.split(':')[1]

    return int(hour)


def histbyhour(filename: str) -> dict[int, int]:
    """
    Computes the histogram of access by hour
    :param filename: The name of the file to process
    :return: A dictionary where keys are hours (as integers) and values are access counts
    """
    hour_list = []
    with open(filename, 'r') as file:  # Open file in reader ('r') mode.
        for line in file:
            hour = get_hour(line)  # Get the hour in .log
            hour_list.append(hour)  # Fill the list with all hours in .log file

    dic_hour = {}  # Empty dic.
    for h in hour_list:
        if h in dic_hour:
            dic_hour[h] += 1
        else:
            dic_hour[h] = 1

    return dic_hour


def ipaddreses(filename: str) -> set[str]:
    """
    Returns a list of IP addresses that are not bots.
    :param filename:
    :return:
    """
    ip_list_no_bot = []
    with open(filename, 'r') as file:  # Open file in reader ('r') mode.
        for line in file:
            bot = is_bot(line)  # Bool with true or false statement about if the line contain a bot or not
            if not bot:  # bot == True
                ip_list_no_bot.append(get_ipaddr(line).strip())

    ip_list_unique = set(ip_list_no_bot)
    ip_list_unique = list(ip_list_unique)
    return set(ip_list_unique)


def test_doc():
    doctest.run_docstring_examples(get_user_agent, globals(), verbose=True)
    doctest.run_docstring_examples(is_bot, globals(), verbose=True)
    doctest.run_docstring_examples(get_ipaddr, globals(), verbose=True)
    doctest.run_docstring_examples(get_hour, globals(), verbose=True)


def test_ipaddresses():
    assert ipaddreses('access_short.log') == {'34.105.93.183', '39.103.168.88'}


def test_hist():
    hist = histbyhour('access_short.log')
    assert hist == {5: 3, 7: 2, 23: 1}
