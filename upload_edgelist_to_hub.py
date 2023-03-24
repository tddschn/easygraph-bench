import os
from huggingface_hub import HfApi

# Set up the Hugging Face API client
api = HfApi()

# Set the directory path where the *.edgelist files are located
directory = "/Users/tscp/testdir/easygraph-bench/dataset"

# Loop over all *.edgelist files in the directory and upload them to the Hub
for filename in os.listdir(directory):
    if filename.endswith(".edgelist"):
        # Rename the file extension to .tsv
        new_filename = os.path.splitext(filename)[0] + ".tsv"
        # Upload the file to the dataset repository on the Hub
        api.upload_file(
            path_or_fileobj=os.path.join(directory, filename),
            path_in_repo=new_filename,
            repo_id="easygraph-bench/datasets",
            repo_type="dataset",
            # message="Added {} to dataset repository".format(new_filename),
        )
        print(f'Uploaded {new_filename} to dataset repository.')
