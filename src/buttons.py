from random import choice

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush, QColor
from PyQt5.QtWidgets import QPushButton, QStyle, QTableWidgetItem


def display_all(window):
    window.all_table.show()
    window.qb_table.hide()
    window.rb_table.hide()
    window.wr_table.hide()
    window.te_table.hide()
    window.def_table.hide()
    window.k_table.hide()


def display_qb(window):
    window.all_table.hide()
    window.qb_table.show()
    window.rb_table.hide()
    window.wr_table.hide()
    window.te_table.hide()
    window.def_table.hide()
    window.k_table.hide()


def display_rb(window):
    window.all_table.hide()
    window.qb_table.hide()
    window.rb_table.show()
    window.wr_table.hide()
    window.te_table.hide()
    window.def_table.hide()
    window.k_table.hide()


def display_wr(window):
    window.all_table.hide()
    window.qb_table.hide()
    window.rb_table.hide()
    window.wr_table.show()
    window.te_table.hide()
    window.def_table.hide()
    window.k_table.hide()


def display_te(window):
    window.all_table.hide()
    window.qb_table.hide()
    window.rb_table.hide()
    window.wr_table.hide()
    window.te_table.show()
    window.def_table.hide()
    window.k_table.hide()


def display_def(window):
    window.all_table.hide()
    window.qb_table.hide()
    window.rb_table.hide()
    window.wr_table.hide()
    window.te_table.hide()
    window.def_table.show()
    window.k_table.hide()


def display_k(window):
    window.all_table.hide()
    window.qb_table.hide()
    window.rb_table.hide()
    window.wr_table.hide()
    window.te_table.hide()
    window.def_table.hide()
    window.k_table.show()


