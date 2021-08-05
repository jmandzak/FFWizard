from PyQt5.QtGui import QBrush, QColor
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QWidget, QPushButton, QAbstractItemView
from PyQt5.QtCore import Qt
from data import statsio as parse

def initialize(ppr=0):
    # fixes position multiplier based on PPR
    if ppr:
        parse.posMultiplier['WR'] = 0.95
        parse.posMultiplier['TE'] = 1.1

    # creates empty players dictionary
    players = {}

    # creates empty teams dictionary
    teams = {}

    # calls all functions to fill in dictionaries

    # strength of schedule
    teams = parse.GetSos("Stats/Sos_Full.txt", teams, "full")
    teams = parse.GetSos("Stats/Sos_Season.txt", teams, "season")
    teams = parse.GetSos("Stats/Sos_Playoff.txt", teams, "playoff")

    # past stats
    players, QBs = parse.ReadQB(players)
    players, RBs = parse.ReadRB(players)
    players, WRs = parse.ReadWR(players)
    players, TEs = parse.ReadTE(players)
    players, Ks = parse.ReadK(players)
    players, DEFs = parse.ReadDEF(players)

    # position specific tiers and rank
    # 3 positions are different based on if the league is PPR
    if ppr:
        players, RBs = parse.PosTiers("Stats/PPR_RB_Tiers.txt", players, RBs, "RB")
        players, WRs = parse.PosTiers("Stats/PPR_WR_Tiers.txt", players, WRs, "WR")
        players, TEs = parse.PosTiers("Stats/PPR_TE_Tiers.txt", players, TEs, "TE")
    else:
        players, RBs = parse.PosTiers("Stats/RB_Tiers.txt", players, RBs, "RB")
        players, WRs = parse.PosTiers("Stats/WR_Tiers.txt", players, WRs, "WR")
        players, TEs = parse.PosTiers("Stats/TE_Tiers.txt", players, TEs, "TE")

    players, QBs = parse.PosTiers("Stats/QB_Tiers.txt", players, QBs, "QB")
    players, Ks = parse.PosTiers("Stats/K_Tiers.txt", players, Ks, "K")
    players, DEFs = parse.DEFTiers(players, DEFs)

    # non position specific rank
    if ppr:
        players, QBs, RBs, WRs, TEs, Ks, DEFs = parse.ReadTiers("Stats/PPR_Tiers.txt", players, QBs, RBs, WRs, TEs, Ks, DEFs)
    else:    
        players, QBs, RBs, WRs, TEs, Ks, DEFs = parse.ReadTiers("Stats/Tiers.txt", players, QBs, RBs, WRs, TEs, Ks, DEFs)

    # assigning strength of schedule values
    players, QBs, RBs, WRs, TEs, Ks, DEFs = parse.AssignSos(players, QBs, RBs, WRs, TEs, Ks, DEFs, teams)

    # calculate composite for each player in each dict
    players = parse.CalcComposite(players)
    QBs = parse.CalcComposite(QBs)
    RBs = parse.CalcComposite(RBs)
    WRs = parse.CalcComposite(WRs)
    TEs = parse.CalcComposite(TEs)
    DEFs = parse.CalcComposite(DEFs)
    Ks = parse.CalcComposite(Ks)

    return players, QBs, RBs, WRs, TEs, Ks, DEFs

def create_all_table(players):
        table = QTableWidget()
        table.setRowCount(len(players))
        table.setColumnCount(7)
        table.setHorizontalHeaderLabels(["Name", "Pos.", "Team", "Rank", "Tier", "SoS", "Composite"])

        i = 0
        for player in players.values():
            if player.composite == 10000 or player.tier == 0:
                continue

            table.setItem(i, 0, QTableWidgetItem(player.name))
            table.setItem(i, 1, QTableWidgetItem(player.position))
            table.setItem(i, 2, QTableWidgetItem(player.proTeam))

            item = QTableWidgetItem()
            item.setData(0, player.avgRank)
            table.setItem(i, 3, item)

            item = QTableWidgetItem()
            item.setData(0, player.tier)
            table.setItem(i, 4, item)

            item = QTableWidgetItem()
            item.setData(0, player.fullSos)
            table.setItem(i, 5, item)
            if player.fullSos < 12:
                table.item(i, 5).setBackground(QBrush(QColor("lightgreen")))
            elif player.fullSos < 22:
                table.item(i, 5).setBackground(QBrush(QColor("khaki")))
            else:
                table.item(i, 5).setBackground(QBrush(QColor("indianred")))

            item = QTableWidgetItem()
            item.setData(0, player.composite)
            table.setItem(i, 6, item)

            i += 1

        table.setSortingEnabled(True)
        table.sortByColumn(6, Qt.AscendingOrder)
        table.resizeColumnsToContents()
        table.setSelectionBehavior(QAbstractItemView.SelectRows)
        return table
        
    # create the qb table
