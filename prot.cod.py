from datetime import date
import pymysql
hostPadrao = 'localhost'
userPadrao = 'root'
passPadrao = ''
banco = True
while True:
    print('carregando dados...')


    try:
        conecting = pymysql.connect(
            host = hostPadrao,
            user = userPadrao,
            passwd = passPadrao,
            database = 'Placas_do_joao'
        )
        comandsql = conecting.cursor()
        break

    except:
        try:
            conecting = pymysql.connect(
                host = hostPadrao,
                user = userPadrao,
                passwd =passPadrao
            )

            comandsql = conecting.cursor()
            comandsql.execute("create database Placas_do_joao")

            comandsql.execute("""
            CREATE TABLE `Placas_do_joao`.`Clientes` ( `Id` INT NOT NULL AUTO_INCREMENT ,
            `Nome` VARCHAR(50) NOT NULL ,
            `Tele` VARCHAR(50) NOT NULL ,            
            `Endereco` VARCHAR(50) NOT NULL ,
            PRIMARY KEY (`Id`))
            ENGINE = InnoDB;
            """)


            comandsql.execute("""
                        CREATE TABLE `Placas_do_joao`.`Pedidos` ( `Id` INT NOT NULL AUTO_INCREMENT ,
                        `NomeCli` VARCHAR(50) NOT NULL ,
                        `Qtddplaca` INT NOT NULL ,
                        `Frase` VARCHAR(50) NOT NULL ,
                        `CorPlaca` VARCHAR(50) NOT NULL ,
                        `CorFrase` VARCHAR(50) NOT NULL ,
                        `DataEnrega` INT NOT NULL ,
                        `Desc` INT NOT NULL ,
                        `ValorService` INT NOT NULL ,
                        PRIMARY KEY (`Id`))
                        ENGINE = InnoDB;
                        """)
            print('Criando tabelas...')



        except:
            a = input('''
            Algo errado aconteçeu...
            
            Não foi possivel se conectar com o banco de dados,verifique se voce iniciou o mesmo corretamente.
            caso voce tenha modificado a sua senha do banco - em relação ao padrão - ou seu banco não seja
            local - localhost -,escolha a opção 1 para adicionar sua senha e host personalizada,ou, escolha
            a opção 2 para continuar tendo ciencia da ausecia de salvamento em memoria involátil de dados.
            
            1 - Tentar novamente com seus dados de banco
            2 - Continuar com dado volátil
            ''').strip()

            if a == '1':
                hostPers = input('''
                Presione ENTER se seu banco é local.
                
                host: ''').strip()
                if hostPers == '':
                    pass
                else:
                    hostPadrao = hostPers

                userPers = input('''
                                Presione ENTER se seu user é padrão.
                                
                                user: ''').strip()
                if userPers =='':
                    pass

                else:
                    userPadrao = userPers

                passPers = input('''
                                                Presione ENTER se sua senha é padrão.

                                                senha: ''').strip()
                if passPers == '':
                    pass

                else:
                    userPadrao = passPers

            elif a == '2':
                banco = False
                break
            else:
                print('Responsta invalida')




















class Cliente(object):

    def __init__(self,nome,tel,endereco):
        self.__nome = nome
        self.__tel = tel
        self.__endereco = endereco
    def GetNome(self):
        return self.__nome
    def GetTel(self):
        return self.__tel
    def GetEndereco(self):
        return self.__endereco
    def SetNome(self,nome):
        self.__nome = nome
    def SetTel(self,tel):
        self.__tel = tel
    def SetEndereco(self,endereco):
        self.__endereco = endereco



class Pedidos(object):
    def __init__(self,nomeCliente,qtddPlaca,frase,corPlaca,corFrase,dataEntrega,ValorService,desc = 0):
        self.__nomeCliente = nomeCliente
        self.__qtddPlaca = qtddPlaca
        self.__frase = frase
        self.__corPlaca = corPlaca
        self.__corFrase = corFrase
        self.__dataEntrega = dataEntrega
        self.__desc = desc
        self.__ValorService = ValorService
    def GetnomeCliente(self):
        return self.__nomeCliente
    def GetqtddPlaca(self):
        return self.__qtddPlaca
    def Getfrase(self):
        return self.__frase
    def GetcorPlaca(self):
        return self.__corPlaca
    def GetcorFrase(self):
        return self.__corFrase
    def GetdataEntrega(self):
        return self.__dataEntrega
    def Getdatadesc(self):
        return self.__desc
    def GetValorService(self):
        return  self.__ValorService
    def SetnomeCliente(self,nomeCliente):
        self.__nomeCliente = nomeCliente
    def SetqtddPlaca(self,qtddPlaca):
        self.__qtddPlaca = qtddPlaca
    def Setfrase(self,frase):
        self.__frase = frase
    def SetcorPlaca(self,corPlaca):
        self.__corPlaca = corPlaca
    def SetcorFrase(self,corFrase):
        self.__corFrase = corFrase
    def SetdataEntrega(self,dataEntrega):
        self.__dataEntrega = dataEntrega
    def Setdesc(self,desc):
        self.__dataEntrega = desc
    def SetValorService(self,ValorService):
        self.__ValorService = ValorService










