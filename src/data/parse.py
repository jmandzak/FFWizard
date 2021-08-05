import pandas as pd
import math
from data.positions import *

def GetPlayers(ppr=0):
    player_df = pd.read_csv("Stats/master_sheet.csv")
    pd.set_option("display.max_rows", None,)
    print(player_df.index[player_df.index.duplicated()].unique())
    player_df.set_index('PLAYER NAME', inplace=True)
    players = player_df.to_dict('index')
    QBs = []
    RBs = []
    WRs = []
    TEs = []
    DEFs = []
    Ks = []
    all_players = []
    
    for name, stats in players.items():
        if stats['POS'] == 'UNKNOWN' or name is None:
            continue

        if stats['POS'] == 'QB':
            player = MakeQB(name, stats)
            player.position = 'QB'
            all_players.append(player)
            QBs.append(player)
        
        if stats['POS'] == 'RB':
            player = MakeRB(name, stats, ppr)
            player.position = 'RB'
            all_players.append(player)
            RBs.append(player)
        
        if stats['POS'] == 'WR':
            player = MakeWR(name, stats, ppr)
            player.position = 'WR'
            all_players.append(player)
            WRs.append(player)
        
        if stats['POS'] == 'TE':
            player = MakeTE(name, stats, ppr)
            player.position = 'TE'
            all_players.append(player)
            TEs.append(player)
        
        if stats['POS'] == 'DEF':
            player = MakeDEF(name, stats)
            player.position = 'DEF'
            all_players.append(player)
            DEFs.append(player)
        
        if stats['POS'] == 'K':
            player = MakeK(name, stats)
            player.position = 'K'
            all_players.append(player)
            Ks.append(player)

    return all_players, QBs, RBs, WRs, TEs, Ks, DEFs
        

def MakeQB(name, stats):
    player = QB()
    player.name = name
    player.proTeam = stats['TEAM']
    player.fullSos = stats['FULL_SOS']
    player.seasonSos = stats['SEASON_SOS']
    player.playoffSos = stats['PLAYOFF_SOS']

    player.pastPPG = stats['AVG_FAN PTS']
    player.avgRank = stats['AVG_RK']
    player.avgPosRank = stats['POS_AVG.']
    player.tier = stats['TIERS']
    player.posTier = stats['POS_TIERS']
    player.std_dev = stats['STD.DEV_RK']
    player.pos_std_dev = stats['POS_STD.DEV']

    # position specific
    player.passYard = stats['AVG_PASS_YDS']
    player.passTD = stats['AVG_PASS_TDS']
    player.passInt = stats['AVG_PASS_INT']
    player.rushAtt = stats['AVG_RUSH_ATT']
    player.rushYard = stats['AVG_RUSH_YDS']
    player.rushTD = stats['AVG_RUSH_TDS']

    CalcComposite(player)
    return player

def MakeRB(name, stats, ppr):
    player = RB()
    player.name = name
    player.proTeam = stats['TEAM']
    player.fullSos = stats['FULL_SOS']
    player.seasonSos = stats['SEASON_SOS']
    player.playoffSos = stats['PLAYOFF_SOS']

    # ppr specific
    if ppr:
        player.pastPPG = stats['PPR_AVG_FAN PTS']
        player.avgRank = stats['PPR_AVG_RK']
        player.avgPosRank = stats['PPR_POS_AVG.']
        player.tier = stats['PPR_TIERS']
        player.posTier = stats['PPR_POS_TIERS']
        player.std_dev = stats['PPR_STD.DEV_RK']
        player.pos_std_dev = stats['PPR_POS_STD.DEV']

    # position specific
    player.rushAtt = stats['AVG_RUSH_ATT']
    player.rushYard = stats['AVG_RUSH_YDS']
    player.rushTD = stats['AVG_RUSH_TDS']
    player.recTarget = stats['AVG_REC_TGT']
    player.receptions = stats['AVG_REC']
    player.recYard = stats['AVG_REC_YDS']
    player.recTD = stats['AVG_REC_TDS']

    CalcComposite(player)
    return player

def MakeWR(name, stats, ppr):
    player = WR()
    player.name = name
    player.proTeam = stats['TEAM']
    player.fullSos = stats['FULL_SOS']
    player.seasonSos = stats['SEASON_SOS']
    player.playoffSos = stats['PLAYOFF_SOS']

    # ppr specific
    if ppr:
        player.pastPPG = stats['PPR_AVG_FAN PTS']
        player.avgRank = stats['PPR_AVG_RK']
        player.avgPosRank = stats['PPR_POS_AVG.']
        print(player.name, ': ', player.avgPosRank)
        player.tier = stats['PPR_TIERS']
        player.posTier = stats['PPR_POS_TIERS']
        player.std_dev = stats['PPR_STD.DEV_RK']
        player.pos_std_dev = stats['PPR_POS_STD.DEV']

    # position specific
    player.recTarget = stats['AVG_REC_TGT']
    player.receptions = stats['AVG_REC']
    player.recYard = stats['AVG_REC_YDS']
    player.recTD = stats['AVG_REC_TDS']

    CalcComposite(player)
    return player

def MakeTE(name, stats, ppr):
    return MakeWR(name, stats, ppr)

def MakeDEF(name, stats):
    player = Defense()
    player.name = name
    player.fullSos = stats['FULL_SOS']
    player.seasonSos = stats['SEASON_SOS']
    player.playoffSos = stats['PLAYOFF_SOS']

    player.pastPPG = stats['AVG_FAN PTS']
    player.avgRank = stats['AVG_RK']
    player.avgPosRank = stats['POS_AVG.']
    player.tier = stats['TIERS']
    player.posTier = stats['POS_TIERS']
    player.std_dev = stats['STD.DEV_RK']
    player.pos_std_dev = stats['POS_STD.DEV']

    if not math.isnan(stats['SACK']):
        player.sack = stats['SACK']
    if not math.isnan(stats['FUMR']):
        player.FR = stats['FUMR']
    if not math.isnan(stats['INT']):
        player.intercept = stats['INT']
    if not math.isnan(stats['DEF TD']):
        player.TD = stats['DEF TD']
    if not math.isnan(stats['RET TD']):
        player.kickTD = stats['RET TD']

    CalcComposite(player)
    return player

def MakeK(name, stats):
    player = K()
    player.name = name
    player.proTeam = stats['TEAM']
    player.fullSos = stats['FULL_SOS']
    player.seasonSos = stats['SEASON_SOS']
    player.playoffSos = stats['PLAYOFF_SOS']

    player.pastPPG = stats['AVG_FAN PTS']
    player.avgRank = stats['AVG_RK']
    player.avgPosRank = stats['POS_AVG.']
    player.tier = stats['TIERS']
    player.posTier = stats['POS_TIERS']
    player.std_dev = stats['STD.DEV_RK']
    player.pos_std_dev = stats['POS_STD.DEV']

    player.EPA = stats['AVG_XPA']
    player.EPM = stats['AVG_XPM']

    CalcComposite(player)
    return player

def CalcComposite(player):
    if player.avgPosRank != 500 and player.avgRank != 500:
        player.composite = player.avgPosRank + player.avgRank + player.std_dev + player.pos_std_dev + player.tier + player.posTier + (player.fullSos / 4)
        player.composite = round(player.composite, 2)

    return player