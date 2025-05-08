README FILE

42BKK
DISCOVERY PYTHON MAY 5th-9th, 2025
RUSH00 FINAL PROJECT: EX01 - THE LAST BONUS TRACK

TEAM
DEVOPS/ saku- (Detective Li) | temeenku (Khun Aun)

------------------------------
Re.: PROJECT EXPLANATION BASIS
------------------------------

A. INSTRUCTION:

    You can choose to create a (creative) functionality,

    "Your creative part of the bonus doesn’t have to be the same as the
    examples. You can be creative and add any functionality you want, as
    long as you justify it."

       Choose from 3-MODIFICATION THEME

       a. Create a program that accept files containing rows of a chessboard as arguments
          and checks if your King is "in check".
       b. Create a program that takes the best move for a checkmate.
       c. Create a chessgame.

B. RESPONSE:

    We choose to Create Game that also Integrates a Program that Suggest Best Moves 

C. PERFORMANCE:

    1. Our Mini-Chess Game would begin by putting all 4-Suspects:
       Queen(Q), Bishop(B), Rook(R), Pawn (P) onto the same chessboard at once.
    
    2. The 4-Suspects can be Easily Reduced to 1 or 3, depending on the needs of the Player.
       The Chessboard tiles also can be Easily Reduced or Expanded, depending on the needs
       of the Player.

    3. All 4-Suspects would be Randomly Placed by the game software at the start,
       Automatically.

    4. At the beginning of the game, the King(K) is hidden in Player's Hand;
       The King(K) would be disposed only by Player's own Decisive-Choice - Manually.
    
    5. The Logic Reasoning behind this issue is that, if the King(K) is also part of
       the Random Placement at the start, with 4-Enemies surrounding 1-King, the chance
       of probability that the King(K) would be directly Checkmated by the 4-Suspects
       reaches >90% possibility. Thus, if so, the game would END at its very start.

    6. The Mission of this mini-game would be: for the Player to Position the King(K)
       on the Chessboard, in a Clean-Single move, with a hope that the King(K) would
       Survive the 4-Suspects.
    
    7. The Game Automatically Hunts the King(K) by mathematically checks the grids.

    8. If the Player's King(K) manages to Survive the Hunt, a VICTORY would be awarded.

    9. If the King(K) got checked and dies, the Suspected Killer would be announced.

   10. Last but not the least, there is also a SECRET CHEAT-CODE for Player to view all
       of the HIDDEN SAFE ZONES MARKED IN GREEN for the King(K) to Survive. But once this
       Cheat-Code is Activated - The Game will STOP as a Game Over (by Cheating).

D. SOLUTION:

    1. We MODIFIED the Mandatory Codes and Added some Game-Engine Functionality in the
       separate checkmate library. We maintained the same mathematical library from the
       previous Mandatory Codes.

    2. We Added Subroutine for Reveal Safe Zones - corresponding to the Secret Cheat-Code.

    3. We created Interface where Player could INTERACT with the game, and to provide
       sufficient information-data regarding the play status for the Player. Player just 
       needs to enter the Coordinate Intercept as written on the chessboard, such as:
       a1, b3, e5, etc. to place the King(K); and it has been made CASE-INSENSITIVE to
       provide EASE for the Player.

    4. We added Coloring and Visual Tidiness for Improving ACCESSABILITY for the Player.

    5. The game will also AUTO-DETECT if Player wrongly positions the King(K) over any
       existing position for the 4-Suspects. If so, then the game will issue a warning,
       and Player would be ushered to select another position for the King(K).

    
