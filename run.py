import argparse
import pandas as pd
import yaml
import json
import time
import logging
import sys


def setup_logging(log_file):
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )


def load_config(config_path):
    try:
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)

        required_keys = ["seed", "window", "version"]
        for key in required_keys:
            if key not in config:
                raise ValueError(f"Missing config key: {key}")

        return config
    except Exception as e:
        raise ValueError(f"Config error: {str(e)}")


def load_data(input_path):
    try:
        df = pd.read_csv(input_path)

        if df.empty:
            raise ValueError("CSV is empty")

        if "close" not in df.columns:
            raise ValueError("Missing 'close' column")

        return df
    except Exception as e:
        raise ValueError(f"Data error: {str(e)}")


def process(df, window):
    df["rolling_mean"] = df["close"].rolling(window=window).mean()
    df["signal"] = (df["close"] > df["rolling_mean"]).astype(int)
    return df


def compute_metrics(df, start_time):
    rows_processed = len(df)
    signal_rate = df["signal"].mean()
    latency_ms = int((time.time() - start_time) * 1000)

    return rows_processed, signal_rate, latency_ms


def write_success(output_path, config, rows, signal_rate, latency):
    output = {
        "version": config["version"],
        "rows_processed": rows,
        "metric": "signal_rate",
        "value": round(signal_rate, 4),
        "latency_ms": latency,
        "seed": config["seed"],
        "status": "success"
    }

    with open(output_path, 'w') as f:
        json.dump(output, f, indent=4)

    print(json.dumps(output, indent=4))


def write_error(output_path, config_version, error_msg):
    output = {
        "version": config_version if config_version else "v1",
        "status": "error",
        "error_message": error_msg
    }

    with open(output_path, 'w') as f:
        json.dump(output, f, indent=4)

    print(json.dumps(output, indent=4))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--config", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--log-file", required=True)

    args = parser.parse_args()

    start_time = time.time()
    config = None

    try:
        setup_logging(args.log_file)
        logging.info("Job started")

        config = load_config(args.config)
        logging.info(f"Config loaded: {config}")

        df = load_data(args.input)
        logging.info(f"Rows loaded: {len(df)}")

        df = process(df, config["window"])
        logging.info("Processing completed")

        rows, signal_rate, latency = compute_metrics(df, start_time)

        write_success(args.output, config, rows, signal_rate, latency)
        logging.info("Job completed successfully")

    except Exception as e:
        logging.error(str(e))
        write_error(args.output, config["version"] if config else None, str(e))
        sys.exit(1)


if __name__ == "__main__":
    main()