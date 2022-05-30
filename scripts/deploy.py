from brownie import FundMe, network, config
from scripts.helpful_scripts import getAccount


def deploy_fund_me():
    account = getAccount()
    # pass the price feed address to our fundme contract

    # if we are on a persistent network like rinkeby, use the associated address
    # otherwise, deploy mocks

    if network.show_active() != "development":
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]

    fund_me = FundMe.deploy(
        "0x8A753747A1Fa494EC906cE90E9f37563A8AF630e",
        {"from": account},
        publish_source=True,
    )
    print(f"contract deployed to{fund_me.address}")


def main():
    deploy_fund_me()