def create_QB_table(players):
    table = QTableWidget()
    table.setRowCount(len(players))
    table.setColumnCount(14)
    table.setHorizontalHeaderLabels(["Name", "Team", "Rank", "Pos. Rank", "Tier", "Pos. Tier", "SoS", "Playoff SoS",
                                     "Pass Yards", "Pass TDs", "Interceptions", "Rush Yards", "Rush TDs", "Composite"])

    i = 0
    for player in players.values():
        if player.composite == 10000 or player.tier == 0:
            continue

        table.setItem(i, 0, QTableWidgetItem(player.name))
        table.setItem(i, 1, QTableWidgetItem(player.proTeam))

        item = QTableWidgetItem()
        item.setData(0, player.avgRank)
        table.setItem(i, 2, item)

        item = QTableWidgetItem()
        item.setData(0, player.avgPosRank)
        table.setItem(i, 3, item)

        item = QTableWidgetItem()
        item.setData(0, player.tier)
        table.setItem(i, 4, item)

        item = QTableWidgetItem()
        item.setData(0, player.posTier)
        table.setItem(i, 5, item)

        item = QTableWidgetItem()
        item.setData(0, player.fullSos)
        table.setItem(i, 6, item)
        if player.fullSos < 12:
            table.item(i, 6).setBackground(QBrush(QColor("lightgreen")))
        elif player.fullSos < 22:
            table.item(i, 6).setBackground(QBrush(QColor("khaki")))
        else:
            table.item(i, 6).setBackground(QBrush(QColor("indianred")))

        item = QTableWidgetItem()
        item.setData(0, player.playoffSos)
        table.setItem(i, 7, item)

        item = QTableWidgetItem()
        item.setData(0, float(str(player.passYard).replace(",", "")))
        table.setItem(i, 8, item)

        item = QTableWidgetItem()
        item.setData(0, int(player.passTD))
        table.setItem(i, 9, item)

        item = QTableWidgetItem()
        item.setData(0, int(player.passInt))
        table.setItem(i, 10, item)

        item = QTableWidgetItem()
        item.setData(0, float(str(player.rushYard).replace(",", "")))
        table.setItem(i, 11, item)

        item = QTableWidgetItem()
        item.setData(0, int(player.rushTD))
        table.setItem(i, 12, item)

        item = QTableWidgetItem()
        item.setData(0, player.composite)
        table.setItem(i, 13, item)

        i += 1

    table.setSortingEnabled(True)
    table.sortByColumn(13, Qt.AscendingOrder)
    table.resizeColumnsToContents()
    table.setSelectionBehavior(QAbstractItemView.SelectRows)
    return table

