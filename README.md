# SCP-Extractor
Extract information about SCPs from the [wiki](http://www.scp-wiki.net/scp-series).


## Setup
You will need to have Python 3.x installed.

After installing Python 3.x, you can download the necessary python packages via
```bash
    pip install -r requirements.txtr
```

## Usage
To run the extraction script, do the following:

1. Run the extract.py script:
    ```shell
    python extract.py
    ```

2. Run with a starting number and last number with a csv file
    ```shell
    python extract.py -f 1 -l 10 -c scp.csv
    ```

Note: You may have to update the script to extract more SCP information.

## Authors

* **Jimmy Le** - [Jldevops](https://github.com/jldevops)

## License

Licensed under the [License](LICENSE)
