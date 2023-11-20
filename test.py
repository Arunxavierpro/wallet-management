from wallet import Wallet

def test_getbalance():
  obj = Wallet(40)
  obj.set_balance(20)
  assert obj.get_balance() == 20
  
