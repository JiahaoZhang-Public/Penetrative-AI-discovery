import configparser
import os
from Src.LLMs.GptBase import GPTBasedLLMs
from Src.Dataloader.CreditCard.dataloader import CreditCardFraudDataLoader

current_script_path = os.path.abspath(__file__)
rootpath = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(current_script_path))))
#  Load Configs
config = configparser.ConfigParser()
config.read(os.path.join(rootpath,'config.ini'))

# get the config paths
dataset_path = os.path.join(rootpath,config['CreditCard']['dataset_path'])
prompt_template_path = os.path.join(rootpath,config.get('CreditCard', 'prompt_template_path'))
role_def_path = os.path.join(rootpath,config.get('CreditCard', 'role_def_path'))

def main(dataset_path, prompt_file_path):
    """
    Main function to process data from a folder and generate outputs using a prompt template.
    """
    data_loader = CreditCardFraudDataLoader(dataset_path)

    # Initialize the LLM with the prompt template path (assuming API key is fetched from environment)
    llm = GPTBasedLLMs(prompt_template_path=prompt_file_path)

    # Load the prompt template
    prompt_template = llm.load_prompt_template()

    prompt = prompt_template.format(list = data_loader.load_data_as_tuples(data_loader.get_test_data()))
    print(prompt)
    # Use the LLM to generate a response based on the prompt
    response = llm.evaluate(prompt)

    print("Generated Response:", response)

if __name__ == "__main__":
    main(dataset_path, prompt_template_path)