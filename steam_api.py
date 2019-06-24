import requests, re
from bs4 import BeautifulSoup

adduserurl = 'https://partner.steamgames.com/pub/ajaxadduser/88757/'
cookie = 'sessionid=949324b4662d5cc26a90cb0c; steamMachineAuth76561198802018074=1F51DF05E8C2CF584B09813F3CE9587FD13C5112; requestedPrimaryPublisher=88757; steamLoginSecure=76561198972162041%7C%7C5C253AEDE1B78FE07419898581E38D64518F7398%7C%7C30ff7906af6996ef513a063bc108e355; steamMachineAuth76561198972162041=D4788769CFEE9734AF984763499AE6340F1C7751; _ga=GA1.2.548426798.1561368228; _gid=GA1.2.449321792.1561368228'

getlinkurl = 'https://partner.steamgames.com/pub/users/88757/'

delurl = 'https://partner.steamgames.com/pub/ajaxdeleteuser/88757/'


def addUser(login):
    data = {
        'sessionid': '949324b4662d5cc26a90cb0c',
        'accountname': login,
        'realname': login,
        'emailaddr': login,
        'notes': ''
}
    headers = {
        'cookie': cookie,
        'origin': 'https://partner.steamgames.com',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'referer': 'https://partner.steamgames.com/pub/users/88757',
        'authority': 'partner.steamgames.com',
        'x-requested-with': 'XMLHttpRequest'}
    r = requests.post(adduserurl, data=data, headers=headers)

def getlink(login):
    headers = {
        'cookie': cookie,
        'origin': 'https://partner.steamgames.com',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'referer': 'https://partner.steamgames.com/pub/users/88757',
        'authority': 'partner.steamgames.com',
        'x-requested-with': 'XMLHttpRequest'}
    r = requests.get(getlinkurl, headers=headers)
    id = re.search('{},{},{},{},\d+'.format(login, login, login, login), r.text).group().split(',')[-1]
    soup = BeautifulSoup(r.text, 'lxml')
    delid = soup.find('div', {'data-filter-meta':'{},{},{},{},{}'.format(login, login, login, login, id)}).get('id').replace('user_', '')
    r = requests.post(delurl, headers=headers, data={'victim':delid,
                                                    'sessionid':'949324b4662d5cc26a90cb0c'})
    return 'https://steamcommunity.com/profiles/'+id


def main(login):
    addUser(login)
    return getlink(login)
