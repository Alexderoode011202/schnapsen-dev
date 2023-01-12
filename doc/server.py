
from schnapsen.bots import SchnapsenServer
from schnapsen.bots import RandBot, AlphaBetaBot, RdeepBot
from schnapsen.game import SchnapsenGamePlayEngine, Bot
import random
from schnapsen.bots import second_bot
from schnapsen.bots import second_bully
import click


@click.command()
@click.option('--bot', '-b',
                # And I added my bot here too
              type=click.Choice(['AlphaBetaBot',"second_bot", "bully_bot", 'RdeepBot', 'MLDataBot', 'MLPlayingBot', 'RandBot'], case_sensitive=False),
              default='RandBot', help="The bot you want to play against.")
def main(bot: str) -> None:
    """Run the GUI."""
    engine = SchnapsenGamePlayEngine()
    bot1: Bot
    with SchnapsenServer() as s:
        if bot.lower() == "randbot":
            bot1 = RandBot(12)
        elif bot.lower() in ["alphabeta", "alphabetabot"]:
            bot1 = AlphaBetaBot()
        elif bot.lower() == "rdeepbot":
            bot1 = RdeepBot(num_samples=16, depth=4, rand=random.Random(42))
            # Here I added my bot
        elif bot.lower() == "bully_bot":
            bot1 = second_bully()
        elif bot.lower() == "second_bot":
            bot1 = second_bot()  
        else:
            raise NotImplementedError
        bot2 = s.make_gui_bot(name="mybot2")
        # bot1 = s.make_gui_bot(name="mybot1")
        engine.play_game(bot1, bot2, random.Random(100))


if __name__ == "__main__":
    main()
