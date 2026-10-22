import asyncio
import pygame  # imported in main.py so the web build (pygbag) bundles it
from game import game_loop
from menu import menu_loop
from gamestate import GameState


async def main():
    while True:
        state = GameState()
        await menu_loop(state)
        await game_loop(state.rows, state.cols, state.mines)


asyncio.run(main())
