import requests
import re
import webbrowser
import pyperclip
from datetime import date
# https://c.fandom.com/wiki/Special:AllMessages?prefix=cnw-vertical-id-
verticalToHub = {
    0: 'other',
    1: 'tv',
    2: 'games',
    3: 'books',
    4: 'comics',
    5: 'lifestyle',
    6: 'music',
    7: 'movies',
    8: 'anime'
}
adoptionInfo = {
        # lang: [wiki, lang, namespace]
        'en': ['community', '', '118'],
        'es': ['comunidad', '', '116'],
        'de': ['community', 'de', '118'],
        'fr': ['communaute', 'fr', '116'],
        # 'ru' # nonstandard format
        'it': ['community', 'it', '118'],
        'pl': ['spolecznosc', '', '114'],
        'nl': ['community', 'nl', '114'],
        'pt': ['comunidade', '', '118'],
        'zh': ['community', 'zh', '112']
}
def urlseperatelang(meshurl):
    lang = ''
    if '.' in meshurl:
        lang = meshurl.split('.')[0]
        meshurl = meshurl[len(lang) + 1:]
    return (meshurl,lang)
def getCityInfoJson(cityId):
    return requests.get(
        'https://community.fandom.com/wikia.php?controller=DWDimensionApi&method=getWikis&limit=1&after_wiki_id=%d' % (
                    cityId - 1)).json()[0]
def createinfotemplate(meshurl,doubleclip=False):
    url,lang = urlseperatelang(meshurl)

    data = requests.get(
        'https://%s.fandom.com/%s/api.php?format=json&action=query&meta=siteinfo&siprop=general|statistics|variables' % (
        url, lang)).json()['query']

    cityId = next((x for x in data['variables'] if x['id'] == 'wgCityId'), None)['*']

    dw = getCityInfoJson(cityId)

    infobox = {
        'name': data['general']['sitename'],
        'badge': [],
        'URL': (lang and f'{lang}.' or '') + data['general']['servername'].split('.')[0],  # community.fandom.com
        'dbname': data['general']['logo'].split('/')[3],  # https://images.wikia.com/central/images/b/bc/Wiki.png
        'path-prefix': data['general']['logo'].split('/')[4] if data['general']['logo'].split('/')[
                                                                    4] != 'images' else None,
        # non-en wikis like https://images.wikia.com/amongus/es/images/b/bc/Wiki.png
        'language': data['general']['lang'],
        'articles': data['statistics']['articles'],
        'founded': dw['created_at'],
        'founder': dw['founding_user_id'] != '0' and requests.get(
            'https://community.fandom.com/api.php?format=json&action=query&list=users&ususerids=' + dw[
                'founding_user_id']).json()['query']['users'][0]['name'] or None,
        'adopted': None,
        'adopter': None,
        'id': cityId,
        'hub': verticalToHub[int(dw['vertical_id'])],
        'checked': date.today().strftime("%Y-%m-%d")
    }

    if data['general']['gamepedia'] == 'true':
        infobox['badge'].append('gamepedia')

    cnw = requests.get(
        'https://community.fandom.com/wikia.php?controller=Fandom\CreateNewWiki\Builder\CreateNewWiki&method=checkDomain&format=json&name=%s&lang=%s' % (
        data['general']['servername'].split('.')[0], infobox['language'])).json()
    if cnw['potential_duplicates'][0]['wikiOfficial'] == True:
        infobox['badge'].append('official')


    adopt = adoptionInfo[
        next((k for k in adoptionInfo.keys() if k.startswith(infobox['language'].split('-')[0])), 'en')]

    for attempt in requests.get(
            f'https://{adopt[0]}.fandom.com/{adopt[1]}/api.php?format=json&action=query&list=allpages&apdir=descending&apnamespace={adopt[2]}&apprefix=' + (
                    adopt == adoptionInfo['en'] and infobox['name'] or infobox['name'].replace('Wiki', ''))).json()['query']['allpages']:  # non-en requests seem to not have wiki in the name?
        req = requests.get(
            f'https://{adopt[0]}.fandom.com/{adopt[1]}/api.php?format=json&formatversion=2&action=query&prop=revisions&rvlimit=1&rvprop=content|user&rvdir=newer&titles=' +
            attempt['title']).json()['query']['pages'][0]['revisions'][0]
        if re.search('https?:\/\/' + (lang and f"(({lang}|{infobox['language']})\.)?" or '') +
                     data['general']['servername'].split('.')[0] + '\.(fandom|wikia)\.(com|org)' + (
                             lang and f"(\/({lang}|{infobox['language']}))?" or ''),
                     req['content']):  # this wiki was mentioned
            user = req['user']
            log = requests.get(data['general']['server'] + data['general'][
                'scriptpath'] + '/api.php?format=json&action=query&list=logevents&leaction=rights/rights&letitle=User:' + user).json()[
                'query']['logevents']
            if not log:
                # they didn't adopt it, try the next page
                continue
            if 'bureaucrat' in log[0]['params']['newgroups']:
                # they are still a bcrat, find when it was added
                action = next((x for x in reversed(log) if
                               next((y for y in x['params']['newmetadata'] if y['group'] == 'bureaucrat'), None)), None)

                infobox['adopted'] = action['timestamp'].replace('T', ' ').replace('Z', '')
                infobox['adopter'] = user
                break
    template = '{{Infobox wiki\n'
    for key, value in infobox.items():
        if value:
            if type(value) is list:
                value = ','.join(value)
            template += f'|{key} = {value}\n'
    template += '}}'
    if(doubleclip):
        return (template,infobox["name"])
    else: 
        return (template,)


doubleclipmode=input("Activate Double Clip mode (Copy the name, then the template)?[Y/N]:")=="Y"
holdercachemode=False
urlcache=[]
while True:
    url = input('Input wiki: ')
    if not url and not holdercachemode:
        break
    data=createinfotemplate(url,doubleclipmode)
    if(doubleclipmode):
        pyperclip.copy(data[1])
        input("Name Copied! [Waiting for enter to copy template]")
    pyperclip.copy(data[0])
    print("Template copied!")