def draft_player(window):
    content = ""
    position = ""
    name = ""
    all_table = 0  # used to keep up with if the player was drafted from "all" table or position table

    # remove the row from the table
    if window.all_table.isVisible():
        content = window.all_table.selectedItems()
        position = content[1].text()
        name = content[0].text()

        current_row = window.all_table.currentRow()
        window.all_table.removeRow(current_row)
        all_table = 1

    elif window.qb_table.isVisible():
        content = window.qb_table.selectedItems()
        name = content[0].text()
        current_row = window.qb_table.currentRow()
        window.qb_table.removeRow(current_row)
        position = "QB"

    elif window.rb_table.isVisible():
        content = window.rb_table.selectedItems()
        name = content[0].text()
        current_row = window.rb_table.currentRow()
        window.rb_table.removeRow(current_row)
        position = "RB"

    elif window.wr_table.isVisible():
        content = window.wr_table.selectedItems()
        name = content[0].text()
        current_row = window.wr_table.currentRow()
        window.wr_table.removeRow(current_row)
        position = "WR"

    elif window.te_table.isVisible():
        content = window.te_table.selectedItems()
        name = content[0].text()
        current_row = window.te_table.currentRow()
        window.te_table.removeRow(current_row)
        position = "TE"

    elif window.def_table.isVisible():
        content = window.def_table.selectedItems()
        name = content[0].text()
        current_row = window.def_table.currentRow()
        window.def_table.removeRow(current_row)
        position = "DEF"

    elif window.k_table.isVisible():
        content = window.k_table.selectedItems()
        name = content[0].text()
        current_row = window.k_table.currentRow()
        window.k_table.removeRow(current_row)
        position = "K"

    # remove player from the other table they're in
    if all_table:

        # remove from position table
        if position == "QB":
            item = window.qb_table.findItems(name, Qt.MatchFixedString)
            row = window.qb_table.row(item[0])
            window.qb_table.removeRow(row)

        elif position == "RB":
            item = window.rb_table.findItems(name, Qt.MatchFixedString)
            row = window.rb_table.row(item[0])
            window.rb_table.removeRow(row)

        elif position == "WR":
            item = window.wr_table.findItems(name, Qt.MatchFixedString)
            row = window.wr_table.row(item[0])
            window.wr_table.removeRow(row)
        elif position == "TE":
            item = window.te_table.findItems(name, Qt.MatchFixedString)
            row = window.te_table.row(item[0])
            window.te_table.removeRow(row)

        elif position == "DEF":
            item = window.def_table.findItems(name, Qt.MatchFixedString)
            row = window.def_table.row(item[0])
            window.def_table.removeRow(row)

        elif position == "K":
            item = window.k_table.findItems(name, Qt.MatchFixedString)
            row = window.k_table.row(item[0])
            window.k_table.removeRow(row)

    # remove from "all" table
    else:
        item = window.all_table.findItems(name, Qt.MatchFixedString)
        row = window.all_table.row(item[0])
        window.all_table.removeRow(row)

    # remove from watchlist if player is there
    item = window.watch_list.findItems(name, Qt.MatchFixedString)
    if len(item) > 0:
        row = window.watch_list.row(item[0])
        window.watch_list.removeRow(row)

    # now assign the player to the user's team
    if position == "QB":
        if window.my_team.item(0, 1) is None:
            window.my_team.setItem(0, 1, QTableWidgetItem(name))
        else:
            for i in range(8):
                if window.my_team.item(i + 9, 1) is None:
                    window.my_team.setItem(i + 9, 1, QTableWidgetItem(name))
                    break

    elif position == "RB":
        if window.my_team.item(1, 1) is None:
            window.my_team.setItem(1, 1, QTableWidgetItem(name))
        elif window.my_team.item(2, 1) is None:
            window.my_team.setItem(2, 1, QTableWidgetItem(name))
        elif window.my_team.item(6, 1) is None:
            window.my_team.setItem(6, 1, QTableWidgetItem(name))
        else:
            for i in range(8):
                if window.my_team.item(i + 9, 1) is None:
                    window.my_team.setItem(i + 9, 1, QTableWidgetItem(name))
                    break

    elif position == "WR":
        if window.my_team.item(3, 1) is None:
            window.my_team.setItem(3, 1, QTableWidgetItem(name))
        elif window.my_team.item(4, 1) is None:
            window.my_team.setItem(4, 1, QTableWidgetItem(name))
        elif window.my_team.item(6, 1) is None:
            window.my_team.setItem(6, 1, QTableWidgetItem(name))
        else:
            for i in range(8):
                if window.my_team.item(i + 9, 1) is None:
                    window.my_team.setItem(i + 9, 1, QTableWidgetItem(name))
                    break

    elif position == "TE":
        if window.my_team.item(5, 1) is None:
            window.my_team.setItem(5, 1, QTableWidgetItem(name))
        else:
            for i in range(8):
                if window.my_team.item(i + 9, 1) is None:
                    window.my_team.setItem(i + 9, 1, QTableWidgetItem(name))
                    break

    elif position == "DEF":
        if window.my_team.item(7, 1) is None:
            window.my_team.setItem(7, 1, QTableWidgetItem(name))
        else:
            for i in range(8):
                if window.my_team.item(i + 9, 1) is None:
                    window.my_team.setItem(i + 9, 1, QTableWidgetItem(name))
                    break

    elif position == "K":
        if window.my_team.item(8, 1) is None:
            window.my_team.setItem(8, 1, QTableWidgetItem(name))
        else:
            for i in range(8):
                if window.my_team.item(i + 9, 1) is None:
                    window.my_team.setItem(i + 9, 1, QTableWidgetItem(name))
                    break

    window.drafting_teams.removeColumn(0)


