import chess
import chess.svg
import cairosvg
import io
import tkinter as tk
from PIL import ImageTk, Image


def draw_board(board, display=False):
    print(f'draw board here')
    board_svg = chess.svg.board(board)
    board_png = cairosvg.svg2png(bytestring=board_svg)
    if display == False:
        with open('board.png', 'wb') as f:
            f.write(board_png)  # save board as png file
    else:
        root = tk.Tk()
        img = ImageTk.PhotoImage(Image.open(io.BytesIO(board_png)).resize((800, 800)))
        panel = tk.Label(root, image=img)
        panel.pack()

        # Start the Tkinter event loop
        root.mainloop()
    return