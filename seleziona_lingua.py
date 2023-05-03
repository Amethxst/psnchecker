import curses

def seleziona_lingua(stdscr):
    lingue = ['Italiano', 'English', 'Français', 'Español']
    selezione = 0

    curses.curs_set(0)  # Nascondo il cursore



    while True:
        stdscr.clear()
        h, w = stdscr.getmaxyx()
        x_start = w // 2 - 10

        for idx, lingua in enumerate(lingue):
            y = h // 2 - 2 + idx
            x = x_start + 3

            if idx == selezione:
                stdscr.attron(curses.A_BOLD)
                stdscr.addstr(y, x, lingua)
                stdscr.attroff(curses.A_BOLD)
                stdscr.addstr(y, x - 3, ">")  # Aggiungo la freccia per indicare la selezione corrente
            else:
                stdscr.addstr(y, x, lingua)

        stdscr.refresh()

        key = stdscr.getch()

        if key == curses.KEY_UP and selezione > 0:
            selezione -= 1
        elif key == curses.KEY_DOWN and selezione < len(lingue) - 1:
            selezione += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            return lingue[selezione]

if __name__ == '__main__':
    print(curses.wrapper(seleziona_lingua))