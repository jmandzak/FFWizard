from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem, QWidget, QPushButton, QRadioButton, QAbstractItemView
from PyQt5.QtGui import QBrush, QColor
from PyQt5.QtCore import Qt
from data import statsio as parse


class MockWindow(QWidget):
    def __init__(self, num_teams, position) -> None:
        super(MockWindow, self).__init__()
        self.num_teams = num_teams
        self.position = position
        
        self.setWindowTitle("Mock Draft")
        self.setGeometry(0, 0, 1600, 1200)
        self.showMaximized()

        self.main_layout = QVBoxLayout()
        self.team_player_split = QHBoxLayout()
        self.position_chart_split = QVBoxLayout()
        self.position_buttons_split = QHBoxLayout()

        self.drafting_teams = QTableWidget()
        self.drafting_teams.setRowCount(1)
        self.drafting_teams.setColumnCount(self.num_teams * 16)
        self.drafting_teams.setMaximumHeight(200)

        # set up the drafting teams
        draft_order = []
        for i in range(self.num_teams):
            if i+1 == self.position:
                draft_order.append(f'Your Team')
            else:
                draft_order.append(f'team {i+1}')

        for i in range(self.num_teams):
            if self.num_teams-i == self.position:
                draft_order.append(f'Your Team')
            else:
                draft_order.append(f'team {self.num_teams-i}')

        draft_order *= 8

        for i in range(self.num_teams*16):
            self.drafting_teams.setItem(0, i, QTableWidgetItem(draft_order[i]))

            if draft_order[i] == "Your Team":
                self.drafting_teams.item(0, i).setBackground(QBrush(QColor("Yellow")))

        self.my_team = QTableWidget()
        self.my_team.setRowCount(16)
        self.my_team.setColumnCount(2)

        # set up the table
        self.my_team.setItem(0, 0, QTableWidgetItem("QB"))
        self.my_team.setItem(1, 0, QTableWidgetItem("RB"))
        self.my_team.setItem(2, 0, QTableWidgetItem("RB"))
        self.my_team.setItem(3, 0, QTableWidgetItem("WR"))
        self.my_team.setItem(4, 0, QTableWidgetItem("WR"))
        self.my_team.setItem(5, 0, QTableWidgetItem("TE"))
        self.my_team.setItem(6, 0, QTableWidgetItem("FLEX"))
        self.my_team.setItem(7, 0, QTableWidgetItem("DEF"))
        self.my_team.setItem(8, 0, QTableWidgetItem("K"))
        for i in range(8):
            self.my_team.setItem(i+9, 0, QTableWidgetItem("BE"))

        self.my_team.setColumnWidth(0, 50)
        self.my_team.setColumnWidth(1, 400)
        #self.my_team.horizontalHeader().setVisible(False)
        self.my_team.verticalHeader().setVisible(False)
        self.my_team.setHorizontalHeaderLabels(["", "Your Team"])

        # now to set up the buttons to see diff positions
        self.all_button = QPushButton("All")
        self.QB_button = QPushButton("QB")
        self.RB_button = QPushButton("RB")
        self.WR_button = QPushButton("WR")
        self.TE_button = QPushButton("TE")
        self.DEF_button = QPushButton("DEF")
        self.K_button = QPushButton("K")

        self.draft_button = QPushButton("Draft")
        self.remove_button = QPushButton("Remove")

        self.players, self.QBs, self.RBs, self.WRs, self.TEs, self.Ks, self.DEFs = self.initialize()

        self.all_table = self.create_all_table(self.players)
        self.qb_table = self.create_QB_table(self.QBs)
        self.rb_table = self.create_RB_table(self.RBs)
        self.wr_table = self.create_WR_table(self.WRs)
        self.te_table = self.create_TE_table(self.TEs)
        self.def_table = self.create_DEF_table(self.DEFs)
        self.k_table = self.create_K_table(self.Ks)


        self.position_buttons_split.addWidget(self.all_button)
        self.position_buttons_split.addWidget(self.QB_button)
        self.position_buttons_split.addWidget(self.RB_button)
        self.position_buttons_split.addWidget(self.WR_button)
        self.position_buttons_split.addWidget(self.TE_button)
        self.position_buttons_split.addWidget(self.DEF_button)
        self.position_buttons_split.addWidget(self.K_button)
        self.position_buttons_split.addSpacing(1000)
        self.position_buttons_split.addWidget(self.draft_button)
        self.position_buttons_split.addWidget(self.remove_button)

        self.position_chart_split.addLayout(self.position_buttons_split)
        self.position_chart_split.addWidget(self.k_table)

        self.team_player_split.addWidget(self.my_team)
        self.team_player_split.addLayout(self.position_chart_split)

        self.main_layout.addWidget(self.drafting_teams)
        self.main_layout.addSpacing(100)
        self.main_layout.addLayout(self.team_player_split)
        self.setLayout(self.main_layout)

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

    def create_all_table(self, players):
        all_table = QTableWidget()
        all_table.setRowCount(len(players))
        all_table.setColumnCount(7)
        all_table.setHorizontalHeaderLabels(["Name", "Pos.", "Team", "Rank", "Tier", "SoS", "Composite"])

        i = 0
        for player in players.values():
            if player.composite == 10000 or player.tier == 0:
                continue

            all_table.setItem(i, 0, QTableWidgetItem(player.name))
            all_table.setItem(i, 1, QTableWidgetItem(player.position))
            all_table.setItem(i, 2, QTableWidgetItem(player.proTeam))

            item = QTableWidgetItem()
            item.setData(0, player.avgRank)
            all_table.setItem(i, 3, item)

            item = QTableWidgetItem()
            item.setData(0, player.tier)
            all_table.setItem(i, 4, item)

            item = QTableWidgetItem()
            item.setData(0, player.fullSos)
            all_table.setItem(i, 5, item)

            item = QTableWidgetItem()
            item.setData(0, player.composite)
            all_table.setItem(i, 6, item)

            i += 1

        all_table.setSortingEnabled(True)
        all_table.sortByColumn(6, Qt.AscendingOrder)
        all_table.resizeColumnsToContents()
        all_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        return all_table
        
    # create the qb table
    def create_QB_table(self, players):
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
    def create_RB_table(self, players):
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

    def create_WR_table(self, players):
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
    def create_TE_table(self, players):
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
    def create_DEF_table(self, players):
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
    def create_K_table(self, players):
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