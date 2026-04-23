# Documentação do Projeto - Neurônio Avaliador de Notas

## Visão Geral

Este projeto implementa um **neurônio artificial** para calcular a nota bimestral de um aluno baseado em diferentes avaliações com pesos personalizáveis. O sistema utiliza uma rede neural simplificada (perceptron) para combinar notas de trabalho, resumo e prova, demonstrando os conceitos fundamentais de computação neural.

## Objetivos

- Demonstrar o funcionamento de um neurônio artificial e seu uso prático
- Calcular a nota bimestral final aplicando pesos ajustáveis a cada avaliação
- Fornecer uma interface interativa para visualizar como as mudanças nos pesos afetam o resultado
- Decompor e explicar o cálculo da nota através de visualizações

## Estrutura do Projeto

```
2026-04-22/
│
├── app.py              # Interface interativa com Streamlit
├── neuronio.py         # Implementação da classe NeuronioAvaliador
├── requirements.txt    # Dependências do projeto
└── README.md           # Este arquivo
```

## Componentes Principais

### `neuronio.py`

Implementação da classe `NeuronioAvaliador` que encapsula a lógica do neurônio artificial.

**Características:**
- Armazena os pesos (importância relativa) de cada entrada: `peso_trabalho`, `peso_resumo`, `peso_prova`
- Armazena o bias: ajuste fino que pode aumentar ou diminuir a saída geral
- Método `calcular_nota()`: realiza a computação neuronal

**Fórmula do Neurônio:**
```
Soma Ponderada = (peso_trabalho × nota_trabalho) + 
                 (peso_resumo × nota_resumo) + 
                 (peso_prova × nota_prova) + 
                 bias

Nota Final = max(0.0, min(10.0, Soma Ponderada))
```

A função de ativação utiliza uma **função identidade com cláusula de segurança**, garantindo que o resultado sempre fico entre 0 e 10.

### `app.py`

Interface interativa desenvolvida com **Streamlit** que permite:

- **Configuração de Pesos** (sidebar): 
  - Ajustar a importância de cada avaliação via sliders
  - Visualizar a soma total dos pesos
  - Modificar o bias para ajuste fino

- **Inserção de Notas** (coloque principal):
  - Digitar notas individuais (0-10) para trabalho, resumo e prova
  - Valores padrão para demonstração rápida

- **Visualização de Resultados**:
  - Nota bimestral final com indicador de desempenho (Excelente, Muito Bom, Bom, Insuficiente)
  - Decomposição da contribuição de cada avaliação
  - Gráfico em barras mostrando a distribuição de contribuição
  - Indicador de aprovação (≥ 6.0) ou reprovação

## Como Executar

### 1. Crie um ambiente virtual (recomendado)

```bash
python -m venv .venv
```

### 2. Ative o ambiente virtual

- **Windows:**
  ```bash
  .venv\Scripts\activate
  ```

- **Linux/Mac:**
  ```bash
  source .venv/bin/activate
  ```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute a aplicação

```bash
streamlit run app.py
```

A aplicação abrirá automaticamente no navegador padrão no endereço `http://localhost:8501`.

## Uso da Aplicação

1. **Ajuste os pesos na barra lateral** (⚙️ Configuração dos Pesos):
   - Cada slider permite valores de 0.0 a 1.0
   - A soma dos pesos é exibida para referência
   - Não é obrigatório que a soma seja 1.0, mas recomenda-se normalizar

2. **Insira as notas dos alunos** (📊 Inserir Notas):
   - Digite as notas de trabalho, resumo e prova (0-10)
   - Os valores podem ser decimais (ex: 7.5)

3. **Visualize o resultado** (✨ Resultado):
   - A nota bimestral final é exibida com o indicador de desempenho
   - A decomposição mostra quanto cada avaliação contribuiu para a nota final

4. **(Opcional) Explore a decomposição** (📈 Decomposição da Nota):
   - Veja a contribuição individual de cada avaliação
   - Acompanhe o cálculo da soma ponderada com a fórmula matemática
   - Visualize o gráfico de distribuição de contribuição

## Conceitos Técnicos

### O Neurônio Artificial

Um **neurônio artificial** é a unidade básica de uma rede neural. Funciona de forma análoga a um neurônio biológico:

- **Entradas** (`inputs`): nota_trabalho, nota_resumo, nota_prova
- **Pesos** (`weights`): peso_trabalho, peso_resumo, peso_prova (representam a importância relativa)
- **Soma Ponderada** (`weighted sum`): combinação linear das entradas com seus pesos
- **Bias**: termo aditivo que permite ajuste fino do resultado
- **Função de Ativação** (`activation function`): transforma a soma em uma saída final (neste caso, clamping entre 0 e 10)

### Funcionamento

O neurônio realiza a seguinte sequência:

1. **Multiplica** cada entrada pelo seu peso correspondente
2. **Soma** todos os produtos ponderados
3. **Adiciona** o bias
4. **Aplica** a função de ativação para garantir que o resultado está no intervalo válido

