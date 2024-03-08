class LLMsInterface:
    def evaluate(self, prompt: str) -> str:
        """
        Generates a response from the LLM based on the given prompt.

        :param prompt: A string containing the prompt to be processed by the LLM.
        :return: A string containing the LLM's response.
        """
        raise NotImplementedError("This method needs to be implemented by subclasses.")
