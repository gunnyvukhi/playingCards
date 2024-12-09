import pied_poker as pp
import numpy as np
np.random.seed(420)
def CaculateWinRate(PlayerCard, CommunityCard, TotalPlayers=2, num_simulations=1000):
    c1, c2 = PlayerCard
    # community_cards = pp.Card.of(*CommunityCard)
    p1 = pp.Player('Player', pp.Card.of(c1, c2))

    community_cards = pp.Card.of(*CommunityCard)
    simulator = pp.PokerRound.PokerRoundSimulator(community_cards=community_cards,
                        players=[p1],
                        total_players=TotalPlayers)
    num_simulations = num_simulations

    simulation_result = simulator.simulate(n=num_simulations, n_jobs=1)

    return "%.2f%%" % (simulation_result.probability_of(pp.Probability.PlayerWins(p1)).probability * 100)

if __name__ == "__main__":
    print(CaculateWinRate(('ac', '2c',), ['10s', '7h', 'ad'], 4, 10000))