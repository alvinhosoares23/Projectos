using System;
using System.Collections.Generic;
using System.Globalization;
using System.Linq;
using System.Threading.Tasks;

namespace C_.Utils
{
    public class Utils
    {
        public void Money(decimal valor){
            CultureInfo.DefaultThreadCurrentCulture = new CultureInfo("pt-pt");
            Console.WriteLine(valor.ToString("C"));
        }
        public void porcentagem(double numero){
            Console.WriteLine(numero.ToString("P"));
        }
        public void separa(int numero){
            Console.WriteLine(numero.ToString("###-###-###"));
        }
        public void DataHoje(){
            DateTime data = DateTime.Now;
            Console.WriteLine(data.ToString("dd/MM/yyyy"));
        }
    }
}