#!/usr/bin/env python3
import tcod

from engine import Engine
from input_handlers import EventHandler
from entity import Entity

def main() -> None:

  width = 80
  height = 50

  #Define the font and Size  
  tileset = tcod.tileset.load_tilesheet(
    'dejavu10x10_gs_tc.png', 32, 8, tcod.tileset.CHARMAP_TCOD
  )

  event_handler = EventHandler()
  
  player = Entity(int(width/2), int(height / 2), '@', (190, 12, 35))
  npc = Entity(int(width/2 - 5), int(height / 2), '@', (255, 255, 0))
  entities = {npc, player}

  engine = Engine(entities=entities, event_handler=event_handler, player=player)

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
      engine.render(console=root, context=context)
      #Print the screen and update
      events = tcod.event.wait()

      engine.handle_events(events)

if __name__ == "__main__":
  main()