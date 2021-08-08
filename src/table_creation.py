from PyQt5.QtGui import QBrush, QColor
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QWidget, QPushButton, QAbstractItemView
from PyQt5.QtCore import Qt
from data import parse

def initialize(ppr=1):
    return parse.GetPlayers(ppr)

def create_all_table(players):
    table = QTableWidget()
    table.setRowCount(len(players))
    header_labels = ["Name", "Pos.", "Depth", "Team", "Boom", "Starter", "Bust", "Rank", "Tier", "Std Dev", "SoS", "Composite"]
    table.setColumnCount(len(header_labels))
    table.setHorizontalHeaderLabels(header_labels)

    i = 0
    for player in players:
        if player.composite == 10000 or player.tier == 0:
            continue

        pos = 0

        table.setItem(i, pos, QTableWidgetItem(player.name))
        pos += 1

        table.setItem(i, pos, QTableWidgetItem(player.position))
        pos += 1

        item = QTableWidgetItem()
        item.setData(0, player.depth)
        table.setItem(i, pos, item)
        if player.depth == 1:
            table.item(i, pos).setBackground(QBrush(QColor("lightgreen")))
        elif player.depth == 2:
            table.item(i, pos).setBackground(QBrush(QColor("khaki")))
        else:
            table.item(i, pos).setBackground(QBrush(QColor("indianred")))
        pos += 1

        table.setItem(i, pos, QTableWidgetItem(player.proTeam))
        pos += 1

        item = QTableWidgetItem()
        item.setData(0, player.boom)
        table.setItem(i, pos, item)
        if player.boom >= 37.5:
            table.item(i, pos).setBackground(QBrush(QColor("lightgreen")))
        elif player.boom >= 20:
            table.item(i, pos).setBackground(QBrush(QColor("khaki")))
        else:
            table.item(i, pos).setBackground(QBrush(QColor("indianred")))
        pos += 1

        item = QTableWidgetItem()
        item.setData(0, player.starter)
        table.setItem(i, pos, item)
        if player.starter >= 75:
            table.item(i, pos).setBackground(QBrush(QColor("lightgreen")))
        elif player.starter >= 50:
            table.item(i, pos).setBackground(QBrush(QColor("khaki")))
        else:
            table.item(i, pos).setBackground(QBrush(QColor("indianred")))
        pos += 1

        item = QTableWidgetItem()
        item.setData(0, player.bust)
        table.setItem(i, pos, item)
        if player.bust <= 12.5:
            table.item(i, pos).setBackground(QBrush(QColor("lightgreen")))
        elif player.bust <= 25:
            table.item(i, pos).setBackground(QBrush(QColor("khaki")))
        else:
            table.item(i, pos).setBackground(QBrush(QColor("indianred")))
        pos += 1

        item = QTableWidgetItem()
        item.setData(0, player.avgRank)
        table.setItem(i, pos, item)
        pos += 1

        item = QTableWidgetItem()
        item.setData(0, player.tier)
        table.setItem(i, pos, item)
        pos += 1

        item = QTableWidgetItem()
        item.setData(0, player.std_dev)
        table.setItem(i, pos, item)
        pos += 1

        item = QTableWidgetItem()
        item.setData(0, player.fullSos)
        table.setItem(i, pos, item)
        if player.fullSos < 12:
            table.item(i, pos).setBackground(QBrush(QColor("lightgreen")))
        elif player.fullSos < 22:
            table.item(i, pos).setBackground(QBrush(QColor("khaki")))
        else:
            table.item(i, pos).setBackground(QBrush(QColor("indianred")))
        pos += 1

        item = QTableWidgetItem()
        item.setData(0, player.compositeOverall)
        table.setItem(i, pos, item)

        i += 1

    table.setSortingEnabled(True)
    table.sortByColumn(len(header_labels)-1, Qt.AscendingOrder)
    table.resizeColumnsToContents()
    table.setSelectionBehavior(QAbstractItemView.SelectRows)
    return table
        
    # create the qb table
