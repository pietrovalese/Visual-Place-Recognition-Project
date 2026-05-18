import os

import gdown
import torch

URL = "https://drive.google.com/file/d/1B06ysb-Wjb4KDcNrl-7pyj1mJve1jqdk/view"


def get_clique_mining_model():
    # Load the SALAD model (which has the same architecture as clique-mining)
    # and then load clique-mining's weights
    model = torch.hub.load("serizba/salad", "dinov2_salad")

    file_path = "trained_models/cliquemining.ckpt"

    if not os.path.exists(file_path):
        os.makedirs("trained_models", exist_ok=True)
        gdown.download(id=URL.split("/d/")[1].split("/")[0], output=file_path)

    state_dict = torch.load(file_path)["state_dict"]
    model.load_state_dict(state_dict)
    return model
