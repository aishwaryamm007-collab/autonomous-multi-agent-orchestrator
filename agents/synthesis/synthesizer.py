from typing import List


class SynthesisAgent:
    """
    Agent responsible for combining results from multiple agents.
    """

    def __init__(self):
        pass

    def synthesize(self, results: List[str]) -> str:
        """
        Combine multiple agent results into one structured final result.
        """

        print("\nSynthesis Agent received results:")

        if not results:
            print("- No results available")

            return "No results were produced by the agents."

        for result in results:
            print(f"- {result}")

        sections = []

        for index, result in enumerate(results, start=1):
            sections.append(
                f"Result {index}:\n{result}"
            )

        final_result = (
            "========== SYNTHESIZED RESULT ==========\n\n"
            + "\n\n".join(sections)
            + "\n\n=========================================="
        )

        print("\nSynthesized result:")
        print(final_result)

        return final_result