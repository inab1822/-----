Menu = {
    'americano': {
        'ingredients' :{
            'water' : 250,
            'coffee' : 18,
        },
        'cost' : 1500
    },
    'latte' : {
        'ingredients' : {
            'water' : 200,
            'coffee' : 24,
            'milk' : 150,
        },
        'cost' : 2500
    },
    'cappuccino' : {
        'ingredients' :{
            'water' : 250,
            'coffee' : 24,
            'milk' : 100,
        },
        'cost' : 3000,
    }
}

# 수익
profit = 0

# 자판기에 있는 재료 자원
resources = {
    'water' : 700,
    'milk' : 300,
    'coffee' : 200,
}
class Coffee:
    profit = 0
    def __init__(self,Menu,resources):
        self.Menu = Menu
        self.resources = resources

    def report(self):
        print('현재 제고입니다.')
        print('물 :'+str(self.resources['water'])+'ml')
        print('우유 :'+str(self.resources['milk'])+'ml')
        print('커피 :'+str(self.resources['coffee'])+'g')
        print('돈 : '+str(Coffee.profit)+'원')

        


def coffee_prompt():
    while True:
      try:
        coffe_name = input('어떤 커피를 원하세요? (아메리카노/라떼/카푸치노)')
        if coffe_name in Menu.keys():
           enough(coffe_name)
           return False
        elif coffe_name == 'report':
          rp = Coffee(Menu,resources)
          print(rp.report())# 커피 제고, 돈 출력
        elif coffe_name == 'off':
            print('안녕히 가세요.')
            return False
        else:
          raise ValueError
      except ValueError:
        print('올바르지 않은 입력입니다. 다시 입력해 주세요')
        

def enough(coffee_name):
    coffee_name_stuff = Menu[coffee_name]['ingredients']
    user_w= coffee_name_stuff['water']
    user_m= coffee_name_stuff['milk']
    user_c= coffee_name_stuff['coffee']
    re = Coffee(Menu,resources)
    resor_w = re.resources['water']
    resor_m = re.resources['milk']
    resor_c = re.resources['coffee']
    if user_w > resor_w or user_m > resor_m or user_c > resor_c:
      print('재료가 부족합니다')
    else:
      put_ur_money(coffee_name)
      

def put_ur_money(coffee_name):
    ur_coffee_m = Menu[coffee_name]['cost']
    print(f'{ur_coffee_m:,} 입니다. 돈을 넣어주세요')
    man = int(input('만원'))
    ochun = int(input('오천원'))
    chun = int(input('천원'))
    obec = int(input('오백원'))
    bec = int(input('백원'))
    oship = int(input('오십원'))
    ship = int(input('십원'))
    inserted_coin = man * 10000 + ochun * 5000 + chun * 1000 + obec * 500 + bec * 100 + oship * 50 + ship * 10
    if inserted_coin >= ur_coffee_m:
        ur_charge = inserted_coin - ur_coffee_m
        print(f'넣으신 금액은{inserted_coin:,}원 입니다.')
        print(f'거스름돈 {ur_charge:,}원 받아가세요.')
        coffee_maker(coffee_name, ur_coffee_m)
      
    else:
        print(f'넣으신 금액은{inserted_coin:,}원 입니다.')
        print('금액이 모자랍니다. 다시 돈을 넣어주세요')
        put_ur_money(coffee_name)
  
    
def coffee_maker(coffee_name,ur_coffee_m):
    print(f'{coffee_name}을(를) 만들고 있습니다. 잠시만 기다려 주세요.')
    coffee_name_stuff = Menu[coffee_name]['ingredients']
    user_w= coffee_name_stuff['water']
    user_m= coffee_name_stuff['milk']
    user_c= coffee_name_stuff['coffee']
    re = Coffee(Menu,resources)
    re.resources['water'] -= user_w
    re.resources['milk'] -= user_m
    re.resources['coffee'] -= user_c
    Coffee.profit += ur_coffee_m
  
coffee_prompt()