### Pesos e Bias

- **Pesos**: Quanto maior o peso, mais importância aquela avaliação tem na nota final. Um peso 0.6 para prova significa que a prova representa 60% da importância relativa.
- **Bias**: Permite aumentar ou diminuir a nota base. Um bias de +2.0 adiciona 2 pontos à nota final, útil para ajustes finos.

### Cenários de Uso

**Exemplo 1: Prova mais importante**
```
Pesos: trabalho=0.2, resumo=0.1, prova=0.7
Um aluno com notas 8.0, 9.0, 7.5 terá:
Soma = (0.2×8.0) + (0.1×9.0) + (0.7×7.5) = 1.6 + 0.9 + 5.25 = 7.75
Nota Final = 7.75 (sem bias)
```

**Exemplo 2: Avaliações mais balanceadas**
```
Pesos: trabalho=0.33, resumo=0.33, prova=0.34
Mesmas notas resulta em média próxima a 8.17
```

**Exemplo 3: Ajuste com bias positivo**
```
Pesos: trabalho=0.3, resumo=0.1, prova=0.6
Bias: +1.0
Aluno com notas 7.0, 8.0, 6.0:
Soma = (0.3×7.0) + (0.1×8.0) + (0.6×6.0) + 1.0 = 2.1 + 0.8 + 3.6 + 1.0 = 7.5
Nota Final = 7.5
```

## Configuração e Personalização

### Alterando Valores Padrão

Para modificar os valores padrão da aplicação, edite o arquivo `app.py`:

- **Valor padrão dos pesos**: Procure pelos valores de `value=` nos sliders (linhas 23-45)
- **Notas de exemplo**: Procure pelos `value=` dos `number_input` (linhas 70-89)
- **Limites e incrementos**: Altere `min_value`, `max_value`, `step` nos sliders

### Exemplo de Ajuste

Para alterar o peso padrão do trabalho de 0.3 para 0.4:

```python
peso_trabalho = st.sidebar.slider(
    "Peso do Trabalho",
    min_value=0.0,
    max_value=1.0,
    value=0.4,  # ← Alterado de 0.3
    step=0.05
)
```

### Alterando Critérios de Aprovação

Para mudar o critério de aprovação (atualmente 6.0), edite a linha que contém:

```python
if nota_final >= 6.0:
    st.success("✅ Aluno Aprovado")
else:
    st.error("❌ Aluno Reprovado")
```

## Interpretação dos Resultados

### Indicadores de Desempenho

| Intervalo | Status | Cor |
|-----------|--------|-----|
| 9.0 - 10.0 | 🌟 Excelente | Verde |
| 7.0 - 8.9 | 💪 Muito Bom | Azul |
| 5.0 - 6.9 | 👍 Bom | Laranja |
| 0.0 - 4.9 | ⚠️ Insuficiente | Vermelho |

### Contribuição de Cada Avaliação

A coluna "Decomposição da Nota" mostra quanto cada avaliação contribuiu para o resultado final:

```
Contribuição = peso × nota

Se peso_prova=0.6 e nota_prova=8.0:
Contribuição da Prova = 0.6 × 8.0 = 4.8
```

## Troubleshooting

**Streamlit não encontrado:**
```bash
pip install streamlit
```

**Erro ao executar `streamlit run app.py`:**
- Certifique-se de que está no diretório correto
- Verifique se o ambiente virtual foi ativado
- Reinstale as dependências: `pip install -r requirements.txt --force-reinstall`

**Aplicação não abre no navegador:**
- A aplicação pode estar rodando em outra porta (ex: 8502)
- Verifique o terminal para encontrar a URL correta
- Acesse manualmente a URL mostrada no terminal

**Valores estranhos ou overflow:**
- Certifique-se de que os pesos não criam uma soma ponderada > 20 com bias positivo
- Use o bias apenas como ajuste fino (geralmente entre -2.0 e +2.0)

## Extensões Futuras

Possíveis melhorias e extensões do projeto:

- Adicionar múltiplos neurônios em camadas (rede neural profunda)
- Implementar função de ativação ReLU ou Sigmoid
- Adicionar histórico de avaliações e evolução de notas
- Exportar relatórios em PDF
- Persistir configurações de peso em arquivo
- Adicionar dashboard com estatísticas da turma

## Conceitos Educacionais

Este projeto demonstra:

1. **Neurônio Artificial**: Unidade básica de redes neurais
2. **Pesos e Bias**: Parâmetros aprendíveis de um modelo neural
3. **Função de Ativação**: Transformação não-linear (neste caso linear com clamping)
4. **Computação Linear**: Combinação ponderada de entradas
5. **Interatividade e Visualização**: Como parâmetros afetam a saída

## Licença

Este projeto está sob a licença MIT. Você pode usar, copiar, modificar e distribuir livremente.
