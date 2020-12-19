from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem, QWidget, QPushButton
from PyQt5.QtGui import QBrush, QColor


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

        self.team_player_split.addWidget(self.my_team)
        self.team_player_split.addLayout(self.position_buttons_split)

        self.main_layout.addWidget(self.drafting_teams)
        self.main_layout.addSpacing(100)
        self.main_layout.addLayout(self.team_player_split)
        self.setLayout(self.main_layout)

        