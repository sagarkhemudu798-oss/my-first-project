import sys

class ATM:
    def __init__(self, pin, balance=1000):
        self.pin = pin
        self.balance = balance

    def check_pin(self, user_pin):
        return self.pin == user_pin

    def check_balance(self):
        print(f"\n💰 ଆପଣଙ୍କ ଆକାଉଣ୍ଟ ବାଲାନ୍ସ ହେଉଛି: {self.balance} ଟଙ୍କା")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"\n✅ {amount} ଟଙ୍କା ସଫଳତାର ସହ ଜମା ହେଲା।")
            print(f"💵 ସାମ୍ପ୍ରତିକ ବାଲାନ୍ସ: {self.balance} ଟଙ୍କା")
        else:
            print("\n❌ ଅବୈଧ ଟଙ୍କା (Invalid amount)!")

    def withdraw(self, amount):
        if amount > self.balance:
            print("\n❌ ଆପଣଙ୍କ ଆକାଉଣ୍ଟରେ ପର୍ଯ୍ୟାପ୍ତ ଟଙ୍କା ନାହିଁ (Insufficient Balance)!")
        elif amount <= 0:
            print("\n❌ ଅବୈଧ ଟଙ୍କା (Invalid amount)!")
        else:
            self.balance -= amount
            print(f"\n✅ {amount} ଟଙ୍କା ସଫଳତାର ସହ ଉଠାଗଲା।")
            print(f"💵 ସାମ୍ପ୍ରତିକ ବାଲାନ୍ସ: {self.balance} ଟଙ୍କା")

# --- ମୁଖ୍ୟ ପ୍ରୋଗ୍ରାମ୍ (Main Program) ---
def main():
    # ଏଠାରେ Default PIN '1234' ଏବଂ ପ୍ରାରମ୍ଭିକ ବାଲାନ୍ସ ୫୦୦୦ ଟଙ୍କା ରଖାଯାଇଛି
    my_atm = ATM(pin="1234", balance=5000)
    
    print("=== 🏦 ATM ସିମୁଲେସନ୍‌କୁ ସ୍ୱାଗତ 🏦 ===")
    
    # ୩ ଥର ଭୁଲ୍ PIN ମାରିଲେ ପ୍ରୋଗ୍ରାମ୍ ବନ୍ଦ ହୋଇଯିବ
    chances = 3
    while chances > 0:
        entered_pin = input("\n🔐 ଆପଣଙ୍କ ୪ ଅଙ୍କ ବିଶିଷ୍ଟ PIN ମାରନ୍ତୁ: ")
        if my_atm.check_pin(entered_pin):
            print("\n✅ PIN ଭେରିଫିକେସନ୍ ସଫଳ ହେଲା!")
            break
        else:
            chances -= 1
            print(f"❌ ଭୁଲ୍ PIN! ଆଉ {chances} ଥର ଚେଷ୍ଟା କରିପାରିବେ।")
            
    if chances == 0:
        print("\n❌ ୩ ଥର ଭୁଲ୍ PIN ମାରିଛନ୍ତି। ଆପଣଙ୍କ କାର୍ଡ ବ୍ଲକ୍ ହୋଇଯାଇଛି!")
        sys.exit()

    # ATM ମେନୁ (Menu)
    while True:
        print("\n-------------------------")
        print("୧. ବାଲାନ୍ସ ଚେକ୍ (Check Balance)")
        print("୨. ଟଙ୍କା ଜମା (Deposit)")
        print("୩. ଟଙ୍କା ଉଠାଇବା (Withdraw)")
        print("୪. ବାହାରକୁ ଯାଆନ୍ତୁ (Exit)")
        print("-------------------------")
        
        choice = input("ଆପଣ କଣ କରିବାକୁ ଚାହୁଁଛନ୍ତି? (1/2/3/4) ବାଛନ୍ତୁ: ")
        
        if choice == '1':
            my_atm.check_balance()
        elif choice == '2':
            amt = float(input("💰 କେତେ ଟଙ୍କା ଜମା କରିବେ ଲେଖନ୍ତୁ: "))
            my_atm.deposit(amt)
        elif choice == '3':
            amt = float(input("💸 କେତେ ଟଙ୍କା ଉଠାଇବେ ଲେଖନ୍ତୁ: "))
            my_atm.withdraw(amt)
        elif choice == '4':
            print("\n🙏 ଆମ ATM ବ୍ୟବହାର କରିଥିବାରୁ ଧନ୍ୟବାଦ! ଆପଣଙ୍କ ଦିନଟି ଶୁଭ ହେଉ।")
            break
        else:
            print("\n❌ ଭୁଲ୍ ବିକଳ୍ପ! ଦୟାକରି 1, 2, 3 କିମ୍ବା 4 ବାଛନ୍ତୁ।")

if __name__ == "__main__":
    main()
