from web3 import Web3
from solcx import compile_files, install_solc, set_solc_version
import os
import streamlit as st

def deploy_and_mint_nft(ipfs_link):
    if not ipfs_link:
        st.error("IPFS link is required to mint the NFT.")
        return
    if not st.session_state.get('metamask_connected'):
        st.error("Please connect MetaMask first.")
        return

    # Install and set Solidity version
    install_solc('0.8.20')
    set_solc_version('0.8.20')

    # Define the path to the contracts folder
    contracts_path = 'E:/app4/@openzeppelin/contracts'

    # Solidity source files to compile
    contract_files = [
        os.path.join(contracts_path, 'token/ERC721/ERC721.sol'),
        os.path.join(contracts_path, 'access/Ownable.sol'),
        os.path.join(contracts_path, 'token/ERC721/extensions/ERC721URIStorage.sol'),
        'E:/app4/@openzeppelin/contracts/MyNFT.sol'
    ]

    # Compile the contracts
    compiled_sol = compile_files(contract_files, output_values=['abi', 'bin'])

    # Extract the main contract interface
    contract_key = '@openzeppelin/contracts/MyNFT.sol:MyNFT'
    if contract_key not in compiled_sol:
        st.error(f'Contract interface for MyNFT not found. Available keys: {list(compiled_sol.keys())}')
        return
    
    contract_interface = compiled_sol[contract_key]

    # Connect to Polygon Mumbai testnet
    infura_url = "https://polygon-amoy.infura.io/v3/41a8174eef734e4a9411c2e386bce358"
    w3 = Web3(Web3.HTTPProvider(infura_url))

    if not w3.is_connected():
        st.error("Failed to connect to the Polygon network")
        return

    # Use the account from MetaMask
    my_address = st.session_state.metamask_account
    private_key = st.session_state.metamask_private_key  # This should be securely managed

    # Deploy the contract
    contract = w3.eth.contract(abi=contract_interface['abi'], bytecode=contract_interface['bin'])
    nonce = w3.eth.get_transaction_count(my_address)

    deploy_txn = contract.constructor().build_transaction({
        'chainId': 80002,  # Mumbai Testnet Chain ID
        'gas': 2500000,
        'gasPrice': w3.to_wei('50', 'gwei'),
        'nonce': nonce,
    })

    signed_txn = w3.eth.account.sign_transaction(deploy_txn, private_key=private_key)

    try:
        tx_hash = w3.eth.send_raw_transaction(signed_txn.raw_transaction)
        tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        contract_address = tx_receipt.contractAddress
        st.success(f"Contract deployed at {contract_address}")
    except Exception as e:
        st.error(f"Deployment failed: {e}")
        return

    # Mint the NFT
    nonce = w3.eth.get_transaction_count(my_address)
    contract_instance = w3.eth.contract(address=contract_address, abi=contract_interface['abi'])
    mint_txn = contract_instance.functions.createNFT(ipfs_link).build_transaction({
        'chainId': 80002,
        'gas': 3000000,
        'gasPrice': w3.to_wei('50', 'gwei'),
        'nonce': nonce,
    })

    signed_mint_txn = w3.eth.account.sign_transaction(mint_txn, private_key=private_key)

    try:
        mint_tx_hash = w3.eth.send_raw_transaction(signed_mint_txn.raw_transaction)
        mint_tx_receipt = w3.eth.wait_for_transaction_receipt(mint_tx_hash)
        st.success(f"NFT minted! Transaction hash: {mint_tx_receipt.transactionHash.hex()}")
    except Exception as e:
        st.error(f"Minting failed: {e}")

    return contract_address
