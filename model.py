from donaclotilde import *

class Model(Donaclotilde):
    def __init__(self,):
        self.entrada_select=[]
        self.entrada_from_table=[]
        self.entrada_insert=[]
        self.entrada_count=[]
        self.entrada_where=[]
        self.query=[]

    def connect_db(self):
        self.conn = sqlite3.connect('database.db')
        self.cursor = self.conn.cursor()


    def save(self,kwargs):
        
        valores=[]
        for x in kwargs.values():
            valores.append(x)

        colunas=[]
        for x in kwargs.keys():
            colunas.append(x)

        sql = self.set("usuarios",valores,colunas)
        #print(sql)
        self.insert(sql)

    def listall(self):
        
        self.select('id') #indice 0 
        self.select('nome_cedente')#indice 1
        self.select('nome_banco')#indice 2
        self.select('nome_agencia')#indice 3
        self.select('nome_conta')#indice 4

        self.from_table("usuarios")
        sql = self.get()
        data = self.result_list(sql)
        return data

    def list_filt(self,search):
        

        self.select('id') #indice 0 
        self.select('nome_cedente')#indice 1
        self.select('nome_banco')#indice 2
        self.select('nome_agencia')#indice 3
        self.select('nome_conta')#indice 4

        self.from_table("usuarios")
        if search:
            self.where(search,"nome_cedente")
            
        sql = self.get()
        data = self.result_list(sql)
        return data     
        pass
 