def create_QB_table(players):
    table = QTableWidget()
    table.setRowCount(len(players))
    header_labels = ["Name", "Depth", "Team", "Fan Pts", "Boom", "Starter", "Bust", "Pos. Rank", "Pos. Tier", "Pos Std Dev.", "SoS", "Season Sos", "Playoff SoS",
                     "Pass Yards", "Pass TDs", "Interceptions", "Rush Attempts", "Rush Yards", "Rush TDs", "Composite"]
    table.setColumnCount(len(header_labels))
    table.setHorizontalHeaderLabels(header_labels)

    i = 0
    for player in players:
        if player.composite == 10000 or player.tier == 0:
            continue

        pos = 0

        table.setItem(i, pos, QTableWidgetItem(player.name))
        pos += 1

        table.setItem(i, pos, QTableWidgetItem(player.proTeam))
        pos += 1

        item = QTableWidgetItem()
        item.setData(0, player.depth)
        table.setItem(i, pos, item)
        if player.depth == 1:
            table.item(i, pos).setBackground(QBrush(QColor("lightgreen")))
        elif player.depth == 2:
            table.item(i, pos).setBackground(QBrush(QColor("khaki")))
        else:
            table.item(i, pos).setBackground(QBrush(QColor("indianred")))
        pos += 1

        item = QTableWidgetItem()
        item.setData(0, player.pastPPG)
        table.setItem(i, pos, item)
        pos += 1

        item = QTableWidgetItem()
        item.setData(0, player.boom)
        table.setItem(i, pos, item)
        if player.boom >= 37.5:
            table.item(i, pos).setBackground(QBrush(QColor("lightgreen")))
        elif player.boom >= 20:
            table.item(i, pos).setBackground(QBrush(QColor("khaki")))
        else:
            table.item(i, pos).setBackground(QBrush(QColor("indianred")))
        pos += 1

        item = QTableWidgetItem()
        item.setData(0, player.starter)
        table.setItem(i, pos, item)
        if player.starter >= 75:
            table.item(i, pos).setBackground(QBrush(QColor("lightgreen")))
        elif player.starter >= 50:
            table.item(i, pos).setBackground(QBrush(QColor("khaki")))
        else:
            table.item(i, pos).setBackground(QBrush(QColor("indianred")))
        pos += 1

        item = QTableWidgetItem()
        item.setData(0, player.bust)
        table.setItem(i, pos, item)
        if player.bust <= 12.5:
            table.item(i, pos).setBackground(QBrush(QColor("lightgreen")))
        elif player.bust <= 25:
            table.item(i, pos).setBackground(QBrush(QColor("khaki")))
        else:
            table.item(i, pos).setBackground(QBrush(QColor("indianred")))
        pos += 1

        item = QTableWidgetItem()
        item.setData(0, player.avgPosRank)
        table.setItem(i, pos, item)
        pos += 1

        item = QTableWidgetItem()
        item.setData(0, player.posTier)
        table.setItem(i, pos, item)
        pos += 1

        item = QTableWidgetItem()
        item.setData(0, float(player.pos_std_dev))
        table.setItem(i, pos, item)
        pos += 1

        item = QTableWidgetItem()
        item.setData(0, player.fullSos)
        table.setItem(i, pos, item)
        if player.fullSos < 12:
            table.item(i, pos).setBackground(QBrush(QColor("lightgreen")))
        elif player.fullSos < 22:
            table.item(i, pos).setBackground(QBrush(QColor("khaki")))
        else:
            table.item(i, pos).setBackground(QBrush(QColor("indianred")))
        pos += 1

        item = QTableWidgetItem()
        item.setData(0, player.seasonSos)
        table.setItem(i, pos, item)
        if player.seasonSos < 12:
            table.item(i, pos).setBackground(QBrush(QColor("lightgreen")))
        elif player.seasonSos < 22:
            table.item(i, pos).setBackground(QBrush(QColor("khaki")))
        else:
            table.item(i, pos).setBackground(QBrush(QColor("indianred")))
        pos += 1

        item = QTableWidgetItem()
        item.setData(0, player.playoffSos)
        table.setItem(i, pos, item)
        if player.playoffSos < 12:
            table.item(i, pos).setBackground(QBrush(QColor("lightgreen")))
        elif player.playoffSos < 22:
            table.item(i, pos).setBackground(QBrush(QColor("khaki")))
        else:
            table.item(i, pos).setBackground(QBrush(QColor("indianred")))
        pos += 1

        item = QTableWidgetItem()
        item.setData(0, float(player.passYard))
        table.setItem(i, pos, item)
        pos += 1

        item = QTableWidgetItem()
        item.setData(0, float(player.passTD))
        table.setItem(i, pos, item)
        pos += 1

        item = QTableWidgetItem()
        item.setData(0, float(player.passInt))
        table.setItem(i, pos, item)
        pos += 1
        
        item = QTableWidgetItem()
        item.setData(0, float(player.rushAtt))
        table.setItem(i, pos, item)
        pos += 1

        item = QTableWidgetItem()
        item.setData(0, float(player.rushYard))
        table.setItem(i, pos, item)
        pos += 1

        item = QTableWidgetItem()
        item.setData(0, float(player.rushTD))
        table.setItem(i, pos, item)
        pos += 1

        item = QTableWidgetItem()
        item.setData(0, player.composite)
        table.setItem(i, pos, item)

        i += 1

    table.setSortingEnabled(True)
    table.sortByColumn(len(header_labels)-1, Qt.AscendingOrder)
    table.resizeColumnsToContents()
    table.setSelectionBehavior(QAbstractItemView.SelectRows)
    return table

