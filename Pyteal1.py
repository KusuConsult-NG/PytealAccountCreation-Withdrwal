# simple.py
#!/usr/bin/env python3
from pyteal import *

def bank_for_account(receiver):
    """Only allow receiver to withdraw funds from this contract account."""
    is_payment = Txn.type_enum() == Int(1)
    is_correct_receiver = Txn.receiver() == Addr(receiver)
    is_one_tx = Global.group_size() == Int(1)
    is_not_close = Txn.close_remainder_to() == Global.zero_address()
    is_not_close_asset = Txn.asset_close_to() == Global.zero_address()
    return And(is_payment, is_correct_receiver, is_not_close, is_not_close_asset)
program = bank_for_account("ZZAF5ARA4MEC5PVDOP64JM5O5MQST63Q2KOY2FLYFLXXD3PFSNJJBYAFZM")
# print(compileTeal(program.teal(), Mode.Signature))
print(compileTeal(program, Mode.Application))