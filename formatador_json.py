import os
import json
import time

def limpar_caminho(caminho):
    """Remove sujeiras que o Windows adiciona ao arrastar arquivos no terminal."""
    return caminho.strip().strip('"').strip("'").replace('file:///', '')

def formatador_json():
    # Ativa o estilo Matrix (Fundo preto, Letras verdes)
    os.system('color 0a')
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("="*60)
        print("           FORMATADOR DE JSON OFFLINE (MATRIX)")
        print("="*60)
        
        entrada = input("\nArraste o arquivo .json/.txt aqui (ou cole o JSON puro) e aperte Enter:\n> ")
        entrada = limpar_caminho(entrada)
        
        if not entrada:
            continue
            
        try:
            # Tenta verificar se a entrada é um arquivo físico
            if os.path.exists(entrada):
                print("\nLendo arquivo e formatando...")
                with open(entrada, 'r', encoding='utf-8') as f:
                    dados = json.load(f)
                
                # Cria o nome do novo arquivo formatado
                caminho_saida = entrada.rsplit('.', 1)[0] + "_formatado.json"
                
                with open(caminho_saida, 'w', encoding='utf-8') as f:
                    json.dump(dados, f, indent=4, ensure_ascii=False)
                    
                print(f"\n✅ Sucesso! Arquivo formatado e salvo em:\n{caminho_saida}")
                
            else:
                # Caso o usuário tenha colado o texto JSON direto no terminal
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
            print("\nEncerrando o Formatador... Até logo!")
            time.sleep(2)
            break

if __name__ == "__main__":
    formatador_json()