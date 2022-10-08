# Gitcoin

Gitcoin describes itself as a community of builders, creators and protocols that have come together in order to develop the future of the open internet. Gitcoin creates a community that supports new infrastructure for Web3 — includingn tools, technologies and networks — to foster development in the open-source sphere.

## Token

* Networks:
	* Ethereum: [GTC](https://etherscan.io/token/0xde30da39c46104798bb5aa3fe8b9e0e1f348163f)
* Dune Analytics Dashboards
	* [@ivanmolto / GitcoinDAO: Governance & Financial overview](https://dune.com/ivanmolto/Gitcoin-DAO)

## Donations

* Networks:
	* Ethereum: [0x14CB60F6Aca2b2A68d975743baCb33F01f587da5](https://etherscan.io/address/0x14CB60F6Aca2b2A68d975743baCb33F01f587da5)
* Dune Analytics Dashboards
	* [Gitcoin Donation](https://dune.com/gm365/gitcoin)

## Fraud Detection & Defense (FDD)

* [Fraud Detection & Defense](https://gitcoin.notion.site/Fraud-Detection-Defense-2bde13c0b8e74fda81435d94e49e2703)
* Gov Forum
	* [Closing the Gap between FDD and Gitcoin Passport Sybil Defenses](https://gov.gitcoin.co/t/closing-the-gap-between-fdd-and-gitcoin-passport-sybil-defenses/11218)
	* [The limits of Sybil defense (and how composability might help)](https://gov.gitcoin.co/t/the-limits-of-sybil-defense-and-how-composability-might-help/11524)
	* [Sybil Defence Ideas for Gitcoin and Grant Owners](https://gov.gitcoin.co/t/sybil-defence-ideas-for-gitcoin-and-grant-owners/11611)

## Source Code

* https://github.com/gitcoinco/grants-round
* https://github.com/gitcoinco/grant-hub
* https://github.com/gitcoinco/web
* [scorer](https://github.com/gitcoinco/scorer): Scoring service for gitcoin passport

## API Clients

* Python:
	* https://github.com/gitcoinco/python-api-client/

## The Grants

* [The Grants 2.0 Funding Stack - Choose Your Own Algorithm](https://gov.gitcoin.co/t/the-grants-2-0-funding-stack-choose-your-own-algorithm/10770)

### Grants Round 15 (GR15)

Datetime: 07-09-2022 15:00:00 UTC - 22-09-2022 23:59:59 UTC

* [Grant Approvals](https://www.notion.so/3940c8762a304e8c9630a05418ebd2a1?v=8fd78e98993e4dc29fd40a5b12a9ea75) - When new grant applications are received
* [Grant Disputes](https://www.notion.so/e79f1dd9e5074a1d986ee3f91b12943e?v=74372375b4ba42ebb269be219f2c452d) - When a grant is “flagged” by a user
* [Grant Appeals](https://www.notion.so/5627564cce204a0f8ae5af463873bb3d?v=2510b1a2634b4a0ea24cf2b81241d13a) - When a grant denied eligibility argues an incorrect judgment
* Dune Analytics Dashboards
	* [@gitcoin_dao / Gitcoin GR15 Dashboard](https://dune.com/gitcoin_dao/gr15-dashboard)
	* [@latsan / Gr15 Dashboard](https://dune.com/latsan/gr15-dashboard)
* Networks:
	* Ethereum: [0x7d655c57f71464b6f83811c55d84009cd9f5221c](https://etherscan.io/address/0x7d655c57f71464b6f83811c55d84009cd9f5221c)
	* Polygon: [0xb99080b9407436eBb2b8Fe56D45fFA47E9bb8877](https://polygonscan.com/address/0xb99080b9407436eBb2b8Fe56D45fFA47E9bb8877)
* Blog
	* [Gitcoin Grants Round 15: Round Results & Recap](https://go.gitcoin.co/blog/gr15-results)
	* [Gitcoin Grants Round 15 kicks off Sept. 7](https://go.gitcoin.co/blog/grants-round-15-kicks-off/)
* Gov Forum
	* [GR15 Round Structure](https://gov.gitcoin.co/t/proposal-gr15-round-structure/11272)
	* [GR15 Fraud Report](https://gov.gitcoin.co/t/gr15-fraud-report/11609)
* [Official Data](https://drive.google.com/drive/folders/17OdrV7SA0I56aDMwqxB6jMwoY3tjSf5w)
	* hackathon-contributions-dataset
		* txn_id - an internal ID for a contribution (off-chain)
		* user_id - an internal ID for a contributor
		* address - the wallet address used to contribute
		* grant_id - the ID of a grant on gitcoin
		* chain - the chain used for the contribution (eth, zksync, polygon...)
		* txn_hash - the hash of the transaction (on-chain)
		* network - mainnet or testnet
		* token - the token contributed
		* amount_in_usdt - the equivalent amount contributed in usdt
		* timestamp - the time of the contribution
	* grants_applications_gr15
		* grant_id - the ID of a grant on gitcoin
		* active - is it active at the moment of export (end of round) will it receive its matching or not
		* approved - was approved (illegible for matching)
		* address - the wallet address to receive the contributions
		* title - the title of the grant (name)
		* url - the url of the grant on Gitcoin website
		* description - the description of the grant
		* created_on - the time of creation
	* gr15_grants
		* grant_id - the ID of a grant on gitcoin
		* active - is it active at the moment of export (end of round) will it receive its matching or not
		* title - the title of the grant (name)
		* address - the wallet address to receive the contributions
		* amout_received - The total amount received all-time (usdt)
		* amount_received_in_round - the amount recieved this round (usdt)
		* contribution_count - the number of contributions
		* contributor_count - the number of contributors
		* description - the description of the grant
		* website - the website of the grant (not gitcoin page)
		* github_project_url - the github of the grant
		* twitter_handle_1 - the twitter handle of grant
		* twitter_handle_2 - the twitter handle of grant
		* twitter_verified - whether the twitter account was verified
		* created_on - the time of creation
		* last_update - the time of latest update by the grantee

### Grants Round 14 (GR14)

* [GR14 Governance Brief](https://gov.gitcoin.co/t/gr14-governance-brief/11050/1)