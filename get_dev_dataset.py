import re
import get_reddit_posts as grp
import requests
import reddit_access as ra
import pandas as pd
import time

def requests_remaining():
    '''
    note to self: use ratelimit to stop the program when the limit is reached
    then use different function for reset time to know when to start again
    '''
    headers = ra.get_token()
    ratelimit_remaining = requests.get('https://oauth.reddit.com/', headers=headers).headers['x-ratelimit-remaining']
    print(f'Requests remaining: {ratelimit_remaining}')

def reset_time():
    headers = ra.get_token()
    ratelimit_reset = requests.get('https://oauth.reddit.com/', headers=headers).headers['x-ratelimit-reset']
    print(f'Reset time: {ratelimit_reset}')


africa = ['Algeria', 'Angola', 'Benin', 'Botswana', 'BurkinaFaso', 'Burundi', ['Cameroon', 'Cameroun'], ['Canarias', 'IslasCanarias', 'CanaryIslands'], ['CapeVerde', 'CaboVerde'], 'ChadNews', 'Comoros', 'Congo', 'RepublicofCongo', ['Cotedivoire', 'IvoryCoast'], 'Djibouti', ['Egypt', 'EgyptStreets'], 'Eritrea', 'EquatorialGuinea', 'Ethiopia', 'Ghana', 'Guinea', ['GuineBissau', 'GuineaBissau'], 'Kenya', 'Lesotho', 'Liberia', 'Libya', 'Madagascar', 'Malawi', 'Mali', 'Mauritania', 'mauritius', 'Morocco', 'Mozambique', 'Namibia', 'Niger', 'Nigeria', 'reunionisland', 'Rwanda', 'SaoTomePrincipe', 'Senegal', 'Seychelles', 'SierraLeone', 'Somalia', 'Somaliland', 'southafrica', 'SouthSudan', 'Sudan', 'Swaziland', 'tanzania', ['Gambia', 'The_Gambia'], 'Togo', 'TristanDaCunha', ['Tunisia', 'TUN'], 'Uganda', 'WesternSahara', 'Zambia', 'Zimbabwe']
asia = ['afghanistan', 'armenia', 'azerbaijan', 'Bahrain', 'bangladesh', 'bhutan', 'Brunei', 'cambodia', 'myanmar', 'China', 'Abkhazia', 'Sakartvelo', ['india', 'indiasocial'], 'indonesia', ['iran', 'iranian'], 'Iraq', 'Israel', 'japan', 'jordan', 'Kazakhstan', 'northkorea', ['korea', 'southkorea', 'South_Korea'], 'kurdistan', 'Kuwait', 'Kyrgyzstan', 'laos', 'lebanon', 'malaysia', 'maldives', 'mongolia', 'Nepal', 'Oman', 'pakistan', 'Palestine', 'Philippines', 'qatar', ['saudiarabia', 'KingdomofSaudiArabia'], 'singapore', 'srilanka', 'Syria', ['taiwan', 'RepublicOfChina'], 'Tajikistan', 'Thailand', ['Timor', 'timorleste'], 'Turkmenistan', 'UAE', 'Uzbekistan', 'VietNam', 'Yemen']
europe = ['albania', 'andorra', 'Austria', 'belarus', 'belgium', 'bosnia', 'croatia', 'cyprus', 'czech', 'Denmark', 'Eesti', 'FaroeIslands', 'Finland', 'germany', 'gibraltar', 'greece', 'greenland', 'Iceland', 'ireland', 'italy', 'kosovo', 'latvia', 'liechtenstein', 'lithuania', 'Luxembourg', 'Madeira', 'malta', 'Monaco', 'montenegro', ['thenetherlands', 'Netherlands'], 'macedonia', 'Norway', 'poland', 'portugal', 'Romania', 'russia', 'San_Marino', 'serbia', 'Slovakia', 'Slovenia', 'spain', 'sweden', ['Switzerland', 'suisse'], 'Transnistria', 'Turkey', ['ukraine', 'ukraina'], ['unitedkingdom', 'Britain', 'england', 'northernireland', 'Scotland', 'Wales'], 'vatican']
central_america = ['anguilla', 'Aruba', 'bahamas', 'bermuda', 'Barbados', 'Belize', 'CaymanIslands', ['costa_rica', 'costarica'], 'cuba', 'curacao', 'Dominica', 'Dominican', 'ElSalvador', 'guatemala', 'haiti', 'Honduras', 'Jamaica', 'Nicaragua', 'StLucia', 'StKitts', 'TrinidadandTobago', 'PuertoRico', 'virginislands', 'TurksAndCaicos']
north_america = ['canada', ['unitedstatesofamerica', 'TheUnitedStates']]
oceania = [['australia', 'australian'], 'CookIslands', 'easterisland', 'micronesia', 'Fijian', 'guam', 'Kiribati', 'MarshallIslands', 'newzealand', 'nauru', 'Niue', ['Saipan', 'CNMI'], 'Palau', ['PNG', 'PapuaNewGuinea'], 'Samoa', 'Solomon_Islands', 'Tahiti', 'tokelau', 'Tonga', 'Tuvalu', 'vanuatu', 'westpapua']
south_america = ['BOLIVIA', 'Brazil', 'chile', 'Colombia', 'ecuador', 'falklandislands', 'Grenada', 'Guyana', 'Paraguay', 'PERU', 'Suriname', 'vzla']
artics = ['arcticcircle', 'antarctica']

continents = [africa, asia, europe, central_america, north_america, oceania, south_america, artics]

def get_dev_dataset():
    '''
    This function is used to get a dataset of 100 posts from each subreddit in the list of subreddits
    '''
    starttime = time.time()
    data = pd.DataFrame()
    for continent in continents:
        requests_remaining()
        reset_time()
        for country in continent:
            print(f'Working on country: {country}')
            if type(country) == list:
                for sub in country:
                    data = data.append(grp.get_posts(sub))
            else:
                data = data.append(grp.get_posts(country))
        
        print(f'Time taken: {time.time() - starttime}')
    return data

df_dev = get_dev_dataset()
df_dev.to_csv('dev_dataset.csv', index=False)