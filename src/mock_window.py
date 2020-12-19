from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem, QWidget, QPushButton, QRadioButton, QAbstractItemView
from PyQt5.QtGui import QBrush, QColor
from PyQt5.QtCore import Qt
from table_creation import create_all_table, create_QB_table, create_RB_table, create_WR_table, create_TE_table, create_DEF_table, create_K_table, initialize
from buttons import display_all, display_qb, display_rb, display_wr, display_te, display_def, display_k

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
        self.my_team.verticalHeader().setVisible(False)
        self.my_team.setHorizontalHeaderLabels(["", "Your Team"])

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
        

        self.draft_button = QPushButton("Draft")
        self.remove_button = QPushButton("Remove")

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
        self.position_buttons_split.addSpacing(1000)
        self.position_buttons_split.addWidget(self.draft_button)
        self.position_buttons_split.addWidget(self.remove_button)

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

        self.team_player_split.addWidget(self.my_team)
        self.team_player_split.addLayout(self.position_chart_split)

        self.main_layout.addWidget(self.drafting_teams)
        self.main_layout.addSpacing(100)
        self.main_layout.addLayout(self.team_player_split)
        self.setLayout(self.main_layout)