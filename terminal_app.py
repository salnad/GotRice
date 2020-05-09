import curses
from gotrice import RiceGetter
import time

menu = ['Get Rice', 'Exit (No More Rice)']
r = RiceGetter()

def print_menu(stdscr, selected_row_idx):
    stdscr.clear()
    h, w = stdscr.getmaxyx()

    for idx, row in enumerate(menu):
        x = w//2 - len(row)//2
        y = h//2 - len(menu)//2 + idx
        if idx == selected_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)
    stdscr.refresh()

def get_rice_loop(stdscr):
    print_get_rice(stdscr, r.get_rice())
    while True:
        key = stdscr.getch()
        time.sleep(2)
        r.play_game()
        if key == curses.KEY_ENTER or key in [10, 13]:
            break
        print_get_rice(stdscr, r.get_rice())

def print_get_rice(stdscr, rice_count):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    to_print = [f'Rice Collected: {rice_count}', 'Main Menu']
    for idx, row in enumerate(to_print):
        x = w//2 - len(row)//2
        y = h//2 - len(menu)//2 + idx
        if idx == 1:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)
    stdscr.refresh()

def print_center(stdscr, text):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    x = w//2 - len(text)//2
    y = h//2
    stdscr.addstr(y, x, text)
    stdscr.refresh()


def main(stdscr):
    # turn off cursor blinking
    curses.curs_set(0)
    curses.halfdelay(5)
    # color scheme for selected row
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    # specify the current selected row
    current_row = 0
    # print the menu
    print_menu(stdscr, current_row)

    while 1:
        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu)-1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            if current_row == 0:
                get_rice_loop(stdscr)
            
            if current_row == 1:
                curses.halfdelay(20)
                print_center(stdscr, "Just one question, GotRice?")
                stdscr.getch()
                break

        print_menu(stdscr, current_row)


curses.wrapper(main)