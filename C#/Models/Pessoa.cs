using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace C_.Models
{
    public class Pessoa
    {
        public Pessoa(){

        }
        public Pessoa(string nome, int idade){
            Nome = nome;
            Idade = idade;
        }

        private string _nome;
        private int _idade;
        //public string NomeCompleto = $"{}";
        public string Nome { 
            get => _nome; 
            set{
                if (value == "" ){
                    throw new ArgumentException("Nome Não pode ser vazio!");
                }
                _nome = value;
            }
         }
        public int Idade { 
            get => _idade;
            set{
                if (value < 1 ){
                    throw new ArgumentException("Idade não pode ser Negativo ou nulo");
                }
                _idade = value;
            } }        
        
        public void Apresentar(){
            Console.WriteLine($"Nome: {Nome}, Idade: {Idade}");
        }
    }
}