simulabancocli = []
simulabancosrvi= []

if banco == True:
    comandox  = 'SELECT * FROM `clientes`'
    comandsql.execute(comandox)
    result = comandsql.fetchall()
    for x in result:
        userADD = Cliente(x[1],int(x[2]),x[3])
        simulabancocli.append(userADD)

    comandox = 'SELECT * FROM `pedidos`'
    comandsql.execute(comandox)
    result = comandsql.fetchall()
    for x in result:
        PedidosADD = Pedidos(x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8])
        simulabancosrvi.append(PedidosADD)







def CadCliente():
    while True:
        nomex = input('Nome: ')
        if VerifNomeDuplicate(nomex) == False:
            break
        else:
            print('ja cadastrado')
    while True:
        try:
            telx = int(input('Telefone: '))
            break
        except:
            input('somente numeros.press ENTER for continue')

    while True:
        enderecox =  input('endereço: ')
        break
    cliente = Cliente(nomex,telx,enderecox)
    simulabancocli.append(cliente)

    if banco == True:
        comandos = """INSERT INTO `Clientes` (`Id`, `Nome`, `Tele`, `Endereco`) VALUES (NULL, '{}','{}','{}')""".format(nomex,str(telx),enderecox)
        comandsql.execute(comandos)
        conecting.commit()
    else:
        pass





def VerifNomeDuplicate(nome_cli):
    if len(simulabancocli) == 0:
        return False
    for c in range(len(simulabancocli)):
        a = simulabancocli[c].GetNome()
        if nome_cli == a:
            return True
        else:
            pass
    return False

def ListarCli():
    if len(simulabancocli) == 0:
        print('nenhum dado encontrado')
    else:
        for x in range(len(simulabancocli)):
            print('{}'.format(x+1),simulabancocli[x].GetNome())

def CadEncomenda():
    if len(simulabancocli) == 0:
        print('nenhum cliente cadastrado,faça isso primeiro')
        return False
    while True:
        try:
            ListarCli()
            clientN = int(input('escolha o cliente'))
            if clientN <= 0 or (clientN) > len(simulabancocli):
                input('informação não é valida')
            else:
                cliOBJ = simulabancocli[clientN-1]
                break
        except:
            print('informação não é valida')

    while True:
        try:
            alturaPlaca = int(input('Altura: '))
            larguraPlaca = int(input('Largura : '))
            break

        except:
            print('informação não é valida')
    while True:
        text_placa = input('frase da placa: ')
        if text_placa.strip() == 0:
            print('texto inválido')
            pass
        else:
            break
    while True:
        try:
            cor_placa = int(input('''cor da placa:
            1 - branca
            2 - cinza'''))
            if cor_placa in [2,1]:
                if cor_placa == 1:
                    cor_placa = 'branca'
                else:
                    cor_placa = 'cinza'

                break

        except:
            print('informação não é valida')
    while True:
        try:
            cor_frase = int(input('''cor da frase:
            1 - azul
            2 - vermelho
            3 - amarelo
            4 - preto 
            5 - verde'''))
            if cor_frase in [1,2,3,4,5]:
                if cor_frase == 1:
                    cor_frase = 'azul'
                elif cor_frase == 2:
                    cor_frase = 'vermelho'
                elif cor_frase == 3:
                    cor_frase = 'amarelo'
                elif cor_frase == 4:
                    cor_frase = 'preto'
                else:
                    cor_frase = 'verde'

                break

        except:
            print('informação não é valida')

    while True:
        try:
            data_entrega = int(input('Data da entrega( formato DDMMAA ): '))
            if DataTest(data_entrega) == True:
                break

        except:
            print('informação não é valida')





    while True:
        text_not_space = ''
        text_not_space_temp = text_placa.strip()
        for p in range(len(text_not_space_temp)):
            if not text_not_space_temp[p] == ' ':
                text_not_space += text_not_space_temp[p]
        custo = ((alturaPlaca * larguraPlaca) * 147.30) + len(text_not_space) * 0.32
        custo = round(custo,2)

        while True:
            descValue = 0
            try:
                desc = input('deseja aplicar desconto (S/N)')
                if desc.upper() == 'S':
                    descValue = int(input('valor do desconto: '))

                    if not descValue > custo:
                        custo -= descValue
                        break
                    else:
                        print('o valor do desconto não pode ser maior qoe {}.'.format(custo))

                elif desc.upper() == 'N':
                    break
                else:
                    print('resposta invalida')

            except:
                print('dado não é valido')



        break

    while True:
        sercico = Pedidos(cliOBJ.GetNome(),len(text_not_space),text_placa.strip(),cor_placa,cor_frase,data_entrega,custo,descValue)
        simulabancosrvi.append(sercico)

        if banco == True:

       #     comandos = """INSERT INTO `pedidos` (`Id`, `NomeCli`, `Qtddplaca`, `Frase`, `CorPlaca`, `CorFrase`, `DataEnrega`, `Desc`, `ValorService`) VALUES (NULL, '{}', '22', 'nnnnn', 'nnnnn', 'nnn', '12', '12', '12');)""".format(cliOBJ.GetNome(),len(text_not_space),text_placa.strip(),cor_placa,cor_frase,data_entrega,custo,descValue)
            comandos = "INSERT INTO `pedidos` (`Id`, `NomeCli`, `Qtddplaca`, `Frase`, `CorPlaca`, `CorFrase`, `DataEnrega`, `Desc`, `ValorService`) VALUES (NULL, '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');".format(cliOBJ.GetNome(),len(text_not_space),text_placa.strip(),cor_placa,cor_frase,data_entrega,descValue,custo)
            comandsql.execute(comandos)

            conecting.commit()

        input('''
        
        Cliente: {}
        Frase da placa: {}
        Cor da placa: {}
        Cor da frase: {}
        Data da entrega {}
        Qtdd de letras: {}
        Desconto Aplicado: {}
        Valor do serviço: {}
        
        O CLIENTE DEVE PAGAR AGORA O VALOR DE:
        Sinal: {}
        '''.format(sercico.GetnomeCliente(),sercico.Getfrase(),sercico.GetcorPlaca(),sercico.GetcorFrase(),FormatarData(sercico.GetdataEntrega()),sercico.GetqtddPlaca(),sercico.Getdatadesc(),sercico.GetValorService(),sercico.GetValorService()/2))
        print('-'*40)

        break





