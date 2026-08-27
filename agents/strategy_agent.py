from agents.base_agent import BaseAgent

from models.schemas import StrategyData

from prompts.strategy_prompt import get_strategy_prompt


class StrategyAgent(BaseAgent):

    def __init__(self):
        super().__init__()

    def run(self, research, analysis):

        print("\n" + "=" * 70)
        print("STRATEGY AGENT")
        print("=" * 70)

        prompt = get_strategy_prompt(
            research,
            analysis
        )

        strategy_json = self.generate_json(
            prompt
        )

        strategy = StrategyData(
            **strategy_json
        )

        print("✓ Strategy Completed")

        return strategy