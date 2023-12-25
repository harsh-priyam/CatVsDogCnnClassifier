from CatvsDogClassifier.config import ConfigurationManager
from CatvsDogClassifier.components import Evaluation
from CatvsDogClassifier import logger

class EvaluationPipeline:

    def __init__(self):
        pass
    
    def main(self):
      config = ConfigurationManager()
      val_config = config.get_validation_config()
      evaluation = Evaluation(val_config)
      evaluation.evaluation()
      evaluation.save_score()
    