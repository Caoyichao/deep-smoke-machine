import sys
from i3d_learner import I3dLearner
from ts_learner import TsLearner
from pt_ts_learner import PtTsLearner
from svm_learner import SvmLearner
from lstm_learner import LSTMLearner
from fusion_learner import FuseLearner


# Train the model
def main(argv):
    if len(argv) < 2:
        print("Usage: python train.py [method]")
        print("Optional usage: python train.py [method] [model_path]")
        return
    method = argv[1]
    if method is None:
        print("Usage: python train.py [method]")
        print("Optional usage: python train.py [method] [model_path]")
        return
    model_path = None
    if len(argv) > 2:
        model_path = argv[2]
    train(method=method, model_path=model_path)


def train(method=None, model_path=None):
    if method == "i3d-rgb":
        model = I3dLearner(mode="rgb")
        if model_path is None:
            model_path = "../data/pretrained_models/i3d_rgb_imagenet_kinetics.pt"
        model.fit(p_model=model_path)
    elif method == "i3d-flow":
        model = I3dLearner(mode="flow")
        if model_path is None:
            model_path = "../data/pretrained_models/i3d_flow_imagenet_kinetics.pt"
        model.fit(p_model=model_path)
    elif method == "ts-rgb":
        model = TsLearner(mode="rgb")
        model.fit()
    elif method == "ts-flow":
        model = TsLearner(mode="flow")
        model.fit()
    elif method == "pt-flow":
        model = PtTsLearner()
        model.fit(mode="pt-flow")
    elif method == "svm-rgb":
        model = SvmLearner(mode="rgb")
        model.fit()
    elif method == "svm-flow":
        model = SvmLearner(mode="flow")
        model.fit()
    elif method == "lstm":
        model = LSTMLearner()
        model.fit()
    elif method == "fuse":
        model = FuseLearner()
        model.fit()
    else:
        print("Method not allowed")
        return


if __name__ == "__main__":
    main(sys.argv)
