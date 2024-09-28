# Guida per Scrivere Formule in LaTeX su Moodle

Alcuni dei problemi e quiz su Moodle richiedono di scrivere la risposta in un campo di testo.

In questa pagina riassumo le basi per  scrivere formule matematiche nel campo testo Moodle adoperando la sintassi del linguaggio LaTeX.

Ecco come farlo utilizzando i delimitatori corretti per Moodle.

## 1. Scrivere Formule Inline

Le formule inline sono quelle inserite all'interno del testo. Puoi utilizzare uno dei seguenti delimitatori:
- `\( ... \)` oppure
- `$ ... $`

Esempio:

```markdown
La famosa equazione di Einstein è \( E = mc^2 \).
```

Oppure:

```markdown
La famosa equazione di Einstein è $E = mc^2$.
```

Entrambi i metodi produrranno la formula inline.

## 2. Scrivere Formule in Modalità Display (su Nuova Linea)

Le formule in modalità display vengono mostrate su una nuova linea e sono formattate in modo più evidente. Utilizza uno dei seguenti delimitatori:
- `\[ ... \]` oppure
- `$$ ... $$`

Esempio:

```markdown
\[ E = mc^2 \]
```

Oppure:

```markdown
$$
E = mc^2
$$
```

Questi delimitatori fanno sì che la formula venga visualizzata su una nuova linea.

## 3. Esempi di Formule Comuni

### Equazione Quadratica

La formula dell'equazione quadratica è:

```markdown
\[ ax^2 + bx + c = 0 \]
```

### Formula di Pitagora

```markdown
\[ a^2 + b^2 = c^2 \]
```

### Derivata di una Funzione

Se hai una funzione \( f(x) \), la sua derivata è:

```markdown
\[ \frac{d}{dx} f(x) = f'(x) \]
```

### Somma di una Serie

```markdown
\[ \sum_{i=1}^{n} i = rac{n(n + 1)}{2} \]
```

## 4. Apici e Sottoscritti

Per scrivere indici e apici, usa:
- `_` per il sottoscritto
- `^` per l'apice

Esempio:

```markdown
\( x_i \) per il sottoscritto, e \( x^2 \) per l'apice.
```

## 5. Altri Operatori e Funzioni

Ecco alcuni operatori comuni che puoi utilizzare:

- Somma: `\sum`
- Integrale: `\int`
- Prodotto: `\prod`
- Limite: `\lim`

Esempio di integrale:

```markdown
\[ \int_{0}^{1} x^2 \, dx = \frac{1}{3} \]
```

## 6. Matrici

Per scrivere matrici, puoi utilizzare l'ambiente `matrix`:

```markdown
\[ \begin{matrix}
a_{11} & a_{12} \
a_{21} & a_{22}
\end{matrix} \]
```

## 7. Consigli Utili

- **Testa le tue Formule**: Utilizza la funzione di anteprima di Moodle per verificare che le tue formule siano visualizzate correttamente.
- **Utilizza MathJax o il Filtro TeX**: Se Moodle utilizza il renderer MathJax o il filtro TeX, puoi usare tranquillamente i delimitatori descritti sopra.
- **Consultare la Documentazione**: Se hai bisogno di ulteriori dettagli, puoi consultare la [documentazione ufficiale di Moodle](https://docs.moodle.org).
