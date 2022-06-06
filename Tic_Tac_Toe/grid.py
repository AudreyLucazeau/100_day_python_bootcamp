def next_player(joueur):
    if joueur == 'X':
        return 'O'
    else:
        return 'X'


class Grid:

    # size : number of cells on each size.
    # alignment : number of signs to align to win the game
    def __init__(self):
        align = 0
        size = 0

        while size <= 1:
            try:
                size = int(input("Which size of grid do you want?"))
            except ValueError:
                pass

        while not (1 < align <= size):
            try:
                align = int(input("How may symbols in a row do you need to win? (Between 2 and " + str(size) + " )?"))
            except ValueError:
                print(f"Please enter a number between 2 and {size}.")

        # Initialisateur
        self.grid = []
        for _ in range(size):
            self.grid.append([" "] * size)
        self.size = size
        self.align = align
        # compte le compte de coups joués depuis le début de la partie
        self.nbCoups = 0

    def afficher_plateau(self):
        print("   ", end="")
        for i in range(self.size):
            print("  " + str(i + 1) + " ", end="")
        print("\n   ", end="")
        for i in range(self.size):
            print("----", end="")
        print()
        for line in range(self.size):
            print(str(line + 1) + " ", end="")
            for column in range(self.size):
                print(" | " + self.grid[line][column], end="")
            print(" |")
            print("   ", end="")
            for i in range(self.size):
                print("----", end="")
            print()

    def saisie_coup(self, joueur):
        valide = False
        line = 0
        column = 0
        # Demande au joueur une case tant qu'elle n'est pas valide
        while not valide:

            while line < 1 or line > self.size:
                try:
                    line = int(input("Joueur " + joueur +
                                      "  In which line would you like to play? \
                                     (Number between 1 and " + str(self.size) + "):"))
                # Dans lec as où x n'est pas un entier
                except ValueError:
                    pass

            # On demande de même un numéro de colomne
            while column < 1 or column > self.size:
                try:
                    column = int(input(
                        "Player " + joueur +
                        " In which column would you like to play?\
                        (Number between 1 and " + str(self.size) + "):"))
                except ValueError:
                    pass

            # Test si la case est vide
            valide = self.grid[line - 1][column - 1] == " "
            if self.grid[line - 1][column - 1] != " ":
                print("Cette case est déjà occupée")
            else:
                valide = True
        return [line, column]

    def mise_a_jour(self, x, y, joueur):
        self.grid[x][y] = joueur
        self.nbCoups += 1

    # Count the number of pieces aligned in a row, in a given direction, from a reference square.
    # x, y : coordinates of the reference square
    # dir_l : show the direction through the line
    #              -1 : move down by one line
    #               0 : stay on the same line
    #               1 : move up by one line
    # dir_c : show the direction through the column
    #              -1 : move to the left by one column
    #               0 : stay on the same column
    #               1 : move to the right by one column
    # pion : 'X' or 'O'
    def nb_pions_aligned(self, x, y, dir_l, dir_c, pion):

        # We don't take care of the case where there is no direction
        if dir_c == 0 and dir_l == 0:
            return 0
        try:
            caractere = self.grid[x + dir_l][y + dir_c]
        except IndexError:
            # The move is not possible from the reference square
            return 0
        else:
            # We cut the case of negative index, otherwise, the count will circle on the grid.
            if x + dir_l < 0 or y + dir_c < 0:
                return 0
            elif caractere == pion:
                return 1 + self.nb_pions_aligned(x + dir_l, y + dir_c, dir_l, dir_c, pion)
            else:
                return 0

    # Return the maximun of aligned pieces, on each direction
    def lenght_max_alignment(self, x, y, pion):
        vertical = self.nb_pions_aligned(x, y, 1, 0, pion) + self.nb_pions_aligned(x, y, -1, 0, pion)
        diag1 = self.nb_pions_aligned(x, y, 1, 1, pion) + self.nb_pions_aligned(x, y, -1, -1, pion)
        horizontal = self.nb_pions_aligned(x, y, 0, 1, pion) + self.nb_pions_aligned(x, y, 0, -1, pion)
        diag2 = self.nb_pions_aligned(x, y, -1, 1, pion) + self.nb_pions_aligned(x, y, 1, -1, pion)
        return max(vertical, diag1, horizontal, diag2)

    def est_fini(self, x, y, pion):
        if self.grid[x][y] == pion and self.lenght_max_alignment(x, y, pion) == self.align - 1:
            self.afficher_plateau()
            print("Player " + pion + " win")
            return True
        if self.nbCoups == self.size ** 2:
            self.afficher_plateau()
            print("No winner this time")
            return True
        return False

    def jouer(self):
        fini_ok = False
        joueur = 'X'
        while not fini_ok:
            self.afficher_plateau()
            x, y = self.saisie_coup(joueur)
            x, y = x - 1, y - 1
            self.mise_a_jour(x, y, joueur)
            fini_ok = self.est_fini(x, y, joueur)
            joueur = next_player(joueur)
