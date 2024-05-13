from virtual import FootballLeague
import copy




# league = FootballLeague()
# league.setup_fixture()

# print(league)
# # # print(league.teams)
# # #print(league.standings)
# # print(len(league.fixtures))
# # for f in league.fixtures:
# #     print(f)
# #     print()



TEAMS = [
                            'ARS', 'AST', 'BHA', 'BOU',  
                            'BRE', 'BUR', 'CHE', 'CRY', 
                            'EVE', 'FOR', 'FUL', 'LIV', 
                            'LUT', 'MCI', 'MUN', 'NEW', 
                            'SHU', 'TOT', 'WHU', 'WOL'
                        ]


print(TEAMS)
fix = set()
helper = copy.deepcopy(TEAMS)
for x in TEAMS:
    for i in helper:
        if x == i:
            continue
        print((x, i))
        fix.add((x, i))



# print(fix)
print(len(fix))