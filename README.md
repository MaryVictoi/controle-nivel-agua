![Banner do Projeto](Design%20sem%20nome.png)

<div align="center">



# 💧 Sistema de Controle e Monitoramento do Nível de Água de Reservatório



![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Colorama](https://img.shields.io/badge/Library-Colorama-4B8BBE?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Conclu%C3%ADdo-success?style=for-the-badge)



Sistema desenvolvido em **Python** para simular o monitoramento do nível de água de um reservatório por meio do terminal, utilizando cores para identificar diferentes situações operacionais.



</div>



---



## 📌 Sobre o projeto



Este projeto foi desenvolvido como atividade da disciplina **Desenvolvimento de Sistemas I**, no curso técnico em **Desenvolvimento de Sistemas** da **ETEC — Centro Paula Souza**.



O sistema simula um painel de monitoramento que exibe cinco níveis de água, cada um associado a uma situação específica e a uma cor de alerta no terminal. A proposta aplica conceitos de **programação estruturada**, **modularização**, **estruturas de dados** e **utilização de bibliotecas externas**.



---



## ⚙️ Funcionalidades



- Exibição do nível atual do reservatório no terminal.
- Identificação visual por cores conforme o nível de risco.
- Estrutura de dados baseada em listas e tuplas.
- Funções modularizadas para separar responsabilidades.
- Utilização da biblioteca `colorama` para formatação colorida.
- Restauração automática do estilo padrão do terminal.



---



## 🎨 Níveis e cores de alerta



| Nível | Situação do reservatório | Grau de risco | Cor |
|:---:|---|---|:---:|
| 1 | Muito baixo (crítico) | Crítico | 🔴 Vermelho |
| 2 | Baixo | Atenção | 🟡 Amarelo |
| 3 | Médio | Condição normal | 🟢 Verde |
| 4 | Alto | Elevado | 🔵 Ciano |
| 5 | Muito alto (alerta) | Risco de transbordamento | 🔷 Azul |



---



## 🖥️ Demonstração



```text
=====================================================
      PAINEL DE MONITORAMENTO DO RESERVATÓRIO        
=====================================================



Nível 1: Muito baixo (crítico)
Nível 2: Baixo
Nível 3: Médio
Nível 4: Alto
Nível 5: Muito alto (alerta)



=====================================================
Monitoramento finalizado com sucesso.
```



> 💡 No terminal, cada mensagem é exibida com a cor correspondente ao nível informado.



---



## 🧠 Tecnologias utilizadas



| Tecnologia | Finalidade |
|---|---|
| ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) | Linguagem de programação |
| ![Colorama](https://img.shields.io/badge/Colorama-4B8BBE?style=flat-square) | Colorização do texto no terminal |
| ![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white) | Controle de versão |
| ![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white) | Hospedagem do repositório |



---



## 📂 Estrutura do projeto



```text
controle-nivel-agua/
├── main.py               # Código-fonte principal
├── requirements.txt      # Dependências do projeto
├── README.md             # Documentação do projeto
└── .gitignore            # Arquivos ignorados pelo Git
```



---


## 📈 Possíveis melhorias



- [ ] Permitir que o usuário informe o nível manualmente.
- [ ] Adicionar validação de entradas inválidas.
- [ ] Criar modo de monitoramento contínuo.
- [ ] Gerar relatórios em arquivo `.txt` ou `.csv`.
- [ ] Desenvolver interface gráfica com Tkinter.
- [ ] Implementar testes automatizados com `pytest`.


</div>
