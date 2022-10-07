# minimal-scraper

## Usage

```shell
python -m venv .venv
(
    source .venv/bin/activate
    python -m pip install --upgrade pip
    python -m pip install jupyter
    python -m pip install ipykernel
    python -m ipykernel install --user --name=gitcoin-hackathon-datascience-29390--minimal-scraper
    python scraper-eth.py
)
```