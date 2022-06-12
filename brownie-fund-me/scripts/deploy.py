from brownie import accounts, FundMe, network, config, MockV3Aggregator
from web3 import Web3

from scripts.helpful_scripts import LOCAL_BLOCKCHAIN_ENVIRONMENTS, deploy_mocks

DECIMALS = 18
STARTING_PRICE = 2000

def deploy_fund_me():
  account = get_account()
  if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
    price_feed_address = config["networks"][network.show_active()]["eth_usd_price_feed"]
  else:
    deploy_mocks()
    price_feed_address = MockV3Aggregator[-1].address

  fund_me = FundMe.deploy(price_feed_address, {"from": account}, publish_source=config["networks"][network.show_active()].get("verify"))

def get_account():
  if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
      return accounts[0]
  else:
      return accounts.add(config["wallets"]["from_key"])

def main():
  deploy_fund_me()