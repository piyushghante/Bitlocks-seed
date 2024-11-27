import streamlit as st
import json
import requests
from web3 import Web3
from solcx import compile_files, install_solc, set_solc_version
from io import BytesIO
from PIL import Image
import random
def UI_NFT_download():
    def download_nft_image(contract_address, token_id):
        # Connect to Polygon Mumbai testnet
        infura_url = "https://polygon-amoy.infura.io/v3/41a8174eef734e4a9411c2e386bce358"
        w3 = Web3(Web3.HTTPProvider(infura_url))

        if not w3.is_connected():
            raise ConnectionError("Failed to connect to the Polygon network")

        # Solidity version
        install_solc('0.8.20')
        set_solc_version('0.8.20')

        # Compile the contract (using the same method you used to deploy)
        contract_files = [
            '@openzeppelin/contracts/token/ERC721/ERC721.sol',
            '@openzeppelin/contracts/access/Ownable.sol',
            '@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol',
            '@openzeppelin/contracts/MyNFT.sol'
        ]

        compiled_sol = compile_files(contract_files, output_values=['abi'])

        # Extract the main contract ABI
        contract_key = '@openzeppelin/contracts/MyNFT.sol:MyNFT'
        contract_abi = compiled_sol[contract_key]['abi']

        # Create contract instance
        contract = w3.eth.contract(address=contract_address, abi=contract_abi)

        # Fetch the token URI (assuming the contract has a `tokenURI` function)
        token_uri = contract.functions.tokenURI(token_id).call()

        # Fetch the NFT metadata from the token URI
        response = requests.get(token_uri)
        #print(token_uri)
        if response.status_code != 200:
            raise Exception(f"Failed to fetch metadata from {token_uri}")
        
        def retrieve_file_from_ipfs(ipfs_link):
            
            # Send a GET request to the file URL
            response = requests.get(ipfs_link)

            if response.status_code == 200:
                # Return the content of the file
                return response.content
            else:
                # Return None if the file retrieval fails
                
                return None

        # Retrieve and process the file
        file_content = retrieve_file_from_ipfs(token_uri)
        if file_content:
            img = Image.open(BytesIO(file_content))
            # Save the image to a BytesIO object
            img_io = BytesIO()
            img.save(img_io, format='PNG')
            img_io.seek(0)
            return img_io
        else:
            st.error("Failed to retrieve image from IPFS")
            return None

    # Streamlit UI
    st.title("NFT Image Downloader")

    # User inputs
    contract_address = st.text_input("Contract Address", value="0x13A4d9D75cEB75087EA77DA0CEB89d558b2F9091")
    token_id = st.number_input("Token ID", value=0)

    if st.button("Download NFT Image"):
        image_io = download_nft_image(contract_address, token_id)
        
        if image_io:
            st.image(image_io, caption=f"NFT Image for Token ID: {token_id}")
            st.download_button(
                label="Download Image",
                data=image_io,
                file_name=f"nft_{random.randint(100000, 999999)}.png",
                mime="image/png"
            )
