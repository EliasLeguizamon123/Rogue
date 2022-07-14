#!/usr/bin/env python3
import tcod

from actions import EscapeAction, MovementAction
from input_handlers import EventHandler

def main() -> None:

  width = 80
  height = 50

  playerX = int(width / 2)
  playerY = int(height / 2)

  #Define the font and Size  
  tileset = tcod.tileset.load_tilesheet(
    'dejavu10x10_gs_tc.png', 32, 8, tcod.tileset.CHARMAP_TCOD
  )

  event_handler = EventHandler()

  #Create my window and define h, w, vsync, etc. 
  with tcod.context.new_terminal(
    width,
    height,
    tileset=tileset,
    title="Rogue",
    vsync=True,
  ) as context:
    root = tcod.Console(width, height, order="F")
    #Loop game
    while True:
      #Where the @ start
      root.print(x=playerX, y=playerY, string="@")
      #Print the screen and update
      context.present(root)

      root.clear()

      #Capture User input
      for event in tcod.event.wait():
        action = event_handler.dispatch(event)
        if action is None:
          continue
        #Movement
        if isinstance(action, MovementAction):
          playerX += action.dx
          playerY += action.dy
        #Quit
        elif isinstance(action, EscapeAction):
          raise SystemExit()

if __name__ == "__main__":
  main()