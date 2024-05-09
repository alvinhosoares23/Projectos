using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace C_.Models
{
    public class Curso
    {
        public Curso()
        {

            Alunos = new List<Pessoa>(); // Inicializa a lista de alunos
        }
        public string Nome { get; set; }
        
        public List<Pessoa> Alunos { get; set; }


        public void AdicionarAlunos(Pessoa aluno){
            Alunos.Add(aluno);
        }
        public bool RemoverAlunos(Pessoa aluno){
            return Alunos.Remove(aluno);
        }
        public int NumeroDeAlunosMaticulados(){
            int NumeroAlunos = Alunos.Count;
            return NumeroAlunos;
        }
        public void ListaAlunosMatriculados(){
            int cont = 0;            
            Console.WriteLine($"============== Alunos Matriculados no Curso {Nome} ===============");
            foreach(Pessoa aluno in Alunos){
                Console.WriteLine($"{++cont}-{aluno.Nome}-{aluno.Idade}");
            }
        }
    }
}