# import json
# import requests
# from web3 import Web3
# from solcx import compile_files, install_solc, set_solc_version
# from io import BytesIO
# from PIL import Image
# import random

# def download_nft_image(contract_address, token_id):
#     # Connect to Polygon Mumbai testnet
#     infura_url = "https://polygon-amoy.infura.io/v3/41a8174eef734e4a9411c2e386bce358"
#     w3 = Web3(Web3.HTTPProvider(infura_url))

#     if not w3.is_connected():
#         raise ConnectionError("Failed to connect to the Polygon network")

#     # Solidity version
#     install_solc('0.8.20')
#     set_solc_version('0.8.20')

#     # Compile the contract (using the same method you used to deploy)
#     contract_files = [
#         '@openzeppelin/contracts/token/ERC721/ERC721.sol',
#         '@openzeppelin/contracts/access/Ownable.sol',
#         '@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol',
#         '@openzeppelin/contracts/MyNFT.sol'
#     ]

#     compiled_sol = compile_files(contract_files, output_values=['abi'])

#     # Extract the main contract ABI
#     contract_key = '@openzeppelin/contracts/MyNFT.sol:MyNFT'
#     contract_abi = compiled_sol[contract_key]['abi']

#     # Create contract instance
#     contract = w3.eth.contract(address=contract_address, abi=contract_abi)

#     # Fetch the token URI (assuming the contract has a `tokenURI` function)
#     token_uri = contract.functions.tokenURI(token_id).call()

#     # Fetch the NFT metadata from the token URI
#     response = requests.get(token_uri)
#     print(token_uri)
#     if response.status_code != 200:
#         raise Exception(f"Failed to fetch metadata from {token_uri}")
    
#     def retrieve_file_from_ipfs(ipfs_link):
        
#         # Send a GET request to the file URL
#         response = requests.get(ipfs_link)

#         if response.status_code == 200:
#             # Return the content of the file
#             return response.content
#         else:
#             # Return None if the file retrieval fails
            
#             return None
#     file_content = retrieve_file_from_ipfs(token_uri)
#     if file_content:
#                         # Open the file content as an image
#                 img = Image.open(BytesIO(file_content))
                        
#                         # Save the image as a PNG file
#                 img.save(f"nft_{random.randint(100000, 999999)}.png", "PNG")
# # Example usage
# contract_address = "0x13A4d9D75cEB75087EA77DA0CEB89d558b2F9091"
# token_id = 0 # Replace with your Token ID
# download_nft_image(contract_address, token_id)
