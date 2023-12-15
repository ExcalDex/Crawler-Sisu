from typing import Any
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

#Para executar o código são necessárias as seguintes bibliotecas baixadas: webdriver-manager (Sim, sem o underscore), selenium.
#Versão do Python: 3.12.0; Versão do webdriver-manager: 4.0.1; Versão do selenium: 4.8.3.
#Comentários do cóidigo em pt-br.

#Observação 1: O código foi feito com base no layout do site oficial do Sisu (https://sisu.mec.gov.br/#/selecionados e https://sisu.mec.gov.br/#/selecionados-lista-espera) na data 27/11/2023. O código pode estar desatualizado para layouts futuros.
#Observação 2: É necessário ter o Google Chrome instalado para rodar o código. Se você deseja usar outro browser serão necessárias alterações no código.

class crawler:
    def __init__(self) -> None:
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.set_window_size(900, 800)
        
    def get_lista_selecionados(self) -> list[dict[str, Any]]:
        lista_de_instituicoes: list[dict[str, Any]] = []
        self.driver.get('https://sisu.mec.gov.br/#/selecionados')
        
        flag_acabou_instituição: bool = False
        i: int = 0
        select_de_instituicao = self.driver.find_element('xpath', '//*[@id="interna"]/div/div[2]/div[1]/div[2]/ng-select[1]/div/div/div[2]/input')
        select_de_local = self.driver.find_element('xpath', '//*[@id="interna"]/div/div[2]/div[1]/div[2]/ng-select[2]/div/div/div[2]/input')
        select_de_curso = self.driver.find_element('xpath', '//*[@id="interna"]/div/div[2]/div[2]/div[2]/ng-select[1]/div/div/div[2]/input')
        select_de_grau_e_turno = self.driver.find_element('xpath', '//*[@id="interna"]/div/div[2]/div[2]/div[2]/ng-select[2]/div/div/div[2]/input')

        while not flag_acabou_instituição:
            select_de_instituicao.click()
            self.driver.execute_script("arguments[0].scrollIntoView(true);", select_de_instituicao)
            try:
                elemento_select_de_instituicao = self.driver.find_element('xpath', f'/html/body/sisu-root/div/section/sisu-selecionados/div/section/div/div/div[2]/div[1]/div[2]/ng-select[1]/ng-dropdown-panel/div/div[2]/div[{i+1}]')
                nome_instituicao: str = elemento_select_de_instituicao.text
                elemento_select_de_instituicao.click()

                flag_acabou_local: bool = False
                j: int = 0
                while not flag_acabou_local: 
                    self.driver.execute_script("arguments[0].scrollIntoView(true);", select_de_local)
                    select_de_local.click()
                    try:
                        elemento_select_local = self.driver.find_element('xpath', f'/html/body/sisu-root/div/section/sisu-selecionados/div/section/div/div/div[2]/div[1]/div[2]/ng-select[2]/ng-dropdown-panel/div/div[2]/div[{j+1}]')
                        local: str = elemento_select_local.text
                        elemento_select_local.click()

                        flag_acabou_curso: bool = False
                        k: int = 0
                        while not flag_acabou_curso:
                            self.driver.execute_script("arguments[0].scrollIntoView(true);", select_de_curso)
                            select_de_curso.click()
                            try:
                                elemento_select_curso = self.driver.find_element('xpath', f'/html/body/sisu-root/div/section/sisu-selecionados/div/section/div/div/div[2]/div[2]/div[2]/ng-select[1]/ng-dropdown-panel/div/div[2]/div[{k+1}]')
                                curso: str = elemento_select_curso.text
                                elemento_select_curso.click()

                                flag_acabou_grau: bool = False
                                l: int = 0
                                while not flag_acabou_grau:
                                    self.driver.execute_script("arguments[0].scrollIntoView(true);", select_de_grau_e_turno)
                                    select_de_grau_e_turno.click()
                                    try:
                                        elemento_select_grau = self.driver.find_element('xpath', f'/html/body/sisu-root/div/section/sisu-selecionados/div/section/div/div/div[2]/div[2]/div[2]/ng-select[2]/ng-dropdown-panel/div/div[2]/div[{l+1}]')
                                        grau = elemento_select_grau.text
                                        self.driver.execute_script("arguments[0].scrollIntoView(true);", elemento_select_grau)
                                        elemento_select_grau.click()
                                        self.driver.find_element('xpath', '/html/body/sisu-root/div/section/sisu-selecionados/div/section/div/div/div[2]/div[3]/a').click()
                                        time.sleep(0.5)
                                        candidatos: list[dict] = self.__get_tabelas_selec()
                                        lista_de_instituicoes.append({"instituicao": nome_instituicao, "local_de_oferta": local,
                                                                      "curso": curso, "grau_e_turno": grau, "lista_candidatos": candidatos})
                                    except:
                                        flag_acabou_grau = True
                                    l += 1
                            except:
                                flag_acabou_curso = True
                            k += 1
                    except:
                        flag_acabou_local = True
                    j += 1
            except:
                flag_acabou_instituição = True
            i += 1

        return lista_de_instituicoes
    
    def get_lista_em_espera(self) -> list[dict[str, Any]]:
        lista_de_instituicoes: list[dict[str, Any]] = []
        self.driver.get('https://sisu.mec.gov.br/#/selecionados-lista-espera')
        
        flag_acabou_instituição: bool = False
        i: int = 0
        select_de_instituicao = self.driver.find_element('xpath', '//*[@id="interna"]/div/div[2]/div[1]/div[2]/ng-select[1]/div/div/div[2]/input')
        select_de_local = self.driver.find_element('xpath', '//*[@id="interna"]/div/div[2]/div[1]/div[2]/ng-select[2]/div/div/div[2]/input')
        select_de_curso = self.driver.find_element('xpath', '//*[@id="interna"]/div/div[2]/div[2]/div[2]/ng-select[1]/div/div/div[2]/input')
        select_de_grau_e_turno = self.driver.find_element('xpath', '//*[@id="interna"]/div/div[2]/div[2]/div[2]/ng-select[2]/div/div/div[2]/input')

        while not flag_acabou_instituição:
            select_de_instituicao.click()
            self.driver.execute_script("arguments[0].scrollIntoView(true);", select_de_instituicao)
            try:
                elemento_select_de_instituicao = self.driver.find_element('xpath', f'/html/body/sisu-root/div/section/sisu-selecionados-lista-espera/div/section/div/div/div[2]/div[1]/div[2]/ng-select[1]/ng-dropdown-panel/div/div[2]/div[{i+1}]')
                nome_instituicao: str = elemento_select_de_instituicao.text
                elemento_select_de_instituicao.click()

                flag_acabou_local: bool = False
                j: int = 0
                while not flag_acabou_local: 
                    self.driver.execute_script("arguments[0].scrollIntoView(true);", select_de_local)
                    select_de_local.click()
                    try:
                        elemento_select_local = self.driver.find_element('xpath', f'/html/body/sisu-root/div/section/sisu-selecionados-lista-espera/div/section/div/div/div[2]/div[1]/div[2]/ng-select[2]/ng-dropdown-panel/div/div[2]/div[{j+1}]')
                        local: str = elemento_select_local.text
                        elemento_select_local.click()

                        flag_acabou_curso: bool = False
                        k: int = 0
                        while not flag_acabou_curso:
                            self.driver.execute_script("arguments[0].scrollIntoView(true);", select_de_curso)
                            select_de_curso.click()
                            try:
                                elemento_select_curso = self.driver.find_element('xpath', f'/html/body/sisu-root/div/section/sisu-selecionados-lista-espera/div/section/div/div/div[2]/div[2]/div[2]/ng-select[1]/ng-dropdown-panel/div/div[2]/div[{k+1}]')
                                curso: str = elemento_select_curso.text
                                elemento_select_curso.click()

                                flag_acabou_grau: bool = False
                                l: int = 0
                                while not flag_acabou_grau:
                                    self.driver.execute_script("arguments[0].scrollIntoView(true);", select_de_grau_e_turno)
                                    select_de_grau_e_turno.click()
                                    try:
                                        elemento_select_grau = self.driver.find_element('xpath', f'/html/body/sisu-root/div/section/sisu-selecionados-lista-espera/div/section/div/div/div[2]/div[2]/div[2]/ng-select[2]/ng-dropdown-panel/div/div[2]/div[{l+1}]')
                                        grau = elemento_select_grau.text
                                        self.driver.execute_script("arguments[0].scrollIntoView(true);", elemento_select_grau)
                                        elemento_select_grau.click()
                                        self.driver.find_element('xpath', '/html/body/sisu-root/div/section/sisu-selecionados-lista-espera/div/section/div/div/div[2]/div[3]/a').click()
                                        time.sleep(0.5)
                                        candidatos: list[dict] = self.__get_tabelas_esp()
                                        lista_de_instituicoes.append({"instituicao": nome_instituicao, "local_de_oferta": local,
                                                                      "curso": curso, "grau_e_turno": grau, "lista_candidatos": candidatos})
                                    except:
                                        flag_acabou_grau = True
                                    l += 1
                            except:
                                flag_acabou_curso = True
                            k += 1
                    except:
                        flag_acabou_local = True
                    j += 1
            except:
                flag_acabou_instituição = True
            i += 1
        return lista_de_instituicoes

    def __get_tabelas_selec(self) -> list:
        lista_de_dados: list[dict] = []
        for j in range(2, 10):
            flag_acabou_linha: bool = False
            i: int = 0
            while not flag_acabou_linha:
                try:
                    tipo: str = "Ampla Concorrencia"
                    if j == 3:
                        tipo: str = "Cota Renda Baixa & Escola Publica"
                    if j == 4:
                        tipo: str = "Cota Racial & Renda Baixa & Escola Publica"
                    if j == 5:
                        tipo: str = "Cota Racial & Renda Baixa"
                    if j == 6:
                        tipo: str = "Cota Escola Publica"
                    if j == 7:
                        tipo: str  = "Cota Racial & Escola Publica"
                    if j == 8:
                        tipo: str = "Cota Deficiencia & Racial & Escola Publica & Renda Baixa"
                    if j == 9:
                        tipo: str = "Cota Deficiencia & Racial & Escola Publica"
                    
                    if self.driver.find_element('xpath', f'//*[@id="interna"]/div/div[3]/div[{j}]/div/div[{i+5}]/div[1]').text == "":
                        time.sleep(0.5)

                    a = {"classificacao": self.driver.find_element('xpath', f'//*[@id="interna"]/div/div[3]/div[{j}]/div/div[{i+5}]/div[1]').text,
                          "nome_cand": self.driver.find_element('xpath', f'//*[@id="interna"]/div/div[3]/div[{j}]/div/div[{i+5}]/div[2]').text,
                          "nota": self.driver.find_element('xpath', f'//*[@id="interna"]/div/div[3]/div[{j}]/div/div[{i+5}]/div[4]').text, "tipo": tipo}
                    
                    if a['classificacao'] == '':
                        a['classificacao'] = '1º'

                    lista_de_dados.append(a)
                except:
                    flag_acabou_linha = True
                i += 1
        return lista_de_dados
    
    def __get_tabelas_esp(self) -> list:
        lista_de_dados: list[dict] = []
        for j in range(1, 10):
            flag_acabou_linha: bool = False
            i: int = 0
            while not flag_acabou_linha:
                try:
                    tipo: str = "Ampla Concorrencia"
                    if j == 3:
                        tipo: str = "Cota Renda Baixa & Escola Publica"
                    if j == 4:
                        tipo: str = "Cota Racial & Renda Baixa & Escola Publica"
                    if j == 5:
                        tipo: str = "Cota Racial & Renda Baixa"
                    if j == 6:
                        tipo: str = "Cota Escola Publica"
                    if j == 7:
                        tipo: str  = "Cota Racial & Escola Publica"
                    if j == 8:
                        tipo: str = "Cota Deficiencia & Racial & Escola Publica & Renda Baixa"
                    if j == 9:
                        tipo: str = "Cota Deficiencia & Racial & Escola Publica"

                    if self.driver.find_element('xpath', f'//*[@id="interna"]/div/div[3]/div[{j}]/div/div[{i+5}]/div[1]').text == "":
                        time.sleep(0.5)
                    a = {"nome_cand": self.driver.find_element('xpath', f'//*[@id="interna"]/div/div[3]/div[{j}]/div/div[{i+5}]/div[1]').text,
                          "nota": self.driver.find_element('xpath', f'//*[@id="interna"]/div/div[3]/div[{j}]/div/div[{i+5}]/div[3]').text, "tipo": tipo}
                    lista_de_dados.append(a)
                except:
                    flag_acabou_linha = True
                i += 1
        return lista_de_dados
