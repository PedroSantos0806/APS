print("Iremos calcular o seu débito de carbono!")
a = 7.0
b = 3.0
op='N'

while op !="S" and op !="s":
    meses= float(input("Você possui o carro? Se sim, há quantos meses?"))
    estrada= float(input("Você costuma dirigir quantos KM por dia? (em média)"))
    print("Agora, iremos calcular o seu débito de carbono...")

    calculo= float((meses*(estrada*30) * a))

    print("Esse foi o tanto de Gás Carbonico emitido por seu automovel: \n" , calculo,"KG de gás")

    Débito= calculo * b
    print("Esse é o seu débito de carbono: \n","R$ :",Débito)

    print("Agora, iremos te mostrar o carro que está disponivel com o valor de débito de carbono que você precisa recompensar")

    if Débito>630000:
        print("Você poderá comprar uma Audi E-tron nova, da Audi, nesse link: \n 'https://www.audi.com.br/br/web/pt/etron-sb-form.html'")
    else:
        if Débito >520000:
            print("Você poderá comprar uma XC90 nova, da Volvo, nesse link: \n 'https://www.volvocars.com/br/cars/xc90-hybrid/'")
        else:
            if Débito>320000:
                print("Você poderá comprar uma XC60 nova, da Volvo, nesse link: \n 'https://www.volvocars.com/br/cars/xc60-hybrid/'")
            else:
                if Débito>260000:
                    print("Você poderá comprar um Fiat 500e, da Fiat, nesse link: \n 'https://caoachery.com.br/icar?utm_source=google&utm_medium=cpc&utm_campaign=havas_caoa-chery_jacarei_eletricos_icar_cpc_exploration-evaluation_brand_1108_google_search_leilao&utm_content=marca_na_net__eletricos_icar_texto_produto_na_na&utm_id=&gclid=Cj0KCQiAsdKbBhDHARIsANJ6-jfPyybfnyE9bfqdsRTm92lqeYAZknTbkH0-XuZkj7Ri9-3rJ5qn0jMaAojSEALw_wcB'")
                else:
                    if Débito>140000:
                        print("Você poderá comprar um Chery Icar, da Chery, nesse link: \n'https://caoachery.com.br/icar?utm_source=google&utm_medium=cpc&utm_campaign=havas_caoa-chery_jacarei_eletricos_icar_cpc_exploration-evaluation_brand_1108_google_search_leilao&utm_content=marca_na_net__eletricos_icar_texto_produto_na_na&utm_id=&gclid=Cj0KCQiAsdKbBhDHARIsANJ6-jfPyybfnyE9bfqdsRTm92lqeYAZknTbkH0-XuZkj7Ri9-3rJ5qn0jMaAojSEALw_wcB'")
                    else:
                        if Débito<0:
                            print("Você não tem nenhuma débito de Carbono, parábens!")
                        else:
                            print("Infelizmente, não possui um carro disponivel no seu valor de dédito de carbono")
    op = input("Digite S para sair do Sistema")