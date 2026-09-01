from typing import List


class SynthesisAgent:
    """
    Agent responsible for combining results from multiple agents.
    """

    def __init__(self):
        pass

    def synthesize(self, results: List[str]) -> str:
        """
        Combine multiple agent results into one final result.
        """

        print("\nSynthesis Agent received results:")

        for result in results:
            print(f"- {result}")

        final_result = "\n".join(results)

        print("\nSynthesized result:")
        print(final_result)

        return final_result