# create the running back table
def create_RB_table(players):
    table = QTableWidget()
    table.setRowCount(len(players))
    header_labels = ["Name", "Depth", "Team", "Fan Pts", "Boom", "Starter", "Bust", "Pos. Rank", "Pos. Tier", "Pos Std Dev.", "SoS", "Season Sos", "Playoff SoS",
                     "Rush Att", "Rush Yards", "Rush TDs", "Targets", "Receptions", "Rec. Yards", "Rec. TDs", "Composite"]
    table.setColumnCount(len(header_labels))
    table.setHorizontalHeaderLabels(header_labels)

    i = 0
    for player in players:
        if player.composite == 10000 or player.tier == 0:
            continue

        pos = 0

        table.setItem(i, pos, QTableWidgetItem(player.name))
        pos += 1

        table.setItem(i, pos, QTableWidgetItem(player.proTeam))
        pos += 1

        item = QTableWidgetItem()
        item.setData(0, player.depth)
        table.setItem(i, pos, item)
        if player.depth == 1:
            table.item(i, pos).setBackground(QBrush(QColor("lightgreen")))
        elif player.depth == 2:
            table.item(i, pos).setBackground(QBrush(QColor("khaki")))
        else:
            table.item(i, pos).setBackground(QBrush(QColor("indianred")))
        pos += 1

        item = QTableWidgetItem()
        item.setData(0, player.pastPPG)
        table.setItem(i, pos, item)
        pos += 1

        item = QTableWidgetItem()
        item.setData(0, player.boom)
        table.setItem(i, pos, item)
        if player.boom >= 37.5:
            table.item(i, pos).setBackground(QBrush(QColor("lightgreen")))
        elif player.boom >= 20:
            table.item(i, pos).setBackground(QBrush(QColor("khaki")))
        else:
            table.item(i, pos).setBackground(QBrush(QColor("indianred")))
        pos += 1

        item = QTableWidgetItem()
        item.setData(0, player.starter)
        table.setItem(i, pos, item)
        if player.starter >= 75:
            table.item(i, pos).setBackground(QBrush(QColor("lightgreen")))
        elif player.starter >= 50:
            table.item(i, pos).setBackground(QBrush(QColor("khaki")))
        else:
            table.item(i, pos).setBackground(QBrush(QColor("indianred")))
        pos += 1

        item = QTableWidgetItem()
        item.setData(0, player.bust)
        table.setItem(i, pos, item)
        if player.bust <= 12.5:
            table.item(i, pos).setBackground(QBrush(QColor("lightgreen")))
        elif player.bust <= 25:
            table.item(i, pos).setBackground(QBrush(QColor("khaki")))
        else:
            table.item(i, pos).setBackground(QBrush(QColor("indianred")))
        pos += 1

        item = QTableWidgetItem()
        item.setData(0, player.avgPosRank)
        table.setItem(i, pos, item)
        pos += 1

        item = QTableWidgetItem()
        item.setData(0, player.posTier)
        table.setItem(i, pos, item)
        pos += 1
        
        item = QTableWidgetItem()
        item.setData(0, float(player.pos_std_dev))
        table.setItem(i, pos, item)
        pos += 1

        item = QTableWidgetItem()
        item.setData(0, player.fullSos)
        table.setItem(i, pos, item)
        if player.fullSos < 12:
            table.item(i, pos).setBackground(QBrush(QColor("lightgreen")))
        elif player.fullSos < 22:
            table.item(i, pos).setBackground(QBrush(QColor("khaki")))
        else:
            table.item(i, pos).setBackground(QBrush(QColor("indianred")))
        pos += 1

        item = QTableWidgetItem()
        item.setData(0, player.seasonSos)
        table.setItem(i, pos, item)
        if player.seasonSos < 12:
            table.item(i, pos).setBackground(QBrush(QColor("lightgreen")))
        elif player.seasonSos < 22:
            table.item(i, pos).setBackground(QBrush(QColor("khaki")))
        else:
            table.item(i, pos).setBackground(QBrush(QColor("indianred")))
        pos += 1

        item = QTableWidgetItem()
        item.setData(0, player.playoffSos)
        table.setItem(i, pos, item)
        if player.playoffSos < 12:
            table.item(i, pos).setBackground(QBrush(QColor("lightgreen")))
        elif player.playoffSos < 22:
            table.item(i, pos).setBackground(QBrush(QColor("khaki")))
        else:
            table.item(i, pos).setBackground(QBrush(QColor("indianred")))
        pos += 1

        item = QTableWidgetItem()
        item.setData(0, float(player.rushAtt))
        table.setItem(i, pos, item)
        pos += 1
        
        item = QTableWidgetItem()
        item.setData(0, float(player.rushYard))
        table.setItem(i, pos, item)
        pos += 1
        
        item = QTableWidgetItem()
        item.setData(0, float(player.rushTD))
        table.setItem(i, pos, item)
        pos += 1
        
        item = QTableWidgetItem()
        item.setData(0, float(player.recTarget))
        table.setItem(i, pos, item)
        pos += 1
        
        item = QTableWidgetItem()
        item.setData(0, float(player.receptions))
        table.setItem(i, pos, item)
        pos += 1

        item = QTableWidgetItem()
        item.setData(0, float(player.recYard))
        table.setItem(i, pos, item)
        pos += 1

        item = QTableWidgetItem()
        item.setData(0, float(player.recTD))
        table.setItem(i, pos, item)
        pos += 1

        item = QTableWidgetItem()
        item.setData(0, player.composite)
        table.setItem(i, pos, item)
        i += 1

    table.setSortingEnabled(True)
    table.sortByColumn(len(header_labels)-1, Qt.AscendingOrder)
    table.resizeColumnsToContents()
    table.setSelectionBehavior(QAbstractItemView.SelectRows)
    return table

