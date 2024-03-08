import configparser
from Src.LLMs.GptBase import GPTBasedLLMs
from Src.Yahoo.dataloader import DataLoader

#  Load Configs
config = configparser.ConfigParser()
config.read('config.ini')

# get the config paths
folder_path = config.get('Yahoo', 'dataset_folder_path')
prompt_template_path = config.get('Yahoo', 'prompt_template_path')
role_def_path = config.get('Yahoo', 'role_def_path')

def main(folder_path, prompt_file_path):
    """
    Main function to process data from a folder and generate outputs using a prompt template.
    """
    data_loader = DataLoader(folder_path)

    # Load data
    data = data_loader.get_data()  # This will be a list of DataFrames

    # Check if we got any data to process
    if not data:
        print("No data loaded.")
        return

    # Initialize the LLM with the prompt template path (assuming API key is fetched from environment)
    llm = GPTBasedLLMs(prompt_template_path=prompt_file_path)

    # Load the prompt template
    prompt_template = llm.load_prompt_template()

    # For simplicity, let's assume we're just using the first DataFrame as our data source
    df = data[0]  # Using the first DataFrame from the data list

    # Generate a prompt from the first row of the DataFrame (customize this as needed)
    example_row = df.iloc[0]
    prompt = prompt_template.format(timestamp=example_row['timestamp'],
                                    value=example_row['value'],
                                    is_anomaly=example_row['is_anomaly'])

    # Use the LLM to generate a response based on the prompt
    response = llm.evaluate(prompt)

    print("Generated Response:", response)

if __name__ == "__main__":
    main(folder_path, prompt_template_path)
