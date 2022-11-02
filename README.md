# Discerning Dune Dashboards

[Hackathon: Gitcoin Open Data Science Hackathon - Discerning Dune Dashboards](https://gitcoin.co/issue/29390)

Create a Discerning Dune Dashboard, you will analyze the entirety of Grants Round 15 from Gitcoin and create Discerning Dune Dashboards that can be used to improve the operations of future Grants Rounds whether operated by Gitcoin or others.

## Development

Install:

```shell
pyenv install 3.9.13
pyenv global 3.9.13
python -m venv .venv
(
    source .venv/bin/activate
    python -m pip install --upgrade pip
    python -m pip install ipykernel jupyter web3 tqdm pandas gitcoin
    python -m ipykernel install --user --name=gitcoin-hackathon-datascience-29390--minimal-scraper
)
```

Scrape:

```shell
(
    source .venv/bin/activate
    python scraper-eth.py
)
```

Start **Jupyter Notebook**:

```shell
(
    source .venv/bin/activate
    python -m jupyter notebook
)
```

Uninstall:

```shell
(
    source .venv/bin/activate
    python -m jupyter kernelspec uninstall gitcoin-hackathon-datascience-29390--minimal-scraper
)
rm -rf .venv
```

## Issues

* Incompatible on Python 3.10.X, only 3.9.X and before