# create the running back table
def create_RB_table(players):
    table = QTableWidget()
    table.setRowCount(len(players))
    table.setColumnCount(15)
    table.setHorizontalHeaderLabels(["Name", "Team", "Rank", "Pos. Rank", "Tier", "Pos. Tier", "SoS", "Playoff SoS",
                                        "Rush Yards", "Rush TDs", "Targets", "Receptions", "Rec. Yards", "Rec. TDs", "Composite"])

    i = 0
    for player in players.values():
        if player.composite == 10000 or player.tier == 0:
            continue

        table.setItem(i, 0, QTableWidgetItem(player.name))
        table.setItem(i, 1, QTableWidgetItem(player.proTeam))

        item = QTableWidgetItem()
        item.setData(0, player.avgRank)
        table.setItem(i, 2, item)

        item = QTableWidgetItem()
        item.setData(0, player.avgPosRank)
        table.setItem(i, 3, item)

        item = QTableWidgetItem()
        item.setData(0, player.tier)
        table.setItem(i, 4, item)

        item = QTableWidgetItem()
        item.setData(0, player.posTier)
        table.setItem(i, 5, item)

        item = QTableWidgetItem()
        item.setData(0, player.fullSos)
        table.setItem(i, 6, item)
        if player.fullSos < 12:
            table.item(i, 6).setBackground(QBrush(QColor("lightgreen")))
        elif player.fullSos < 22:
            table.item(i, 6).setBackground(QBrush(QColor("khaki")))
        else:
            table.item(i, 6).setBackground(QBrush(QColor("indianred")))

        item = QTableWidgetItem()
        item.setData(0, player.playoffSos)
        table.setItem(i, 7, item)

        item = QTableWidgetItem()
        item.setData(0, float(str(player.rushYard).replace(",", "")))
        table.setItem(i, 8, item)

        item = QTableWidgetItem()
        item.setData(0, int(player.rushTD))
        table.setItem(i, 9, item)

        item = QTableWidgetItem()
        item.setData(0, int(player.recTarget))
        table.setItem(i, 10, item)

        item = QTableWidgetItem()
        item.setData(0, int(player.receptions))
        table.setItem(i, 11, item)

        item = QTableWidgetItem()
        item.setData(0, float(str(player.recYard).replace(",", "")))
        table.setItem(i, 12, item)

        item = QTableWidgetItem()
        item.setData(0, int(player.recTD))
        table.setItem(i, 13, item)

        item = QTableWidgetItem()
        item.setData(0, player.composite)
        table.setItem(i, 14, item)

        i += 1

    table.setSortingEnabled(True)
    table.sortByColumn(14, Qt.AscendingOrder)
    table.resizeColumnsToContents()
    table.setSelectionBehavior(QAbstractItemView.SelectRows)
    return table

def create_WR_table(players):
    table = QTableWidget()
    table.setRowCount(len(players))
    table.setColumnCount(15)
    table.setHorizontalHeaderLabels(["Name", "Team", "Rank", "Pos. Rank", "Tier", "Pos. Tier", "SoS", "Playoff SoS",
                                        "Targets", "Receptions", "Rec. Yards", "Rec. TDs", "Rush Yards", "Rush TDs", "Composite"])

    i = 0
    for player in players.values():
        if player.composite == 10000 or player.tier == 0:
            continue

        table.setItem(i, 0, QTableWidgetItem(player.name))
        table.setItem(i, 1, QTableWidgetItem(player.proTeam))

        item = QTableWidgetItem()
        item.setData(0, player.avgRank)
        table.setItem(i, 2, item)

        item = QTableWidgetItem()
        item.setData(0, player.avgPosRank)
        table.setItem(i, 3, item)

        item = QTableWidgetItem()
        item.setData(0, player.tier)
        table.setItem(i, 4, item)

        item = QTableWidgetItem()
        item.setData(0, player.posTier)
        table.setItem(i, 5, item)

        item = QTableWidgetItem()
        item.setData(0, player.fullSos)
        table.setItem(i, 6, item)
        if player.fullSos < 12:
            table.item(i, 6).setBackground(QBrush(QColor("lightgreen")))
        elif player.fullSos < 22:
            table.item(i, 6).setBackground(QBrush(QColor("khaki")))
        else:
            table.item(i, 6).setBackground(QBrush(QColor("indianred")))

        item = QTableWidgetItem()
        item.setData(0, player.playoffSos)
        table.setItem(i, 7, item)

        item = QTableWidgetItem()
        item.setData(0, int(player.recTarget))
        table.setItem(i, 8, item)

        item = QTableWidgetItem()
        item.setData(0, int(player.receptions))
        table.setItem(i, 9, item)

        item = QTableWidgetItem()
        item.setData(0, float(str(player.recYard).replace(",", "")))
        table.setItem(i, 10, item)

        item = QTableWidgetItem()
        item.setData(0, int(player.recTD))
        table.setItem(i, 11, item)

        item = QTableWidgetItem()
        item.setData(0, float(str(player.rushYard).replace(",", "")))
        table.setItem(i, 12, item)

        item = QTableWidgetItem()
        item.setData(0, int(player.rushTD))
        table.setItem(i, 13, item)

        item = QTableWidgetItem()
        item.setData(0, player.composite)
        table.setItem(i, 14, item)

        i += 1

    table.setSortingEnabled(True)
    table.sortByColumn(14, Qt.AscendingOrder)
    table.resizeColumnsToContents()
    table.setSelectionBehavior(QAbstractItemView.SelectRows)
    return table

