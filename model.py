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

    def update(self,kwargs):
        
        valores=[]
        for x in kwargs.values():
            valores.append(x)

        colunas=[]
        for x in kwargs.keys():
            colunas.append(x)

        self.where(kwargs['id'],"id","=")

        sql = self.set("usuarios",valores,colunas)
        #print(sql)
        self.insert(sql)
    def listall(self):
        
        self.select('id') #indice 0 
        self.select('usuario')#indice 1
        self.select('banco')#indice 2
        self.select('agencia')#indice 3
        self.select('conta')#indice 4

        self.from_table("usuarios")
        sql = self.get()
        data = self.result_list(sql)
        return data

    def list_filt(self,search):
        

        self.select('id') #indice 0 
        self.select('usuario')#indice 1
        self.select('banco')#indice 2
        self.select('agencia')#indice 3
        self.select('conta')#indice 4
        self.select('CPF')#indice 5
        self.select('CEP')#indice 6
        self.select('endereco')#indice 7
        self.select('cidade')#indice 8
        self.select('estado')#indice 9

        self.from_table("usuarios")
        if search:
            self.where(search,"usuario")
            
        sql = self.get()
        data = self.result_list(sql)
        return data     
        pass
 