def remove_player(window):

    # TODO - This code is copied from the first half of draft_player, find way to not repeat code
    content = ""
    position = ""
    name = ""
    all_table = 0  # used to keep up with if the player was drafted from "all" table or position table

    # remove the row from the table
    if window.all_table.isVisible():
        content = window.all_table.selectedItems()
        position = content[1].text()
        name = content[0].text()

        current_row = window.all_table.currentRow()
        window.all_table.removeRow(current_row)
        all_table = 1

    elif window.qb_table.isVisible():
        content = window.qb_table.selectedItems()
        name = content[0].text()
        current_row = window.qb_table.currentRow()
        window.qb_table.removeRow(current_row)
        position = "QB"

    elif window.rb_table.isVisible():
        content = window.rb_table.selectedItems()
        name = content[0].text()
        current_row = window.rb_table.currentRow()
        window.rb_table.removeRow(current_row)
        position = "RB"

    elif window.wr_table.isVisible():
        content = window.wr_table.selectedItems()
        name = content[0].text()
        current_row = window.wr_table.currentRow()
        window.wr_table.removeRow(current_row)
        position = "WR"

    elif window.te_table.isVisible():
        content = window.te_table.selectedItems()
        name = content[0].text()
        current_row = window.te_table.currentRow()
        window.te_table.removeRow(current_row)
        position = "TE"

    elif window.def_table.isVisible():
        content = window.def_table.selectedItems()
        name = content[0].text()
        current_row = window.def_table.currentRow()
        window.def_table.removeRow(current_row)
        position = "DEF"

    elif window.k_table.isVisible():
        content = window.k_table.selectedItems()
        name = content[0].text()
        current_row = window.k_table.currentRow()
        window.k_table.removeRow(current_row)
        position = "K"

    # remove player from the other table they're in
    if all_table:

        # remove from position table
        if position == "QB":
            item = window.qb_table.findItems(name, Qt.MatchFixedString)
            row = window.qb_table.row(item[0])
            window.qb_table.removeRow(row)

        elif position == "RB":
            item = window.rb_table.findItems(name, Qt.MatchFixedString)
            row = window.rb_table.row(item[0])
            window.rb_table.removeRow(row)

        elif position == "WR":
            item = window.wr_table.findItems(name, Qt.MatchFixedString)
            row = window.wr_table.row(item[0])
            window.wr_table.removeRow(row)
        elif position == "TE":
            item = window.te_table.findItems(name, Qt.MatchFixedString)
            row = window.te_table.row(item[0])
            window.te_table.removeRow(row)

        elif position == "DEF":
            item = window.def_table.findItems(name, Qt.MatchFixedString)
            row = window.def_table.row(item[0])
            window.def_table.removeRow(row)

        elif position == "K":
            item = window.k_table.findItems(name, Qt.MatchFixedString)
            row = window.k_table.row(item[0])
            window.k_table.removeRow(row)

    # remove from "all" table
    else:
        item = window.all_table.findItems(name, Qt.MatchFixedString)
        row = window.all_table.row(item[0])
        window.all_table.removeRow(row)

    # remove from watchlist if player is there
    item = window.watch_list.findItems(name, Qt.MatchFixedString)
    if len(item) > 0:
        row = window.watch_list.row(item[0])
        window.watch_list.removeRow(row)

    window.drafting_teams.removeColumn(0)


# cpu drafts a player
def cpu_draft(window):
    if (
        window.drafting_teams.item(0, 0).text() != "Your Team"
        and window.row_to_remove != -1
    ):
        display_all(window)
        window.all_table.selectRow(window.row_to_remove)
        remove_player(window)
        window.row_to_remove = -1


# highlight the pick the cpu is about to make
def highlight_pick(window):
    possible_selections = [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 4, 5, 6]

    if (
        window.drafting_teams.item(0, 0).text() != "Your Team"
        and window.row_to_remove == -1
    ):
        selection = choice(possible_selections)
        window.row_to_remove = selection
        display_all(window)
        window.all_table.item(selection, 0).setBackground(QBrush(QColor("Red")))


# adds player to watch list
def add_player_to_watchlist(window):

    # get name of player
    if window.all_table.isVisible():
        content = window.all_table.selectedItems()
        name = content[0].text()
    elif window.qb_table.isVisible():
        content = window.qb_table.selectedItems()
        name = content[0].text()
    elif window.rb_table.isVisible():
        content = window.rb_table.selectedItems()
        name = content[0].text()
    elif window.wr_table.isVisible():
        content = window.wr_table.selectedItems()
        name = content[0].text()
    elif window.te_table.isVisible():
        content = window.te_table.selectedItems()
        name = content[0].text()
    elif window.def_table.isVisible():
        content = window.def_table.selectedItems()
        name = content[0].text()
    elif window.k_table.isVisible():
        content = window.k_table.selectedItems()
        name = content[0].text()

    # appends a row
    window.watch_list.insertRow(window.watch_list.rowCount())

    # sets remove button and player name
    remove_button = QPushButton("X")
    remove_button.clicked.connect(lambda: remove_player_from_watchlist(window))

    # not sure why this doesn't work
    # remove_button.style().standardIcon(QStyle.SP_BrowserStop)

    window.watch_list.setCellWidget(window.watch_list.rowCount() - 1, 0, remove_button)

    item = QTableWidgetItem()
    item.setData(0, name)
    window.watch_list.setItem(window.watch_list.rowCount() - 1, 1, item)


# removes player from watch list
def remove_player_from_watchlist(window):
    window.watch_list.removeRow(window.watch_list.currentRow())