# create TE table
def create_TE_table(players):
    table = QTableWidget()
    table.setRowCount(len(players))
    table.setColumnCount(13)
    table.setHorizontalHeaderLabels(["Name", "Team", "Rank", "Pos. Rank", "Tier", "Pos. Tier", "SoS", "Playoff SoS",
                                        "Targets", "Receptions", "Rec. Yards", "Rec. TDs", "Composite"])

    i = 0
    for player in players.values():
        if player.composite == 10000 or player.tier == 0:
            continue

        table.setItem(i, 0, QTableWidgetItem(player.name))
        table.setItem(i, 1, QTableWidgetItem(player.proTeam))

        item = QTableWidgetItem()
        item.setData(0, player.avgRank)
        table.setItem(i, 2, item)

        item = QTableWidgetItem()
        item.setData(0, player.avgPosRank)
        table.setItem(i, 3, item)

        item = QTableWidgetItem()
        item.setData(0, player.tier)
        table.setItem(i, 4, item)

        item = QTableWidgetItem()
        item.setData(0, player.posTier)
        table.setItem(i, 5, item)

        item = QTableWidgetItem()
        item.setData(0, player.fullSos)
        table.setItem(i, 6, item)
        if player.fullSos < 12:
            table.item(i, 6).setBackground(QBrush(QColor("lightgreen")))
        elif player.fullSos < 22:
            table.item(i, 6).setBackground(QBrush(QColor("khaki")))
        else:
            table.item(i, 6).setBackground(QBrush(QColor("indianred")))

        item = QTableWidgetItem()
        item.setData(0, player.playoffSos)
        table.setItem(i, 7, item)

        item = QTableWidgetItem()
        item.setData(0, int(player.recTarget))
        table.setItem(i, 8, item)

        item = QTableWidgetItem()
        item.setData(0, int(player.receptions))
        table.setItem(i, 9, item)

        item = QTableWidgetItem()
        item.setData(0, float(str(player.recYard).replace(",", "")))
        table.setItem(i, 10, item)

        item = QTableWidgetItem()
        item.setData(0, int(player.recTD))
        table.setItem(i, 11, item)

        item = QTableWidgetItem()
        item.setData(0, player.composite)
        table.setItem(i, 12, item)

        i += 1

    table.setSortingEnabled(True)
    table.sortByColumn(12, Qt.AscendingOrder)
    table.resizeColumnsToContents()
    table.setSelectionBehavior(QAbstractItemView.SelectRows)
    return table

