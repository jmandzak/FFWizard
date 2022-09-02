import pandas as pd
import math
from data.positions import *

def GetPlayers(ppr=0):
    player_df = pd.read_csv("Stats/master_sheet.csv")
    pd.set_option("display.max_rows", None,)
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
            QBs.append(player)
            player.position = 'QB'
            CalcCompositeOverall(player)
            all_players.append(player)
        
        if stats['POS'] == 'RB':
            player = MakeRB(name, stats, ppr)
            RBs.append(player)
            player.position = 'RB'
            CalcCompositeOverall(player)
            all_players.append(player)
        
        if stats['POS'] == 'WR':
            player = MakeWR(name, stats, ppr)
            WRs.append(player)
            player.position = 'WR'
            CalcCompositeOverall(player)
            all_players.append(player)
        
        if stats['POS'] == 'TE':
            player = MakeTE(name, stats, ppr)
            TEs.append(player)
            player.position = 'TE'
            CalcCompositeOverall(player)
            all_players.append(player)
        
        if stats['POS'] == 'DEF':
            player = MakeDEF(name, stats)
            DEFs.append(player)
            player.position = 'DEF'
            CalcCompositeOverall(player)
            all_players.append(player)
        
        if stats['POS'] == 'K':
            player = MakeK(name, stats)
            Ks.append(player)
            player.position = 'K'
            CalcCompositeOverall(player)
            all_players.append(player)

    return all_players, QBs, RBs, WRs, TEs, Ks, DEFs
        

def MakeQB(name, stats):
    player = QB()
    player.name = name
    player.proTeam = stats['TEAM']
    player.fullSos = stats['FULL_SOS']
    player.seasonSos = stats['SEASON_SOS']
    player.playoffSos = stats['PLAYOFF_SOS']
    player.starter = stats['STARTER']
    player.boom = stats['BOOM']
    player.bust = stats['BUST']
    player.depth = int(stats['DEPTH'])

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
    player.passInt = stats['AVG_INT']
    player.rushAtt = stats['AVG_RUSH_ATT']
    player.rushYard = stats['AVG_RUSH_YDS']
    player.rushTD = stats['AVG_RUSH_TDS']

    CalcCompositePos(player)
    return player

def MakeRB(name, stats, ppr):
    player = RB()
    player.name = name
    player.proTeam = stats['TEAM']
    player.fullSos = stats['FULL_SOS']
    player.seasonSos = stats['SEASON_SOS']
    player.playoffSos = stats['PLAYOFF_SOS']
    player.starter = stats['STARTER']
    player.boom = stats['BOOM']
    player.bust = stats['BUST']
    player.depth = int(stats['DEPTH'])

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
    player.recTarget = stats['AVG_TGT']
    player.receptions = stats['AVG_REC']
    player.recYard = stats['AVG_REC_YDS']
    player.recTD = stats['AVG_REC_TDS']

    CalcCompositePos(player)
    return player

def MakeWR(name, stats, ppr):
    player = WR()
    player.name = name
    player.proTeam = stats['TEAM']
    player.fullSos = stats['FULL_SOS']
    player.seasonSos = stats['SEASON_SOS']
    player.playoffSos = stats['PLAYOFF_SOS']
    player.starter = stats['STARTER']
    player.boom = stats['BOOM']
    player.bust = stats['BUST']
    player.depth = int(stats['DEPTH'])

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
    player.recTarget = stats['AVG_TGT']
    player.receptions = stats['AVG_REC']
    player.recYard = stats['AVG_REC_YDS']
    player.recTD = stats['AVG_REC_TDS']

    CalcCompositePos(player)
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

    CalcCompositePos(player)
    return player

def MakeK(name, stats):
    player = K()
    player.name = name
    player.proTeam = stats['TEAM']
    player.fullSos = stats['FULL_SOS']
    player.seasonSos = stats['SEASON_SOS']
    player.playoffSos = stats['PLAYOFF_SOS']
    player.starter = stats['STARTER']
    player.boom = stats['BOOM']
    player.bust = stats['BUST']

    player.pastPPG = stats['AVG_FAN PTS']
    player.avgRank = stats['AVG_RK']
    player.avgPosRank = stats['POS_AVG.']
    player.tier = stats['TIERS']
    player.posTier = stats['POS_TIERS']
    player.std_dev = stats['STD.DEV_RK']
    player.pos_std_dev = stats['POS_STD.DEV']

    player.EPA = stats['AVG_XPA']
    player.EPM = stats['AVG_XPM']

    CalcCompositePos(player)
    return player

def CalcCompositePos(player):
    if player.avgPosRank != 500 and player.avgRank != 500:
        player.composite = player.avgPosRank * 2 + player.posTier + (player.fullSos / 8)
        player.composite = round(player.composite, 2)

    return player

def CalcCompositeOverall(player):
    if player.avgRank != 500:
        player.compositeOverall = player.avgRank * 2 + player.tier + (player.fullSos / 8)
        player.compositeOverall = round(player.compositeOverall, 2)

    return player