def create_WR_table(players):
    table = QTableWidget()
    table.setRowCount(len(players))
    header_labels = ["Name", "Depth", "Team", "Fan Pts", "Boom", "Starter", "Bust", "Pos. Rank", "Pos. Tier", "Pos Std Dev.", "SoS", "Season Sos", "Playoff SoS",
                     "Targets", "Receptions", "Rec. Yards", "Rec. TDs", "Composite"]
    table.setColumnCount(len(header_labels))
    table.setHorizontalHeaderLabels(header_labels)

    i = 0
    for player in players:
        if player.composite == 10000 or player.tier == 0:
            continue
        
        pos = 0

        table.setItem(i, pos, QTableWidgetItem(player.name))
        pos += 1

        table.setItem(i, pos, QTableWidgetItem(player.proTeam))
        pos += 1

        item = QTableWidgetItem()
        item.setData(0, player.depth)
        table.setItem(i, pos, item)
        if player.depth == 1:
            table.item(i, pos).setBackground(QBrush(QColor("lightgreen")))
        elif player.depth == 2:
            table.item(i, pos).setBackground(QBrush(QColor("khaki")))
        else:
            table.item(i, pos).setBackground(QBrush(QColor("indianred")))
        pos += 1

        item = QTableWidgetItem()
        item.setData(0, player.pastPPG)
        table.setItem(i, pos, item)
        pos += 1

        item = QTableWidgetItem()
        item.setData(0, player.boom)
        table.setItem(i, pos, item)
        if player.boom >= 37.5:
            table.item(i, pos).setBackground(QBrush(QColor("lightgreen")))
        elif player.boom >= 20:
            table.item(i, pos).setBackground(QBrush(QColor("khaki")))
        else:
            table.item(i, pos).setBackground(QBrush(QColor("indianred")))
        pos += 1

        item = QTableWidgetItem()
        item.setData(0, player.starter)
        table.setItem(i, pos, item)
        if player.starter >= 75:
            table.item(i, pos).setBackground(QBrush(QColor("lightgreen")))
        elif player.starter >= 50:
            table.item(i, pos).setBackground(QBrush(QColor("khaki")))
        else:
            table.item(i, pos).setBackground(QBrush(QColor("indianred")))
        pos += 1

        item = QTableWidgetItem()
        item.setData(0, player.bust)
        table.setItem(i, pos, item)
        if player.bust <= 12.5:
            table.item(i, pos).setBackground(QBrush(QColor("lightgreen")))
        elif player.bust <= 25:
            table.item(i, pos).setBackground(QBrush(QColor("khaki")))
        else:
            table.item(i, pos).setBackground(QBrush(QColor("indianred")))
        pos += 1

        item = QTableWidgetItem()
        item.setData(0, player.avgPosRank)
        table.setItem(i, pos, item)
        pos += 1

        item = QTableWidgetItem()
        item.setData(0, player.posTier)
        table.setItem(i, pos, item)
        pos += 1
        
        item = QTableWidgetItem()
        item.setData(0, float(player.pos_std_dev))
        table.setItem(i, pos, item)
        pos += 1

        item = QTableWidgetItem()
        item.setData(0, player.fullSos)
        table.setItem(i, pos, item)
        if player.fullSos < 12:
            table.item(i, pos).setBackground(QBrush(QColor("lightgreen")))
        elif player.fullSos < 22:
            table.item(i, pos).setBackground(QBrush(QColor("khaki")))
        else:
            table.item(i, pos).setBackground(QBrush(QColor("indianred")))
        pos += 1

        item = QTableWidgetItem()
        item.setData(0, player.seasonSos)
        table.setItem(i, pos, item)
        if player.seasonSos < 12:
            table.item(i, pos).setBackground(QBrush(QColor("lightgreen")))
        elif player.seasonSos < 22:
            table.item(i, pos).setBackground(QBrush(QColor("khaki")))
        else:
            table.item(i, pos).setBackground(QBrush(QColor("indianred")))
        pos += 1

        item = QTableWidgetItem()
        item.setData(0, player.playoffSos)
        table.setItem(i, pos, item)
        if player.playoffSos < 12:
            table.item(i, pos).setBackground(QBrush(QColor("lightgreen")))
        elif player.playoffSos < 22:
            table.item(i, pos).setBackground(QBrush(QColor("khaki")))
        else:
            table.item(i, pos).setBackground(QBrush(QColor("indianred")))
        pos += 1

        item = QTableWidgetItem()
        item.setData(0, float(player.recTarget))
        table.setItem(i, pos, item)
        pos += 1

        item = QTableWidgetItem()
        item.setData(0, float(player.receptions))
        table.setItem(i, pos, item)
        pos += 1

        item = QTableWidgetItem()
        item.setData(0, float(player.recYard))
        table.setItem(i, pos, item)
        pos += 1

        item = QTableWidgetItem()
        item.setData(0, float(player.recTD))
        table.setItem(i, pos, item)
        pos += 1

        item = QTableWidgetItem()
        item.setData(0, player.composite)
        table.setItem(i, pos, item)

        i += 1

    table.setSortingEnabled(True)
    table.sortByColumn(len(header_labels)-1, Qt.AscendingOrder)
    table.resizeColumnsToContents()
    table.setSelectionBehavior(QAbstractItemView.SelectRows)
    return table

