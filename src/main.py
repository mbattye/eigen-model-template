import sys
from src.config import Config
from src.data_loader import load_data, preprocess_data
from src.model import VirtualGaugeModel
from src.utils import setup_logger

def main():
    logger = setup_logger(Config.LOG_LEVEL)

    # Load data
    try:
        logger.info("Loading data...")
        data = load_data(Config.DATA_FILE)
    except Exception as e:
        logger.error(e)
        sys.exit(1)

    # Preprocess data
    input_vars = ["var1", "var2"]  # Example input variables
    output_var = Config.OUTPUT_VARIABLE_NAME

    try:
        logger.info("Preprocessing data...")
        data = preprocess_data(data, input_vars + [output_var])
    except Exception as e:
        logger.error(e)
        sys.exit(1)

    # Initialize and run the model
    model = VirtualGaugeModel()
    try:
        logger.info("Running inference...")
        result = model.run_inference(data, input_vars, output_var)
        logger.info("Inference completed. Results:")
        print(result)
    except Exception as e:
        logger.error(e)
        sys.exit(1)

if __name__ == "__main__":
    main()
