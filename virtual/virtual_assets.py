url = "https://www.sportybet.com/ng/sport/vFootball/sv:category:202120001/sv:league:1"


instant = "https://www.sportybet.com/ng/instant-virtuals/"


PL_TEAMS = [
                'Arsenal', 'Aston Villa', 'Brentford', 'Brighton & Hove Albion', 
                'Burnley', 'Chelsea', 'Crystal Palace', 'Everton', 
                'Leeds United', 'Leicester City', 'Liverpool', 'Manchester City', 
                'Manchester United', 'Newcastle United', 'Norwich City', 'Southampton', 
                'Tottenham Hotspur', 'Watford', 'West Ham United', 'Wolverhampton Wanderers'
            ]

EPL_TEAMS_ABBR = [
                    'ARS', 'AST', 'BRE', 'BHA', 
                    'BUR', 'CHE', 'CRY', 'EVE', 
                    'LDU', 'LEI', 'LIV', 'MCI', 
                    'MUN', 'NEW', 'NOR', 'SOU', 
                    'TOT', 'WAT', 'WHU', 'WOL'
                ]

VIRTUAL_EPL_TEAMS = [
                        'Arsenal', 'Aston Villa', 'Brighton & Hove Albion', 'Bournemouth FC',
                        'Brentford', 'Burnley', 'Chelsea', 'Crystal Palace', 
                        'Everton', 'FOR', 'Fulham FC',  'Liverpool', 
                        'Luton Town', 'Manchester City', 'Manchester United', 'Newcastle United',
                        'Sheffield United', 'Tottenham Hotspur', 'West Ham United', 'Wolverhampton Wanderers'
                    ]

VIRTUAL_EPL_TEAMS_ABBR = [
                            'ARS', 'AST', 'BHA', 'BOU',  
                            'BRE', 'BUR', 'CHE', 'CRY', 
                            'EVE', 'FOR', 'FUL', 'LIV', 
                            'LUT', 'MCI', 'MUN', 'NEW', 
                            'SHU', 'TOT', 'WHU', 'WOL'
                        ]


VIRTUAL_EPL_TEAMS_ENCODED = {
                            'ARS': [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
                            'AST': [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
                            'BHA': [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
                            'BOU': [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],  
                            'BRE': [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
                            'BUR': [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
                            'CHE': [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0], 
                            'CRY': [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0], 
                            'EVE': [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0], 
                            'FOR': [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0], 
                            'FUL': [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0], 
                            'LIV': [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0], 
                            'LUT': [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0], 
                            'MCI': [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0], 
                            'MUN': [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0], 
                            'NEW': [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0], 
                            'SHU': [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0], 
                            'TOT': [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0], 
                            'WHU': [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0], 
                            'WOL': [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
}
