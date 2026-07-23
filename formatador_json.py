import os
import json
import time

def limpar_caminho(caminho):
    """Remove lixo que o Windows adiciona ao arrastar ficheiros para o terminal."""
    return caminho.strip().strip('"').strip("'").replace('file:///', '')

def formatador_json():
    # Ativa o estilo Matrix (Fundo preto, Letras verdes)
    os.system('color 0a')
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("="*60)
        print("           FORMATADOR DE JSON OFFLINE (MATRIX)")
        print("="*60)
        
        entrada = input("\nArraste o ficheiro .json/.txt aqui (ou cole o JSON puro) e prima Enter:\n> ")
        entrada = limpar_caminho(entrada)
        
        if not entrada:
            continue
            
        try:
            # Tenta verificar se a entrada é um ficheiro físico
            if os.path.exists(entrada):
                print("\nA ler o ficheiro e a formatar...")
                with open(entrada, 'r', encoding='utf-8') as f:
                    dados = json.load(f)
                
                # Cria o nome do novo ficheiro formatado
                caminho_saida = entrada.rsplit('.', 1)[0] + "_formatado.json"
                
                with open(caminho_saida, 'w', encoding='utf-8') as f:
                    json.dump(dados, f, indent=4, ensure_ascii=False)
                    
                print(f"\n✅ Sucesso! Ficheiro formatado e guardado em:\n{caminho_saida}")
                
            else:
                # Caso o utilizador tenha colado o texto JSON direto no terminal
                dados = json.loads(entrada)
                print("\n✅ JSON Formatado com Sucesso:\n")
                print(json.dumps(dados, indent=4, ensure_ascii=False))
                
        except json.JSONDecodeError as e:
            print(f"\n⚠️ Erro de Sintaxe: O conteúdo não é um JSON válido.\nDetalhes: {e}")
        except Exception as e:
            print(f"\n⚠️ Erro inesperado: {e}")
            
        # Loop de continuidade
        continuar = input("\nDeseja formatar outro JSON? (S/N): ").strip().upper()
        if continuar != 'S':
            print("\nA encerrar o Formatador... Até logo!")
            time.sleep(2)
            break

if __name__ == "__main__":
    try:
        formatador_json()
    except Exception as e:
        # Se ocorrer um erro crítico, impede que o ecrã feche instantaneamente
        print(f"\n⚠️ Ocorreu um erro crítico que forçou o fecho: {e}")
        input("Prima Enter para sair...")