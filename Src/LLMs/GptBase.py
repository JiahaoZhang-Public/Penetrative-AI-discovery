import openai
import os
from Src.LLMs.llms import LLMsInterface
class GPTBasedLLMs(LLMsInterface):
    def __init__(self, prompt_template_path: str = None, api_key: str = None):
        """
        Initializes the GPT-based LLM with the optional API key and the path to the prompt template.
        It tries to use the provided API key, if none is given, it looks for an API key in the environment variables.

        :param prompt_template_path: A string containing the file path to the prompt template.
        :param api_key: An optional string containing the OpenAI API key. If not provided, the method attempts to use an environment variable.
        """
        self.api_key = api_key if api_key else os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OpenAI API key not provided and not found in environment variables.")
        if prompt_template_path:
            self.prompt_template_path = prompt_template_path
        openai.api_key = self.api_key

    def load_prompt_template(self) -> str:
        """
        Loads the prompt template from the specified file path.

        :return: A string containing the prompt template.
        """
        with open(self.prompt_template_path, 'r') as file:
            prompt_template = file.read()
        return prompt_template

    def evaluate(self, prompt: str,role_def: str = None) -> str:
        """
        Generates a response from the GPT-based LLM using OpenAI's API, based on the given prompt.

        :param prompt: A string containing the prompt to be processed by the LLM.
        :param role_def: A string defines the role of gpt assistant

        :return: A string containing the LLM's response.
        """
        if not role_def:
            role_def = 'You are a great data analyst.'

        response = openai.chat.completions.create(
            model="gpt-4-1106-preview",
            messages=[
                {"role": "system", "content": role_def},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content

    def estimate_gpt4_tokens(self,prompt):
        basic_tokens = prompt.split()
        print('estimate_gpt4_tokens:',len(basic_tokens))
if __name__ == '__main__':
    gpt = GPTBasedLLMs()
    print(gpt.evaluate(prompt='What is the whether today'))
