import os

from smolagents import CodeAgent, DuckDuckGoSearchTool, OpenAIModel

# The course uses InferenceClientModel, which routes through HF's Inference Providers.
# OpenAIModel points the same agent at Gemini's OpenAI-compatible endpoint instead.
model = OpenAIModel(
    model_id="gemini-3.5-flash-lite",
    api_base="https://generativelanguage.googleapis.com/v1beta/openai/",
    api_key=os.environ["GEMINI_API_KEY"],
)

agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=model)

agent.run("Search for the best music recommendations for a party at the Wayne's mansion.")
