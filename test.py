from wallet import Wallet

def test_getbalance():
  obj = Wallet(0)
  obj.set_balance(40)
  assert obj.get_balance() == 40
  
