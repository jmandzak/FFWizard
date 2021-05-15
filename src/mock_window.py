from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem, QWidget, QPushButton
from PyQt5.QtGui import QBrush, QColor
from PyQt5.QtCore import Qt, QTimer
from table_creation import create_all_table, create_QB_table, create_RB_table, create_WR_table, create_TE_table, create_DEF_table, create_K_table, initialize
from buttons import *

class MockWindow(QWidget):
    def __init__(self, num_teams, position) -> None:
        super(MockWindow, self).__init__()
        self.num_teams = num_teams
        self.position = position

        # set up the window
        self.setWindowTitle("Mock Draft")
        self.setGeometry(0, 0, 1600, 1200)
        self.showMaximized()

        # set up timers
        self.cpu_draft_timer = QTimer()
        self.highlight_player_timer = QTimer()

        # set variable to see if player is highlighted
        self.row_to_remove = -1

        # set up button layouts
        self.main_layout = QVBoxLayout()
        self.team_player_split = QHBoxLayout()
        self.position_chart_split = QVBoxLayout()
        self.position_buttons_split = QHBoxLayout()
        self.team_watch_split = QVBoxLayout()

        # set up draft order
        self.drafting_teams = QTableWidget()
        self.drafting_teams.setRowCount(1)
        self.drafting_teams.setColumnCount(self.num_teams * 16)
        self.drafting_teams.setMaximumHeight(140)
        self.drafting_teams.verticalHeader().setVisible(False)
        self.drafting_teams.horizontalHeader().setVisible(False)

        # set up the drafting teams
        draft_order = []
        for i in range(self.num_teams):
            if i+1 == self.position:
                draft_order.append(f'Your Team')
            else:
                draft_order.append(f'Team {i+1}')

        for i in range(self.num_teams):
            if self.num_teams-i == self.position:
                draft_order.append(f'Your Team')
            else:
                draft_order.append(f'Team {self.num_teams-i}')

        draft_order *= 8

        for i in range(self.num_teams*16):
            self.drafting_teams.setItem(0, i, QTableWidgetItem(draft_order[i]))

            if draft_order[i] == "Your Team":
                self.drafting_teams.item(0, i).setBackground(QBrush(QColor("Yellow")))

        self.my_team = QTableWidget()
        self.my_team.setRowCount(16)
        self.my_team.setColumnCount(2)

        # set up the table for user team
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
        self.my_team.verticalHeader().setVisible(False)
        self.my_team.setHorizontalHeaderLabels(["", "Your Team"])

        # set up watch list
        self.watch_list = QTableWidget()
        self.watch_list.setColumnCount(2)
        self.watch_list.setColumnWidth(0, 50)
        self.watch_list.setColumnWidth(1, 400)
        self.watch_list.setHorizontalHeaderLabels(["", "Watch List"])

        # now to set up the buttons to see diff positions
        self.all_button = QPushButton("All")
        self.all_button.clicked.connect(lambda: display_all(self))

        self.QB_button = QPushButton("QB")
        self.QB_button.clicked.connect(lambda: display_qb(self))

        self.RB_button = QPushButton("RB")
        self.RB_button.clicked.connect(lambda: display_rb(self))

        self.WR_button = QPushButton("WR")
        self.WR_button.clicked.connect(lambda: display_wr(self))
        
        self.TE_button = QPushButton("TE")
        self.TE_button.clicked.connect(lambda: display_te(self))
        
        self.DEF_button = QPushButton("DEF")
        self.DEF_button.clicked.connect(lambda: display_def(self))
        
        self.K_button = QPushButton("K")
        self.K_button.clicked.connect(lambda: display_k(self))
        
        # button to add players to watchlist
        self.add_watchlist_button = QPushButton("Add to Watchlist")
        self.add_watchlist_button.clicked.connect(lambda: add_player_to_watchlist(self))

        # button to draft player to your team
        self.draft_button = QPushButton("Draft")
        self.draft_button.clicked.connect(lambda: draft_player(self))

        # set up timer to call func to remove players, set to run every 2 seconds
        self.cpu_draft_timer.timeout.connect(lambda: cpu_draft(self))
        self.cpu_draft_timer.start(2000)

        # set up timer to call func to highlight player to be removed
        self.highlight_player_timer.timeout.connect(lambda: highlight_pick(self))
        self.highlight_player_timer.start(1)

        self.players, self.QBs, self.RBs, self.WRs, self.TEs, self.Ks, self.DEFs = initialize()

        self.all_table = create_all_table(self.players)
        self.qb_table = create_QB_table(self.QBs)
        self.rb_table = create_RB_table(self.RBs)
        self.wr_table = create_WR_table(self.WRs)
        self.te_table = create_TE_table(self.TEs)
        self.def_table = create_DEF_table(self.DEFs)
        self.k_table = create_K_table(self.Ks)


        self.position_buttons_split.addWidget(self.all_button)
        self.position_buttons_split.addWidget(self.QB_button)
        self.position_buttons_split.addWidget(self.RB_button)
        self.position_buttons_split.addWidget(self.WR_button)
        self.position_buttons_split.addWidget(self.TE_button)
        self.position_buttons_split.addWidget(self.DEF_button)
        self.position_buttons_split.addWidget(self.K_button)
        self.position_buttons_split.addSpacing(300)
        self.position_buttons_split.addWidget(self.add_watchlist_button)
        self.position_buttons_split.addSpacing(300)
        self.position_buttons_split.addWidget(self.draft_button)

        self.position_chart_split.addLayout(self.position_buttons_split)
        self.position_chart_split.addWidget(self.all_table)
        self.position_chart_split.addWidget(self.qb_table)
        self.position_chart_split.addWidget(self.rb_table)
        self.position_chart_split.addWidget(self.wr_table)
        self.position_chart_split.addWidget(self.te_table)
        self.position_chart_split.addWidget(self.def_table)
        self.position_chart_split.addWidget(self.k_table)

        self.qb_table.hide()
        self.rb_table.hide()
        self.wr_table.hide()
        self.te_table.hide()
        self.def_table.hide()
        self.k_table.hide()

        self.team_watch_split.addWidget(self.my_team)
        self.team_watch_split.addWidget(self.watch_list)
        self.team_player_split.addLayout(self.team_watch_split)
        self.team_player_split.addLayout(self.position_chart_split)

        self.main_layout.addWidget(self.drafting_teams)
        self.main_layout.addSpacing(100)
        self.main_layout.addLayout(self.team_player_split)
        self.setLayout(self.main_layout)