# create TE table
def create_TE_table(players):
    return create_WR_table(players)

# Create Defenses Table
def create_DEF_table(players):
    table = QTableWidget()
    table.setRowCount(len(players))
    header_labels = ["Name", "Fan Pts", "Pos. Rank", "Pos. Tier", "Pos. Std Dev", "SoS", "Season Sos", "Playoff SoS",
                     "Sacks", "FR", "INT", "TDs", "Kickoff TDs", "Composite"]
    table.setColumnCount(len(header_labels))
    table.setHorizontalHeaderLabels(header_labels)

    i = 0
    for player in players:
        if player.composite == 10000 or player.tier == 0:
            continue

        pos = 0

        table.setItem(i, pos, QTableWidgetItem(player.name))
        pos += 1

        item = QTableWidgetItem()
        item.setData(0, player.pastPPG)
        table.setItem(i, pos, item)
        pos += 1

        item = QTableWidgetItem()
        item.setData(0, player.avgPosRank)
        table.setItem(i, pos, item)
        pos += 1

        item = QTableWidgetItem()
        item.setData(0, player.posTier)
        table.setItem(i, pos, item)
        pos += 1
        
        item = QTableWidgetItem()
        item.setData(0, float(player.pos_std_dev))
        table.setItem(i, pos, item)
        pos += 1

        item = QTableWidgetItem()
        item.setData(0, player.fullSos)
        table.setItem(i, pos, item)
        if player.fullSos < 12:
            table.item(i, pos).setBackground(QBrush(QColor("lightgreen")))
        elif player.fullSos < 22:
            table.item(i, pos).setBackground(QBrush(QColor("khaki")))
        else:
            table.item(i, pos).setBackground(QBrush(QColor("indianred")))
        pos += 1

        item = QTableWidgetItem()
        item.setData(0, player.seasonSos)
        table.setItem(i, pos, item)
        if player.seasonSos < 12:
            table.item(i, pos).setBackground(QBrush(QColor("lightgreen")))
        elif player.seasonSos < 22:
            table.item(i, pos).setBackground(QBrush(QColor("khaki")))
        else:
            table.item(i, pos).setBackground(QBrush(QColor("indianred")))
        pos += 1

        item = QTableWidgetItem()
        item.setData(0, player.playoffSos)
        table.setItem(i, pos, item)
        if player.playoffSos < 12:
            table.item(i, pos).setBackground(QBrush(QColor("lightgreen")))
        elif player.playoffSos < 22:
            table.item(i, pos).setBackground(QBrush(QColor("khaki")))
        else:
            table.item(i, pos).setBackground(QBrush(QColor("indianred")))
        pos += 1

        item = QTableWidgetItem()
        item.setData(0, float(player.sack))
        table.setItem(i, pos, item)
        pos += 1

        item = QTableWidgetItem()
        item.setData(0, float(player.FR))
        table.setItem(i, pos, item)
        pos += 1

        item = QTableWidgetItem()
        item.setData(0, float(player.intercept))
        table.setItem(i, pos, item)
        pos += 1

        item = QTableWidgetItem()
        item.setData(0, float(player.TD))
        table.setItem(i, pos, item)
        pos += 1

        item = QTableWidgetItem()
        item.setData(0, float(player.kickTD))
        table.setItem(i, pos, item)
        pos += 1

        item = QTableWidgetItem()
        item.setData(0, player.composite)
        table.setItem(i, pos, item)

        i += 1

    table.setSortingEnabled(True)
    table.sortByColumn(len(header_labels)-1, Qt.AscendingOrder)
    table.resizeColumnsToContents()
    table.setSelectionBehavior(QAbstractItemView.SelectRows)
    return table

