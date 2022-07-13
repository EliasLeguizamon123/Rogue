#!/usr/bin/env python3
import tcod

def main():
  #Create Context and show it
  width = 80
  height = 50
  
  tileset = tcod.tileset.load_tilesheet(
    'dejavu10x10_gs_tc.png', 32, 8, tcod.tileset.CHARMAP_TCOD
  )

  with tcod.context.new_terminal(
    width,
    height,
    tileset=tileset,
    title="Rogue",
    vsync=True,
  ) as context:
    root = tcod.Console(width, height, order="F")
    while True:
      root.print(x=1, y=1, string="@")

      context.present(root)

      for event in tcod.event.wait():
        if event.type == "QUIT":
          raise SystemExit()

if __name__ == "__main__":
  main()