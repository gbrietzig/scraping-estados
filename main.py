from modules.gb_selenium import create_driver, access_url, catch_element, btn_click, catch_elements
from modules.gb_data_base import insert_base
from modules.gb_export_excel import export_base
import functions, json

url="https://cidades.ibge.gov.br/"

driver = create_driver()
access_url(url, driver)

btn_start=catch_element(0, "/html/body/app/shell/div/div[3]/home/div/div[1]/div/div/button", driver)
btn_click(btn_start)

btn_state=catch_element(0, "/html/body/app/shell/div/seletor-localidade/div/div[1]/nav/ul/li[2]", driver)
btn_click(btn_state)

ul_states=catch_element(0, "/html/body/app/shell/div/seletor-localidade/div/div[2]/ul", driver)
as_state=catch_elements(1, "a", ul_states)

states=[]
for a_state in as_state:
    state={}
    state_url=a_state.get_attribute("href")
    driver.execute_script("window.open(arguments[0])", state_url)
    driver.switch_to.window(driver.window_handles[1])

    state_name=catch_element(0, "/html/body/app/shell/div/aside/div/div/ul/li[2]/h1", driver)
    state["name"]=state_name.text

    state_gentilico=catch_element(0, "/html/body/app/shell/div/div[3]/panorama-shell/div/section[1]/panorama-resumo/div/div[1]/div[2]/div/p", driver)
    state["gentilico"]=state_gentilico.text

    state_capital=catch_element(0, "/html/body/app/shell/div/div[3]/panorama-shell/div/section[1]/panorama-resumo/div/div[1]/div[3]/div/p", driver)
    state["capital"]=state_capital.text

    data_table=catch_element(0, "/html/body/app/shell/div/div[3]/panorama-shell/div/section[1]/panorama-resumo/div/table", driver)

    data_table_trs_cabecalho=catch_elements(1, "tr.lista__cabecalho", data_table)
    for data_table_tr_cabecalho in data_table_trs_cabecalho:
        if " " not in data_table_tr_cabecalho.get_attribute('class'):
            btn_click(data_table_tr_cabecalho)
    
    for data_table_tr_cabecalho in data_table_trs_cabecalho:
        btn_click(data_table_tr_cabecalho)
        data_table_trs_indicador=catch_elements(1, "tr.lista__indicador", data_table)
        for data_table_tr_indicador in data_table_trs_indicador:
            if " " not in data_table_tr_indicador.get_attribute('class'):
                data_table_tr_indicador_tds=catch_elements(1, "td", data_table_tr_indicador)
                title=functions.tratament_string(data_table_tr_indicador_tds[1].text)
                data=functions.clear_string(data_table_tr_indicador_tds[2].text)
                state[title]=data
    
    states.append(state)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

insert_base(states, "tbl_states")
export_base(states, "ESTADOS")
object_json={
    'result': states
}
object_json=json.dumps(object_json, ensure_ascii=False)

with open(f".\\exports\\state.txt", "w") as f:
    f.write(object_json)