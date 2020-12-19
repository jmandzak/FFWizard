from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem, QWidget
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



        self.main_layout.addWidget(self.drafting_teams)
        self.setLayout(self.main_layout)

        