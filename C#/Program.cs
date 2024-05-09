// See https://aka.ms/new-console-template for more information
using System.Globalization;
using System.Security.Cryptography;
using C_.Models;
using C_.Utils;
/*
Pessoa p1 = new Pessoa(nome:"Matrix", idade:28);
Pessoa p2 = new Pessoa(nome:"Venon", idade:38);
Pessoa p3 = new Pessoa(nome:"Spider", idade:18);

Console.WriteLine($"Nome: {p1.Nome}, Idade:{p1.Idade}");

Curso c1= new Curso();
c1.Nome = "ESI";
c1.AdicionarAlunos(p1);
c1.AdicionarAlunos(p2);
c1.AdicionarAlunos(p3);
int n = c1.NumeroDeAlunosMaticulados();
Console.WriteLine($"Nome do curso: {c1.Nome}, Número de alunos: {n}");
c1.ListaAlunosMatriculados();
*/

Utils m = new Utils();
 m.Money(1000000M);
 m.porcentagem(.80);
 m.separa(1000000);
 m.DataHoje();

 Arquivo a = new Arquivo();
 a.LeArquivo();
