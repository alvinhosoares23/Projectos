using System;
using System.Collections.Generic;
using System.Data;
using System.Linq;
using System.Threading.Tasks;

namespace C_.Utils
{
    public class Arquivo
    {

        public void LeArquivo(){
            string[] linhas = new string[0]; 
            try
            {
                 linhas = File.ReadAllLines("Arquivos/arq.txt");
                
            }
            catch (FileNotFoundException ex)
            {
                
                Console.WriteLine($"Erro!!! Arquivo não Encontrado \n {ex.Message}");
            }
            catch (DirectoryNotFoundException ex)
            {
                
                Console.WriteLine($"Erro!!! Diretorio não Encontrado \n {ex.Message}");
            }
            catch (Exception ex)
            {
                
                Console.WriteLine($"Erro!!! Ocorreu um erro ao tentar abrir o arquivo! \n {ex.Message}");
            }
            foreach (string linha in linhas)
            {
                Console.WriteLine(linha);
            }
        }
        
    }
}