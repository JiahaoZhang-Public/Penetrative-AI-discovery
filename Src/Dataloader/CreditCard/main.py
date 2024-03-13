'''
Author:Jiahao Zhang
Date； 2024/3/12
'''

import configparser
import os
from Src.LLMs.GptBase import GPTBasedLLMs
from Src.Dataloader.CreditCard.dataloader import CreditCardFraudDataLoader

current_script_path = os.path.abspath(__file__)
rootpath = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(current_script_path))))

# Load Configs
config = configparser.ConfigParser()
config.read(os.path.join(rootpath, 'config.ini'))

# get the config paths
dataset_path = os.path.join(rootpath, config['CreditCard']['dataset_path'])
prompt_template_path = os.path.join(rootpath, config.get('CreditCard', 'prompt_template_path'))
prompt_template_path_testsize_known = os.path.join(rootpath, config.get('CreditCard', 'prompt_template_path_testsize_known'))
role_def_path = os.path.join(rootpath, config.get('CreditCard', 'role_def_path'))
test_result_dir = os.path.join(rootpath, config.get('CreditCard', 'test_result_path'))
input_prompt_dir = os.path.join(rootpath, config.get('CreditCard', 'input_prompt_path'))
test_examples_dir = os.path.join(rootpath, config.get('CreditCard', 'test_examples_path'))


def take_n_experiment(dataset_path, prompt_file_path, num_experiments=10,start_experiment_number=11):

    for experiment in range(start_experiment_number, start_experiment_number + num_experiments):
        print(f"Running experiment {experiment}/{start_experiment_number + num_experiments - 1}")
        # Create file paths for the current experiment
        test_result_path = os.path.join(test_result_dir, f"result_{experiment}.txt")
        input_prompt_path = os.path.join(input_prompt_dir, f"prompt_{experiment}.txt")
        test_examples_path = os.path.join(test_examples_dir, f"test_examples_{experiment}.csv")

        llm = GPTBasedLLMs(prompt_template_path=prompt_file_path)

        # Load the prompt template
        prompt_template = llm.load_prompt_template()

        # Get the test data
        data_loader = CreditCardFraudDataLoader(dataset_path, random_state=experiment + 42)
        test_data = data_loader.get_test_data(random_state=experiment + 42)

        # Save the test examples for accuracy calculation
        test_data.to_csv(test_examples_path, index=False)
        print(f"Test examples saved to: {test_examples_path}")

        # Sort and normalize the test data
        sorted_data = data_loader.sort_and_normalize(test_data)

        # Generate textual descriptions
        descriptions = data_loader.generate_textual_descriptions(sorted_data)

        # Select few-shot examples
        few_shot_examples = data_loader.select_few_shot_examples()

        # Include domain knowledge and few-shot examples in the prompt
        domain_knowledge = "In financial transactions, anomalies can indicate fraudulent activities, such as unusually high amounts or transactions occurring at odd hours."

        prompt = prompt_template.format(domain_knowledge=domain_knowledge, few_shot_examples=few_shot_examples,
                                        descriptions=descriptions)
        llm.estimate_gpt4_tokens(prompt)

        # Use the LLM to generate a response based on the prompt
        response = llm.evaluate(prompt)

        with open(input_prompt_path, 'w') as file:
            file.write(prompt)
        print(f"Inputted Prompt saved to: {input_prompt_path}")

        with open(test_result_path, 'w') as file:
            file.write(response)
        print(f"Generated response saved to: {test_result_path}")



if __name__ == "__main__":
    # Domain Knowledge + Few-Shot Examples + Transaction Descriptions(Test Data)
    take_n_experiment(dataset_path, prompt_template_path, num_experiments=10, start_experiment_number=1)
    # Domain Knowledge + Few-Shot Examples + Transaction Descriptions(Test Data)
    # + Priori Knowledge(Provide LLMs with the proportion of labels)
    take_n_experiment(dataset_path,prompt_template_path_testsize_known,num_experiments=10,start_experiment_number=11)
