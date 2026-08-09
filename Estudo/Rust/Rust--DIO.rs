//Estudo Rust

//TIPOS DE DADOS ******************
//INTEIROS
i8
i16
i32
i64
isize //baseado ma arquitetura do pc x32 x64

//INTEIRO SEM SINAL (positivos)
u8
u16
...
usize

//FLOAT
f32
f64

//OUTROS
bool //BOLEANO
char //CARACTERES ➡️




















//importações lib standard Rust
use std::fs::file; //handler arquivos
use std::io::{Write, Result}; //varios modulos
use std::time::Duration; //time sleep
use std::net::Tcplistener; //ouvinte da posta tcp






















//ESTRUTURAS ********************
fn criar_miltiplicador(num: i32) -> impl Fn(i32) -> i32{  //"closure" cria uma variavel dinâmica. 
    move|multiplicador| num * multiplicador               //Onde declarando uma variavel fora do código 
}                                                         //pode alocar um valor diferente para "multiplicador"   


struct Pessoa { //usado como modelador de objeto
     nome: String;
     CPF: String;
     idade: i32;
     peso: f32;
}

enum Profisso { //Usado como seletor
    Dentista(i32), //recebe dados tipados *tupla
    Mecanico {idade: i32, endereço: String}, //recebe struct anônima
    Medico
}

trait Trabalho { //coloca uma regra para onde for implementado
    fn trabalhar(&self) -> String; //obrigatorio
    fn descansar(&self) {
        println!("")
    }
}
 


















//***TRATAMENTO DE ERROS
enum Result{
    Ok;
    Err;
}




















//desafios
fn dobrar(n: i32) -> String {
    n = n * 2;
}
fn main() {
    println!("{}", dobrar(5)); // deve imprimir 10
}

// 
fn pair(n: i32) -> String {
    let divisao: i32 = n % 2;
    if divisao == 0{
        let par: string::From("{} é par", n)
    }else{
        let impar: string::From("{} é impar", n)
    }
}

fn main{
    println!("{}", pair(4))
}























//********* MACROS
macro_rules! cria_struct {
    //captura o nome da struct e seus campos
    ($nome_struct:ident { $($campo:ident: $tipo:ty),* $(,)? }) => {
    //nome:ident(padrão)
    //"$campo:ident" e "$tipo:ty" é variável
    //",*" para dizer que a struct não tem limite de campos
    //"$(,)" para auto regular a virgula na ultimo campo da struct



        //define a struct

        #[derive{Debug}]
        struct $nome_struct {
            $($campo: $tipo,)*
        }
    }
}

//Macros Procesual
#[proc_macro_derive(MeuTrait)]
pub fn meu_trait_derive(input: TokenStream) -> TokenStream{  //"input: TokenStream" recebe o nome da struct no código //TokenStream é um tipo de strutura que o rust entende como trechos de código
    let input: DeriveInput = parse_macro_input(input as DeriveInput); //parseando a variável do nome da struct para tratar dentro da função


    let name: Indent = input.indent; //puxa um atributo da variavel input
    let expanded: TokenStream = quote! {        //variavel >> implementaçao >> funçao
        impl MeuTrait for #name {               //"quote!"é uma forma de guardar um objeto
            fn minha_funcao(&self) -> string {  //"minha_funcao" é a trait que será implementada
                String::from ("Implementação padrão do MeuTrait")
            }
        }
    };
    TokenStream::from(expanded)
}












//******concorrência e paralelismo
//limite de Threads
use rayon::threadPoolBuilder;
threadPoolBuilder::new().num_threads(4).builder_global().unwrap(); //limita o uso de numeros de threads

//iteração paralela
.par_iter(); 
.into_par_iter();//dentro de vetores












//******exemplos
//criaçao arquivo
let arquivo_nome: String = format!("cliente_{}.txt", ciente.id);
let mut arquivo: File = file::create(path: arquivo_nome); //cria um arquivo na pasta raiz















//Result->   Ok(), Err()
fn is_pair(num: i32) -> Result<&str, &str> { //posso escolher a saída do Result (String, i32, io::Error, etc...)
    if (num % 2) == 0 {
        Ok("Numero par")
    }else {
        Err("Numero impar")
    }
}

























//*******TCP Listener
use std::net::Tcplistener; //ouvinte da posta tcp
let listener: Tcplistener =Tcplistener::bind{addr: "127.0.0.1:8080"}?; //cria ouvinte TCP na porta 8080
........











//******persistencia de dados
 