def DataTest(data):
    a = data
    datastr = str(a)
    if not len(datastr) == 6:
        return False
    else:
        dstr = datastr[0]+datastr[1]
        d = int(dstr)
        messtr = datastr[2] + datastr[3]
        mes = int(messtr)
        anostr = datastr[4] + datastr[5]
        ano = int(anostr)
        if not d <= 0 and not d > 31:
            pass
        else:
            return False
        if not mes <= 0 and not mes > 12:
            pass
        else:
            return False
        dat_atual = date.today()
        d_a = dat_atual.year
        d_astr = str(d_a)
        d_a = d_astr[2] + d_astr[3]
        d_a = int (d_a)
        if not ano < d_a:
            pass
        else:
            return False
        return True


def RealatorioClientes():
    for c in range(len(simulabancocli)):
        print('-'*40)
        print('Nome: ',simulabancocli[c].GetNome())
        print('Telefone: ',simulabancocli[c].GetTel())
        print('Endereço: ',simulabancocli[c].GetEndereco())
        print('-'*40)

def RealatorioServicos():

    for C in range(len(simulabancosrvi)):
        print('-'*40)
        print('Cliente: ',simulabancosrvi[C].GetnomeCliente())
        print('Frase da placa: ',simulabancosrvi[C].Getfrase())
        print('Cor da placa: ',simulabancosrvi[C].GetcorPlaca())
        print('Cor da frase : ',simulabancosrvi[C].GetcorFrase())
        print('Data da entrega : ',FormatarData(simulabancosrvi[C].GetdataEntrega()))
        print('Qtdd de letras: ',simulabancosrvi[C].GetqtddPlaca())
        print('Desconto Aplicado: ',simulabancosrvi[C].Getdatadesc())
        print('Valor do serviço - já apicado o desconto: ',simulabancosrvi[C].GetValorService())
        print('Sinal: ',simulabancosrvi[C].GetValorService()/2)
        print('-'*40)

def Relatorios():
    while True:
        relat = input("""
        1 - Relatório de cliente
        2 - Relatório de serviços
        
        0 - Voltar
        """)

        if relat == '1':
            RealatorioClientes()
            break
        elif relat == '2':
            RealatorioServicos()
            break
        elif relat in ('0','o','O'):
            break
        else:
            print('comando invalido')



def FormatarData(datt):
    dat = str(datt)
    return '{}{}/{}{}/20{}{}'.format(dat[0],dat[1],dat[2],dat[3],dat[4],dat[5])

while True:
    menu = input("""
    1- cadastro de cliente
    2- cadastro de serviços
    3- relatórios""")

    if menu == '1':
        CadCliente()
    elif menu == '2':
        CadEncomenda()
    elif menu == '3':
        Relatorios()
















'''    
    Pedidos.Getfrase()
    Pedidos.GetcorFrase()
    Pedidos.GetcorPlaca()
    Pedidos.Getdatadesc()
    Pedidos.GetdataEntrega()
    Pedidos.GetnomeCliente()
    Pedidos.GetqtddPlaca()

'''








while True:




    """   
        simulabancocli.append(Cliente('alexia',5195552021,'Dario MIlla'))
        simulabancocli.append(Cliente('Daniel Alfredo', 51555555, 'sahsdghg'))
        simulabancocli.append(Cliente('MArcio Fafredo', 5195551021, 'Rua da mortw'))
        simulabancocli.append(Cliente('Alexsandro Junior Escarpetti', 51995551041, 'Dario Totta 556'))
    
    simulabancosrvi.append(Pedidos('Melancia',52,'Frase de teste 1','preto','branco',221220,20,0))
    simulabancosrvi.append(Pedidos('Tales',54,'Frase de teste 2','Vermelha','Branca',250522,1000,0))

    RealatorioServicos()
    input()
    """