# Create Defenses Table
def create_DEF_table(players):
    table = QTableWidget()
    table.setRowCount(len(players))
    table.setColumnCount(13)
    table.setHorizontalHeaderLabels(["Name", "Rank", "Pos. Rank", "Tier", "Pos. Tier", "SoS", "Playoff SoS",
                                        "Sacks", "FR", "INT", "TDs", "Kickoff TDs", "Composite"])

    i = 0
    for player in players.values():
        if player.composite == 10000 or player.tier == 0:
            continue

        table.setItem(i, 0, QTableWidgetItem(player.name))

        item = QTableWidgetItem()
        item.setData(0, player.avgRank)
        table.setItem(i, 1, item)

        item = QTableWidgetItem()
        item.setData(0, player.avgPosRank)
        table.setItem(i, 2, item)

        item = QTableWidgetItem()
        item.setData(0, player.tier)
        table.setItem(i, 3, item)

        item = QTableWidgetItem()
        item.setData(0, player.posTier)
        table.setItem(i, 4, item)

        item = QTableWidgetItem()
        item.setData(0, player.fullSos)
        table.setItem(i, 5, item)
        if player.fullSos < 12:
            table.item(i, 5).setBackground(QBrush(QColor("lightgreen")))
        elif player.fullSos < 22:
            table.item(i, 5).setBackground(QBrush(QColor("khaki")))
        else:
            table.item(i, 5).setBackground(QBrush(QColor("indianred")))

        item = QTableWidgetItem()
        item.setData(0, player.playoffSos)
        table.setItem(i, 6, item)

        item = QTableWidgetItem()
        item.setData(0, int(player.sack))
        table.setItem(i, 7, item)

        item = QTableWidgetItem()
        item.setData(0, int(player.FR))
        table.setItem(i, 8, item)

        item = QTableWidgetItem()
        item.setData(0, int(player.intercept))
        table.setItem(i, 9, item)

        item = QTableWidgetItem()
        item.setData(0, int(player.TD))
        table.setItem(i, 10, item)

        item = QTableWidgetItem()
        item.setData(0, int(player.kickTD))
        table.setItem(i, 11, item)

        item = QTableWidgetItem()
        item.setData(0, player.composite)
        table.setItem(i, 12, item)

        i += 1

    table.setSortingEnabled(True)
    table.sortByColumn(12, Qt.AscendingOrder)
    table.resizeColumnsToContents()
    table.setSelectionBehavior(QAbstractItemView.SelectRows)
    return table

# Finally add the Ks to a table
def create_K_table(players):
    table = QTableWidget()
    table.setRowCount(len(players))
    table.setColumnCount(13)
    table.setHorizontalHeaderLabels(["Name", "Rank", "Pos. Rank", "Tier", "Pos. Tier", "SoS", "Playoff SoS",
                                        "FGM", "FGA", "FG%", "XPM", "XPA", "Composite"])

    i = 0
    for player in players.values():
        if player.composite == 10000 or player.tier == 0:
            continue

        table.setItem(i, 0, QTableWidgetItem(player.name))

        item = QTableWidgetItem()
        item.setData(0, player.avgRank)
        table.setItem(i, 1, item)

        item = QTableWidgetItem()
        item.setData(0, player.avgPosRank)
        table.setItem(i, 2, item)

        item = QTableWidgetItem()
        item.setData(0, player.tier)
        table.setItem(i, 3, item)

        item = QTableWidgetItem()
        item.setData(0, player.posTier)
        table.setItem(i, 4, item)

        item = QTableWidgetItem()
        item.setData(0, player.fullSos)
        table.setItem(i, 5, item)
        if player.fullSos < 12:
            table.item(i, 5).setBackground(QBrush(QColor("lightgreen")))
        elif player.fullSos < 22:
            table.item(i, 5).setBackground(QBrush(QColor("khaki")))
        else:
            table.item(i, 5).setBackground(QBrush(QColor("indianred")))

        item = QTableWidgetItem()
        item.setData(0, player.playoffSos)
        table.setItem(i, 6, item)

        item = QTableWidgetItem()
        item.setData(0, int(player.FGM))
        table.setItem(i, 7, item)

        item = QTableWidgetItem()
        item.setData(0, int(player.FGA))
        table.setItem(i, 8, item)

        item = QTableWidgetItem()
        item.setData(0, float(str(player.FGpercent).replace("%", "")))
        table.setItem(i, 9, item)

        item = QTableWidgetItem()
        item.setData(0, int(player.EPM))
        table.setItem(i, 10, item)

        item = QTableWidgetItem()
        item.setData(0, int(player.EPA))
        table.setItem(i, 11, item)

        item = QTableWidgetItem()
        item.setData(0, player.composite)
        table.setItem(i, 12, item)

        i += 1

    table.setSortingEnabled(True)
    table.sortByColumn(12, Qt.AscendingOrder)
    table.resizeColumnsToContents()
    table.setSelectionBehavior(QAbstractItemView.SelectRows)
    return table