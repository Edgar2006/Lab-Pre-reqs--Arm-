Գրեք Python ծրագիր՝ ստուգելու համար՝ արդյոք տրված թիվը զույգ է, թե կենտ։

Գրեք Python ծրագիր առաջին n բնական թվերի գումարը հաշվարկելու համար։

Գրեք Python ծրագիր՝ Ֆիբոնաչիի շարքը մինչև n թիվը տպելու համար։

Գրեք Python ծրագիր՝ ցուցակի ամենամեծ տարրը գտնելու համար:

Ստեղծեք Python դաս, որը կոչվում է BankAccount, որը ներկայացնում է բանկային հաշիվ: Դասը պետք է ունենա հետևյալ հատկանիշներն ու մեթոդները։

Հատկանիշներ:
account_number (a string). Հաշվի համարը:
մնացորդ (a float). Հաշվի ընթացիկ մնացորդը:

Մեթոդներ:
ավանդ (deposit). նշված գումարը ավելացնում է հաշվի մնացորդին:
հանում (withdraw). Հաշվի մնացորդից հանում է նշված գումարը:
get_balance(): Վերադարձնում է հաշվի ընթացիկ մնացորդը:
Հրահանգներ:
Սահմանել BankAccount դասը նշված հատկանիշներով և մեթոդներով:
Կիրառեք դեպոզիտ, դուրսբերում և get_balance մեթոդները՝ օգտագործելով համապատասխան տրամաբանությունը:
Փորձարկեք ձեր դասը՝ ստեղծելով BankAccount-ի օրինակ և կատարելով որոշ գործողություններ դրա վրա:

Example usage:

# Create a bank account with an initial balance of $100 
account = BankAccount("123456789", 100.0) 
# Deposit $50 
account.deposit(50.0) 
# Withdraw $30 
account.withdraw(30.0) 
# Get the current balance 
balance = account.get_balance() 
print(f"Current balance: ${balance}")


Expected output:

Current balance: $120.0


