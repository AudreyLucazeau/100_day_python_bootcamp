from grid import Grid
from random import choice

class VS_Computer(Grid):

    def __init__(self):
        super().__init__()


    def est_fini(self, x, y, pion):
        if self.grid[x][y] == pion and self.lenght_max_alignment(x, y, pion) == self.align - 1:
            self.afficher_plateau()
            if pion == 'X':
                print("Vous avez gagné")
            else:
                print("Vous avez perdu")
            return True
        if self.nbCoups == self.size ** 2:
            self.afficher_plateau()
            print("Partie Nulle")
            return True
        return False


    def choix_coup_ordinateur(self):
        alignment_length_player = []
        alignment_length_computer = []
        for x in range(self.size):
            for y in range(self.size):
                if self.grid[x][y] == " ":
                    alignment_length_computer.append(self.lenght_max_alignment(x, y, 'O'))
                    alignment_length_player.append(self.lenght_max_alignment(x, y, 'X'))
                else:
                    alignment_length_computer.append(0)
                    alignment_length_player.append(0)


        #positions index that allow the computer to increases his maximun chain
        indexes_computer = [i for i, j in enumerate(alignment_length_computer) if j == max(alignment_length_computer)]
        #positions index that could allow the player to create his longest chain, and that the computer has to block
        indexes_player = [i for i, j in enumerate(alignment_length_player) if j == max(alignment_length_player)]

        #Look for commun index, that allows computer to aact on both problem
        optimum_index = list(set(indexes_player) & set(indexes_computer))

        #If there is no commun position, we choose the one that act on the longest chain.
        if len(optimum_index)==0:

            if max(alignment_length_computer) >= max(alignment_length_player):
                position = choice(indexes_computer)
            else:
                position = choice(indexes_player)
        else:
            position = choice(optimum_index)

        x = position // self.size
        y = position % self.size

        return [x, y]

    def jouer(self):
        fini_ok = False
        joueur = 'X'
        while not fini_ok:
            self.afficher_plateau()
            x, y = self.saisie_coup(joueur)
            x, y = x - 1, y - 1
            self.mise_a_jour(x, y, joueur)
            fini_ok = self.est_fini(x, y, joueur)
            if not fini_ok:
                x, y = self.choix_coup_ordinateur()
                self.mise_a_jour(x, y, 'O')
                fini_ok = self.est_fini(x, y, 'O')







