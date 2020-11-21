from algosdk import account, encoding

# generate an account
private_key, address = account.generate_account()
# print("Private key:", private_key)
# print("Address:", address)
address = "36DTG5ITNWLAVZBSZ6BXPWP7UTSPEOL3K4HWIEUYML7RKUCBZQP5XBR7XY"
# check if the address is valid
if encoding.is_valid_address(address):
    print("The address is valid!")
else:
    print("The address is invalid.")