# Finally add the Ks to a table
def create_K_table(players):
    table = QTableWidget()
    table.setRowCount(len(players))
    header_labels = ["Name", "Team", "Fan Pts", "Boom", "Starter", "Bust", "Pos. Rank", "Pos. Tier", "Pos Std Dev.", "SoS", "Season Sos", "Playoff SoS",
                     "XPM", "XPA", "Composite"]
    table.setColumnCount(len(header_labels))
    table.setHorizontalHeaderLabels(header_labels)

    i = 0
    for player in players:
        if player.composite == 10000 or player.tier == 0:
            continue

        pos = 0

        table.setItem(i, pos, QTableWidgetItem(player.name))
        pos += 1

        table.setItem(i, pos, QTableWidgetItem(player.proTeam))
        pos += 1

        item = QTableWidgetItem()
        item.setData(0, player.pastPPG)
        table.setItem(i, pos, item)
        pos += 1

        item = QTableWidgetItem()
        item.setData(0, player.boom)
        table.setItem(i, pos, item)
        if player.boom >= 37.5:
            table.item(i, pos).setBackground(QBrush(QColor("lightgreen")))
        elif player.boom >= 20:
            table.item(i, pos).setBackground(QBrush(QColor("khaki")))
        else:
            table.item(i, pos).setBackground(QBrush(QColor("indianred")))
        pos += 1

        item = QTableWidgetItem()
        item.setData(0, player.starter)
        table.setItem(i, pos, item)
        if player.starter >= 75:
            table.item(i, pos).setBackground(QBrush(QColor("lightgreen")))
        elif player.starter >= 50:
            table.item(i, pos).setBackground(QBrush(QColor("khaki")))
        else:
            table.item(i, pos).setBackground(QBrush(QColor("indianred")))
        pos += 1

        item = QTableWidgetItem()
        item.setData(0, player.bust)
        table.setItem(i, pos, item)
        if player.bust <= 12.5:
            table.item(i, pos).setBackground(QBrush(QColor("lightgreen")))
        elif player.bust <= 25:
            table.item(i, pos).setBackground(QBrush(QColor("khaki")))
        else:
            table.item(i, pos).setBackground(QBrush(QColor("indianred")))
        pos += 1

        item = QTableWidgetItem()
        item.setData(0, player.avgPosRank)
        table.setItem(i, pos, item)
        pos += 1

        item = QTableWidgetItem()
        item.setData(0, player.posTier)
        table.setItem(i, pos, item)
        pos += 1
        
        item = QTableWidgetItem()
        item.setData(0, float(player.pos_std_dev))
        table.setItem(i, pos, item)
        pos += 1

        item = QTableWidgetItem()
        item.setData(0, player.fullSos)
        table.setItem(i, pos, item)
        if player.fullSos < 12:
            table.item(i, pos).setBackground(QBrush(QColor("lightgreen")))
        elif player.fullSos < 22:
            table.item(i, pos).setBackground(QBrush(QColor("khaki")))
        else:
            table.item(i, pos).setBackground(QBrush(QColor("indianred")))
        pos += 1

        item = QTableWidgetItem()
        item.setData(0, player.seasonSos)
        table.setItem(i, pos, item)
        if player.seasonSos < 12:
            table.item(i, pos).setBackground(QBrush(QColor("lightgreen")))
        elif player.seasonSos < 22:
            table.item(i, pos).setBackground(QBrush(QColor("khaki")))
        else:
            table.item(i, pos).setBackground(QBrush(QColor("indianred")))
        pos += 1

        item = QTableWidgetItem()
        item.setData(0, player.playoffSos)
        table.setItem(i, pos, item)
        if player.playoffSos < 12:
            table.item(i, pos).setBackground(QBrush(QColor("lightgreen")))
        elif player.playoffSos < 22:
            table.item(i, pos).setBackground(QBrush(QColor("khaki")))
        else:
            table.item(i, pos).setBackground(QBrush(QColor("indianred")))
        pos += 1

        item = QTableWidgetItem()
        item.setData(0, float(player.EPM))
        table.setItem(i, pos, item)
        pos += 1

        item = QTableWidgetItem()
        item.setData(0, float(player.EPA))
        table.setItem(i, pos, item)
        pos += 1

        item = QTableWidgetItem()
        item.setData(0, player.composite)
        table.setItem(i, pos, item)

        i += 1

    table.setSortingEnabled(True)
    table.sortByColumn(len(header_labels)-1, Qt.AscendingOrder)
    table.resizeColumnsToContents()
    table.setSelectionBehavior(QAbstractItemView.SelectRows)
    return table